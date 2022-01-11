"""
Shape Calculator using Rectangles and Squares.
These are classes and must be instantianted in order to use methods.
"""


class Rectangle:
    width: int
    height: int
    
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        
    def __str__(self) -> str:
        return f'Rectangle(width={self.width}, height={self.height})'
        
    def set_width(self, width: int):
        self.width = width
    
    def set_height(self, height: int):
        self.height = height
        
    def get_area(self) -> float:
        return float(self.width * self.height)
    
    def get_perimeter(self) -> int:
        return 2*self.width + 2*self.height
    
    def get_diagonal(self) -> float:
        return float((self.width**2 + self.height**2) ** .5)
    
    def get_picture(self) -> str:
        if self.width>50 or self.height>50:
            return 'Too big for picture.'
        
        h = self.height
        w = self.width
        shape = ''
        
        while h > 0:
            while w > 0:
                shape += '*'
                w -= 1
            
            w = self.width
            shape += '\n'
            h -= 1
        
        return shape
    
    def get_amount_inside(self, shape: object) -> int:
        area1 = self.get_area()
        area2 = shape.get_area()
        amount = round(area1 / area2, 4)
        st = str(amount)
        st = st.split('.')[0]
        st = int(st)
        
        return st


class Square(Rectangle):
    side: int
    
    def __init__(self, side: int):
        self.width = side
        self.height = side

    def __str__(self) -> str:
        return f'Square(side={self.width})'
    
    def set_side(self, side: int):
        self.width = side
        self.height = side
    
    def set_width(self, side: int):
        self.width = side
        self.height = side
        
    def set_height(self, side: int):
        self.width = side
        self.height = side


# Tests
r = Rectangle(3, 6)
s = Square(5)

print('[Test 1: Subclass]')
print(issubclass(Square, Rectangle), end='\n\n')

print('[Test 2: Rectangle String]')
print(r, end='\n\n')

print('[Test 3: Square String]')
print(s, end='\n\n')

print('[Test 4: Area]')
print(f'Rect.: {r.get_area()}')
print(f'Sq.: {s.get_area()}', end='\n\n')

print('[Test 5: Perimeter]')
print(f'Rect.: {r.get_perimeter()}')
print(f'Sq.: {s.get_perimeter()}', end='\n\n')

print('[Test 6: Diagonal]')
print(f'Rect.: {r.get_diagonal()}')
print(f'Sq.: {s.get_diagonal()}', end='\n\n')
