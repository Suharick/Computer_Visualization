import math

class Point:
    def __str__(self):
        return "[%.2f, %.2f]"%(self.x, self.y)

    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(2,6.554)
print(str(p))
