class Vector2:
    def __init__(self, *args):
        if len(args) == 1:
            self.x = float(args[0].x)
            self.y = float(args[0].y)
        else:
            self.x = float(args[0])
            self.y = float(args[1])

    def __add__(self, other):
        totalx = self.x + float(other.x)
        totaly = self.y + float(other.y)
        return Vector2(totalx, totaly)

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __sub__(self, other):
        totalx = self.x - float(other.x)
        totaly = self.y - float(other.y)
        return Vector2(totalx, totaly)

    def __rsub__(self, other):
        if other == 0:
            return self
        else:
            return self.__sub__(other)

    def __getitem__(self, key):
        if key == "x" or 0:
            return self.x
        elif key == "y" or 1:
            return self.y
