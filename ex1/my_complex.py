class MyComplex:

    def __init__(self, realpart=0, imagpart=0):
         self.r = realpart
         self.i = imagpart

    def __add__(self, other):
        return MyComplex(self.r + other.r, self.i + other.i)

    def __sub__(self, other):
        return MyComplex(self.r - other.r, self.i - other.i)

    def __eq__(self, other):
        return self.r == other.r and self.i == other.i

    def addSub(self, other):
        return (self + other, self - other)

    def __str__(self):
        return "{}*i + {}".format(self.i, self.r)

