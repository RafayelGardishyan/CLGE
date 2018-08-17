from clge.plugs.DefaultAssets.Behaviour import Behaviour
from .Component import Component


class Collider2D(Component):
    def __init__(self, *args):
        if len(args) == 4:
            self.x = args[0]
            self.x2 = args[1]
            self.y = args[2]
            self.y2 = args[3]
        else:
            location = args[0].getFullInformation()
            self.x = location["x"]
            self.y = location["y"]
            self.x2 = location["end_x"]
            self.y2 = location["end_y"]

        self.layer = 0
        self.my_type = "collider2d"
        self.coordinates = []
        self.setCoordinates()

    def updatePosition(self, begin_x, begin_y, end_x, end_y):
        self.x = begin_x
        self.x2 = end_x
        self.y = begin_y
        self.y2 = end_y
        self.setCoordinates()

    def setCoordinates(self):
        for i in range(self.x - 1, self.x2 + 2):
            for j in range(self.y - 1, self.y2 + 2):
                if (j == self.y - 1 or j == self.y2 - 1) and (i == self.x - 1 or i == self.x2 - 1):
                    continue
                self.coordinates.append((i, j))

    def getCoordinates(self):
        return self.coordinates

    def changeLayer(self, layer):
        self.layer = layer

    def checkCollision(self, other: Behaviour):
        otherCollider = other.getComponent("collider2d")
        otherObjectCoordinates = otherCollider.getCoordinates()
        for i in self.coordinates:
            for j in otherObjectCoordinates:
                if i == j and otherCollider.layer == self.layer:
                    return True
        return False