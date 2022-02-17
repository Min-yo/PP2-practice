class Shape:
    def __init__(self, area = 0):
        self.area = area
    def Area(self):
        print(str(self.area))

class Square(Shape):
    def __init__(self, length, area = 0):
        self.length = length
        self.area = length**2

p1 = Shape()
p1.Area()
p2 = Square(5)
p2.Area()



