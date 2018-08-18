class Vector2:
    def __init__(self, *args):
        if len(args) == 1:
            self.x = args[0].x
            self.y = args[0].y
        else:
            self.x = args[0]
            self.y = args[1]

    def __add__(self, other):
        totalx = self.x + other.x
        totaly = self.y + other.y
        return Vector2(totalx, totaly)

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)
