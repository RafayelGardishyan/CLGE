from clge.Behaviour import Behaviour
from .Component import Component
import gc

class Collider2D(Component):
    def __init__(self):
        self.layer = 0
        self.isTrigger = False
        self.my_type = "collider2d"
        self.coordinates = []
        self.collided = []
        self.setCoordinates()

    def updatePosition(self):
        location = self.transform2d.getFullInformation()
        self.x = location["x"]
        self.x2 = location["end_x"]
        self.y = location["y"]
        self.y2 = location["end_y"]
        self.setCoordinates()

    def customInit(self, **kwargs):
        self.layer = kwargs["layer"]
        self.updatePosition()

    def getCollidedBehaviours(self):
        return self.collided

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

    def setIsTrigger(self, isTrigger):
        self.isTrigger = isTrigger

    def checkCollision(self, other: Behaviour):
        otherCollider = other.getComponentByType("collider2d")
        otherTransform = other.getComponentByType("transform2d")
        otherObjectCoordinates = otherCollider.getCoordinates()
        for i in self.coordinates:
            for j in otherObjectCoordinates:

                # Collision is detected
                if i == j and otherCollider.layer == self.layer:

                    self.collided.append(other)

                    if self.isTrigger:
                        # Check X
                        if self.x < otherTransform.x:
                            otherTransform.blockMovement["down"] = True
                        elif self.x2 > otherTransform.getFullInformation()["end_x"]:
                            otherTransform.blockMovement["up"] = True

                        # Check Y
                        if self.y < otherTransform.y:
                            otherTransform.blockMovement["left"] = True
                        elif self.y2 > otherTransform.getFullInformation()["end_y"]:
                            otherTransform.blockMovement["right"] = True
                    return True

        # If no collision is detected return False
        return False

    def PreUpdate(self):
        self.collided = []
        for obj in gc.get_objects():
            if isinstance(obj, Behaviour):
                self.checkCollision(Behaviour)
