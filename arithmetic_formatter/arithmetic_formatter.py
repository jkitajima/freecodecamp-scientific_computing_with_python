"""
Enter arithmetical operations to get them properly formatted.
Only addiction and subtraction operations accepted.
Maximum of 4 operations on each execution.

Parameters
----------
List of Strings. Each element represents an arithmetical operation.
Must have a whitespace between the numbers and the operation symbol.

Examples
--------
>>> arithmetic_arranger(["32 + 698", "3801 - 2"])
   32      3801
+ 698    -    2
-----    ------
  730      3799
  
Results are optional. Should enter an optional boolean parameter to
show results.
"""


def arithmetic_arranger(problems, show_results=False):
    if len(problems) > 5:
        raise Exception('Error: Too many problems.')
    
    arranged_problems = ''
    operations = []

    for e in problems:
        operations.append(e.split())

    uplen: int
    botlen: int
    maxlen: int
    trad: bool
    line1, line2, line3, line4 = '', '', '', ''

    for e in operations:
        if e[1] == '/' or e[1] == '*':
            raise Exception("Error: Operator must be '+' or '-'.")

        if not e[0].isdigit() or not e[2].isdigit():
            raise Exception('Error: Numbers must only contain digits.')

        if len(e[0]) > 4 or len(e[2]) > 4:
            raise Exception('Error: Numbers cannot be more than four digits.')

        uplen = len(e[0])
        botlen = len(e[2])

        if uplen >= botlen:
            maxlen = uplen
            trad = True
        else:
            maxlen = botlen
            trad = False

        e.append(maxlen)

        if trad:
            ws1 = e[3] + 2
            ws2 = ws1 - len(e[2]) - 1
            
            while ws1 > e[3]:
                line1 += ' '
                ws1 -= 1
                
            ws1 = e[3] + 2
            line1 += e[0]
            line1 += '    '
            line2 += e[1]
            
            while ws2 > 0:
                line2 += ' '
                ws2 -= 1
                
            line2 += e[2]
            line2 += '    '
            
            while ws1 > 0:
                line3 += '-'
                ws1 -= 1
                
            line3 += '    '
        else:
            ws1 = e[3] + 2 - len(e[0])
            
            while ws1 > 0:
                line1 += ' '
                ws1 -= 1
                
            line1 += e[0]
            line1 += '    '
            line2 += e[1]
            line2 += ' '
            line2 += e[2]
            line2 += '    '
            ws1 = e[3] + 2
            
            while ws1 > 0:
                line3 += '-'
                ws1 -= 1
            
            line3 += '    '
        
        num1: str
        sy: str
        num2: str
        result: int
        ws4 = 0

        if show_results:
            num1 = e[0]
            num1 = int(num1)
            sy = e[1]
            num2 = e[2]
            num2 = int(num2)
            
            if sy == '+':
                result = num1 + num2
            elif sy == '-':
                result = num1 - num2
                
            result = str(result)
            ws4 = e[3] + 2 - len(result)
            
            while ws4 > 0:
                line4 += ' '
                ws4 -= 1
                
            line4 += result
            line4 += '    '

    arranged_problems += line1 + '\n'
    arranged_problems += line2 + '\n'

    if not show_results:
        arranged_problems += line3
    else:
        arranged_problems += line3 + '\n'
    
    arranged_problems += line4

    return arranged_problems


# Tests
print('[Test 1: Two Problems Arrangement 1]')
print(arithmetic_arranger(["3801 - 2", "123 + 49"]))

print('\n\n[Test 2: Two Problems Arrangement 2]')
print(arithmetic_arranger(["1 + 2", "1 - 9380"]))

print('\n\n[Test 3: Four Problems Arrangement]')
print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))

print('\n\n[Test 4: Five Problems Arrangement]')
print(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))

# Uncomment to see the exception
# print(f'\n\n[Test 5: Too Many Problems]\n{arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 +40", "653 + 87"])}')

# Uncomment to see the exception
# print(f'\n\n[Test 6: Incorrect Operator]\n{arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])}')

# Uncomment to see the exception
# print(f'\n\n[Test 7: Too Many Digits]\n{arithmetic_arranger(["24 + 85215", "3801 + 2", "45 + 43", "123 + 49"])}')

# Uncomment to see the exception
# print(f'\n\n[Test 8: Only Digits]\n{arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])}')

print(f'\n\n[Test 9: Two Problems with Solutions]\n{arithmetic_arranger(["3 + 855", "988 + 40"], True)}')

print(f'\n\n[Test 10: Five Problems with Solutions]\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')
