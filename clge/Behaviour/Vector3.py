class Vector3:
    def __init__(self, *args):
        if len(args) == 1:
            self.x = float(args[0].x)
            self.y = float(args[0].y)
            self.z = float(args[0].z)
        else:
            self.x = float(args[0])
            self.y = float(args[1])
            self.z = float(args[2])

    def __add__(self, other):
        totalx = self.x + float(other.x)
        totaly = self.y + float(other.y)
        totalz = self.z + float(other.z)
        return Vector3(totalx, totaly, totalz)

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __sub__(self, other):
        totalx = self.x - float(other.x)
        totaly = self.y - float(other.y)
        totalz = self.z - float(other.z)
        return Vector3(totalx, totaly, totalz)

    def __rsub__(self, other):
        if other == 0:
            return self
        else:
            return self.__sub__(other)

    def __mul__(self, other):
        totalx = self.x * float(other.x)
        totaly = self.y * float(other.y)
        totalz = self.z * float(other.z)
        return Vector3(totalx, totaly, totalz)

    def __rmul__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __div__(self, other):
        totalx = self.x / float(other.x)
        totaly = self.y / float(other.y)
        totalz = self.z / float(other.z)
        return Vector3(totalx, totaly, totalz)

    def __rdiv__(self, other):
        if other == 0:
            return self
        else:
            return self.__sub__(other)

    def __getitem__(self, key):
        if key == "x" or 0:
            return self.x
        elif key == "y" or 1:
            return self.y
        elif key == "z" or 2:
            return self.z

    def __setitem__(self, key, value):
        if key == "x" or 0:
            self.x = value
        elif key == "y" or 1:
            self.y = value
        elif key == "z" or 2:
            self.z = value
