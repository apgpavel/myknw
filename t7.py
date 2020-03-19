class CheckC(object):

    def __init__(self, xc=0, yc=0, zc=0):
        self.xc = xc
        self.yc = yc
        self.zc = zc

    """get & change X"""
    def getX(self):
        return self.xc

    def setX(self, xc):
        self.xc = xc

    """get & change Y"""
    def getY(self):
        return self.yc

    def setY(self, yc):
        self.yc = yc

    """get & change Z"""
    def getZ(self):
        return float(self.zc)

    def setZ(self, zc):
        self.zc = zc

    """change magic ang ariphmetic method"""
    def __add__(self, other):
        return self.xc + other.xc, self.yc + other.yc, self.zc + other.zc

    def __sub__(self, other):
        return self.xc - other.xc, self.yc - other.yc, self.zc - other.zc

    def __mul__(self, other):
        return self.xc * other.xc, self.yc * other.yc, self.zc * other.zc

    def __truediv__(self, other):
        return self.xc / other.xc, self.yc / other.yc, self.zc / other.zc

    def __eq__(self, other):
        return self.zc == other.zc and self.yc == other.yc and self.xc == other.xc

    def __neg__(self):
        return -self.xc, -self.yc, -self.zc

    def printline(self):
        position = [self.xc, self.yc, self.zc]
        return list(map(lambda x: x * x, position))

    def displayinfo(self):
        return self.xc, self.yc, self.zc

test1 = CheckC(1, 2, 3)
test2 = CheckC(2, 4, 6)

print(test1.displayinfo())
print(test2.displayinfo())
test3 = test1 + test2
test4 = test1 * test1
print(test3)
print(test4)
print(test1.getX())
print(test3[0], test3[1], test3[2])
print(test4[0], test4[1], test4[2])
print(-test2)
