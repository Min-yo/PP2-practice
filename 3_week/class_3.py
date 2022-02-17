class Shape:
    def __init__(self, area = 0):
        self.area = area
    def area(self):
        print(self.area)
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def printArea(self):
        print(self.length*self.width)

p1 = Rectangle(5, 4)
p1.printArea()
