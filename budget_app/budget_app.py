"""
Instantiate objects based on different budget categories like food,
clothing, and entertainment. When objects are created, they are passed
in the name of the category. The class have an instance variable called
'ledger' that is a list. The class also contain the following methods:
- A 'deposit' method that accepts an amount and description. If no
description is given, it defaults to an empty string. The method append
an object to the ledger list.
- A 'withdraw' method that is similar to the 'deposit' method, but the
amount passed in is stored in the ledger as a negative number. If there
are not enough funds, nothing is added to the ledger.
- A 'get_balance' method that returns the current balance of the budget
category based on the deposits and withdrawals that have occurred.
- A 'transfer' method that accepts an amount and another budget
category as arguments. The method adds a withdrawal with the amount.
The method then adds a deposit to the other budget category with the
amount. If there aren't enough funds, nothing is added.
- A 'check_funds' method that accepts an amount as an argument. It
returns 'False' if the amount is greater than the balance of the budget
category and returns 'True' otherwise.
"""


class Category:
    name: str
    ledger: list[dict]
    
    def __init__(self, name: str):
        self.name = name
        self.ledger = []
        
    def __str__(self) -> str:
        self.name = self.name.center(30 , '*')
        to_string = f'{self.name}\n'
        
        for e in self.ledger:
            desc = e['description']
            
            if len(desc) > 23:
                desc = desc[:23]
                
            ws = 23 - len(desc)
            to_string += f'{desc}'
            
            while ws > 0:
                to_string += ' '
                ws -= 1
            
            amount = e['amount']
            amount = round(amount, 2)
            amount = str(amount)
            
            if amount.count('.') == 0:
                amount += '.00'
            
            if len(amount) > 7:
                famount = amount.split('.')
                amount = famount[0]
                amount = amount[:4]
                amount += f'.{famount[1]}'
                
            ws = 7 - len(amount)
            
            while ws > 0:
                to_string += ' '
                ws -= 1
            
            to_string += f'{amount}\n'
            
        to_string += f'Total: {self.get_balance()}'
    
        return to_string
    
    def deposit(self, amount: float, description=''):
        d = {'amount': amount, 'description': description}
        self.ledger.append(d)
        
    def withdrawn(self, amount: float, description ='') -> bool:
        if not self.check_funds(amount):
            return False
        
        amount *= -1
        d = {'amount': amount, 'description': description}
        self.ledger.append(d)
        return True
    
    def get_balance(self) -> float:
        current_balance = 0.0
        
        for e in self.ledger:
            current_balance += e['amount']
        
        current_balance = round(current_balance, 2)
        
        return current_balance
    
    def transfer(self, amount: float, destination: object) -> bool:
        if not self.check_funds(amount):
            return False
        
        dname = destination.name.strip('*')
        desc = f'Transfer to {dname}'
        self.withdrawn(amount, description=desc)
        
        stname = self.name.strip('*')
        desc = f'Transfer from {stname}'
        destination.deposit(amount, description=desc)
        
        return True
    
    def check_funds(self, amount: float) -> bool:
        if amount > self.get_balance():
            return False
        else:
            return True


def create_spend_chart(categories: list[Category]) -> str:
    bar_chart = 'Percentage spent by category\n'
    d = {}
    
    for e in categories:
        total_spent = 0.0
        
        for i in e.ledger:
            if i['amount'] < 0 and not i['description'].startswith('Transfer'):
                total_spent += i['amount']
        
        d.update({e.name: total_spent})  
    
    b = 0.0    
    
    for k, v in d.items():
        v *= -1
        d[k] = v
        b += v
    
    for k, v in d.items():
        v = round((v * 100) / b, 0)
        c = 0
        
        while v >= 10:
            c += 1
            v -= 10
        
        d[k] = c
    
    l = []
    
    for e in d.values():
        l.append(e)

    p = 100
    pd = p / 10
    
    while p >= 0:
        pl = f' {p}| '
        
        if p == 100:
            bar_chart += '100| '
        elif p == 0:
            bar_chart += '  0| '
        else:
            bar_chart += pl
        
        index = 0
        
        for e in l:
            if e == pd:
                bar_chart += 'o  '
                l[index] -= 1
            else:
                bar_chart += '   '
                
            index += 1
                
        bar_chart += '\n'
        pd -= 1
        p -= 10

    bar_chart += '----'
    p = 1 + (3*len(l))
    
    while p > 0:
        bar_chart += '-'
        p -= 1
    
    bar_chart += '\n     '
    l.clear()
    
    for e in categories:
        stname = e.name.strip('*')
        c = len(stname)
        l.append(c)
    
    m = max(l)
    index = 0
    
    while m > 0:
        for e in categories:
            stname = e.name.strip('*')
            
            if len(stname) > index:
                bar_chart += f'{stname[index]}  '
            else:
                bar_chart += '   '
                continue
            
        index += 1
        bar_chart += '\n     '
        m -= 1
    
    return bar_chart


# Tests
f = Category('Food')
e = Category('Entertainment')
b = Category('Business')

print('[Test 1: Deposit]')
f.deposit(900, 'deposit')
print(f, '\n')
f.ledger.clear()

print('[Test 2: Deposit without Description]')
f.deposit(45.46)
print(f, '\n')
f.ledger.clear()

print('[Test 3: Withdrawn]')
f.deposit(900, 'deposit')
f.withdrawn(45.67, 'milk, cereal, eggs, bacon, bread')
print(f, '\n')
f.ledger.clear()

print('[Test 4: Withdrawn without Description]')
f.deposit(900, 'deposit')
f.withdrawn(45.67)
print(f, '\n')
f.ledger.clear()

print('[Test 5: Get Balance]')
f.deposit(900, 'deposit')
f.withdrawn(45.67, 'milk, cereal, eggs, bacon, bread')
print(f.get_balance(), '\n')
f.ledger.clear()

print('[Test 6: Transfer]')
f.deposit(900, 'deposit')
f.withdrawn(45.67, 'milk, cereal, eggs, bacon, bread')
f.transfer(20, e)
print(f, '\n')
print(e, '\n')
f.ledger.clear()
e.ledger.clear()

print('[Test 7: Check Funds]')
f.deposit(10, 'deposit')
print(f.check_funds(20))
print(f.check_funds(10))
print()
f.ledger.clear()

print('[Test 8: Withdrawn with not enough Funds]')
f.deposit(100, 'deposit')
print(f.withdrawn(100.10), '\n')
f.ledger.clear()

print('[Test 9: Transfer with not enough Funds]')
f.deposit(100, 'deposit')
print(f.transfer(200, e), '\n')
f.ledger.clear()

print('[Test 10: To String]')
f.deposit(900, 'deposit')
f.withdrawn(45.67, 'milk, cereal, eggs, bacon, bread')
f.transfer(20, e)
print(f, '\n')
print(e, '\n')
f.ledger.clear()
e.ledger.clear()

print('[Test 11: Create Spend Chart]')
f.deposit(900, 'deposit')
e.deposit(900, 'deposit')
b.deposit(900, 'deposit')
f.withdrawn(105.55)
e.withdrawn(33.40)
b.withdrawn(10.99)
print(create_spend_chart([b, f, e]), '\n')
f.ledger.clear()
b.ledger.clear()
e.ledger.clear()
