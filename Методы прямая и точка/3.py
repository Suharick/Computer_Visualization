import math

class Line:
    def __str__(self):
        s1 = "-%.2fx "%(abs(self.a)) if self.a<0 else "%.2fx "%(abs(self.a))
        s2 = "- %.2fy "%(abs(self.b)) if self.b<0 else "+ %.2fy "%(abs(self.b))
        s3 = "- %.2f = 0"%(abs(self.c)) if self.c<0 else "+ %.2f = 0"%(abs(self.c))
        return s1 + s2 + s3
    
    @staticmethod
    def fromCoord(x1, y1, x2, y2):
        a = y1 - y2
        b = x2 - x1
        c = x1*y2 - x2*y1
        return str(Line(a, b, c))

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
