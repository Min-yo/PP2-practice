import math
class Point:
    def __init__(self, coor_X = 0, coor_Y = 0):
        self.coor_X = coor_X
        self.coor_Y = coor_Y
    def show(self):
        print(str(self.coor_X) + " " + str(self.coor_Y))
    def move(self, new_coor_X, new_coor_Y):
        self.coor_X = new_coor_X
        self.coor_Y = new_coor_Y
    def dist(self, end_coor_X, end_coor_Y):
        print(math.sqrt((end_coor_X-self.coor_X)**2 + (end_coor_Y-self.coor_Y)**2))

p1 = Point()
p1.show()
p1.move(3, 4)
p1.show()
p1.dist(4, 3)