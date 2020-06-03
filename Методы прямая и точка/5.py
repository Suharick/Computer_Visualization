import math

class Point:
    def __str__(self):
        return "(%.2f, %.2f)"%(self.x, self.y)

    def distanceTo(self, point):
        return math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)

    def __init__(self, x, y):
        self.x = x
        self.y = y

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
        return Line(a, b, c)

    def distanceToZero(self):
        return abs(self.c)/math.sqrt(self.a**2 + self.b**2)

    def distanceToPoint(self, point):
        return abs(self.a*point.x + self.b*point.y + self.c)/math.sqrt(self.a**2 + self.b**2)
    
    def isParallel(self, line):
        return abs(self.a/self.b*(-1) - line.a/line.b*(-1)) < 0.0001

    def intersection(self, line):
        if abs( self.a/self.b*(-1) - line.a/line.b*(-1)) < 0.0001:
            return None
        else:
            self.q = (self.c*line.b - self.b*line.c)/(self.b*line.a - self.a*line.b)
            self.p = (-self.a*self.q - self.c)/self.b
            return "(%.2f, %.2f)"%(self.q, self.p)

    def nearPoint(self, point):
        self.k = self.b/self.a
        self.ost = point.y - self.k*point.x
        self.q = ((-1)*self.b*self.ost-self.c)/(self.a + self.b*self.k)
        self.p = self.k*self.q + self.ost
        return "(%.2f, %.2f)"%(self.q, self.p)

    def oneSide(self, point1, point2):
        return  (((point1.y >= point1.x*(-1)*self.a/self.b - self.c/self.b) and (point2.y >= point2.x*(-1)*self.a/self.b - self.c/self.b)) or ((point1.y <= point1.x*(-1)*self.a/self.b - self.c/self.b) and (point2.y <= point2.x*(-1)*self.a/self.b - self.c/self.b)))

    def normalize(self):
        if(self.c != 0):
            self.a = self.a/self.c
            self.b = self.b/self.c
            self.c = 1
            return str(Line(self.a,self.b,self.c))
        elif(self.a != 0):
            self.b = self.b/self.a
            self.a = 1
            return str(Line(self.a,self.b,self.c))
        else:
            self.b = 1
            return str(Line(self.a,self.b,self.c))

    def perpendicularLine(self, point):
        self.a = self.b/self.a
        self.c = point.y - self.a*point.x
        self.b = -1
        return str(Line(self.a,self.b,self.c))

    def parallelLine(self, point):
        self.c = - self.a * point.x - self.b * point.y
        return str(Line(self.a,self.b,self.c))

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

l = Line.fromCoord(-4.97,-7.93,-0.09,-1.52)
p = Point(-14.01,-10.61)

print(l.parallelLine(p))
