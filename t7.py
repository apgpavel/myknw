class CheckC:
    def __init__(self, xc, yc, zc):
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
        return self.zc

    def setZ(self, zc):
        self.zc = zc

    def __add__(self, other):
        return CheckC(self.xc + other.xc, self.yc + other.yc, self.zc + other.zc)

    def __sub__(self, other):
        return CheckC(self.xc - other.xc, self.yc - other.yc, self.zc - other.zc)

    def __mul__(self, other):
        return CheckC(self.xc * other.xc, self.yc * other.yc, self.zc * other.zc)

    def __truediv__(self, other):
        return CheckC(self.xc / other.xc, self.yc / other.yc, self.zc / other.zc)

    def __eq__(self, other):
        return self.zc == other.zc and self.yc == other.yc and self.xc == other.xc

    def printline(self):
        position = [self.xc, self.yc, self.zc]
        return list(map(lambda x: x * x, position))

test1 = CheckC(1, 2, 3)
test2 = CheckC(2, 4, 6)
test3 = test1 + test2
test4 = test1 * test1
print(test3.getX(), test3.getY(), test3.getZ())
print(test4.getX(), test4.getY(), test4.getZ())
print(test1.printline())
test1.setX(10)
print(test1.printline())
test5 = test1 * test1
print(test5.getX(), test5.getY(), test5.getZ())
