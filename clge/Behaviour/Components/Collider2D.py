from clge.Behaviour import Behaviour


class Collider2D:
    def __init__(self):
        self.layer = 0
        self.isTrigger = False
        self.my_type = "collider2d"
        self.coordinates = []
        self.coordinatesForOthers = []
        self.collided = []

    def onCollisionEnter2D(self, col):
        pass

    def onTriggerEnter2D(self, col):
        pass

    def updatePosition(self):
        location = self.transform2d.getFullInformation()
        self.x = round(location["x"])
        self.x2 = round(location["end_x"])
        self.y = round(location["y"])
        self.y2 = round(location["end_y"])
        self.setCoordinates()

    def getCollidedBehaviours(self):
        return self.collided

    def setCoordinates(self):
        self.coordinates = []
        self.coordinatesForOthers = []
        for i in range(self.x - 1, self.x2 + 1):
            for j in range(self.y - 1, self.y2 + 1):
                if (j == self.y - 1 or j == self.y2 + 1) and (i == self.x - 1 or i == self.x2 + 1):
                    continue
                self.coordinates.append((i, j))

        for i in range(self.x, self.x2):
            for j in range(self.y, self.y2):
                self.coordinatesForOthers.append((i, j))

    def getCoordinates(self):
        return self.coordinatesForOthers

    def changeLayer(self, layer):
        self.layer = layer

    def setIsTrigger(self, isTrigger):
        self.isTrigger = isTrigger

    def checkCollision(self, other: Behaviour):
        otherCollider = other.getComponentByType("collider2d")

        if otherCollider == self:
            return False

        otherTransform = other.getComponentByType("transform2d")
        otherObjectCoordinates = otherCollider.getCoordinates()
        for i in self.coordinates:
            for j in otherObjectCoordinates:

                # Collision is detected
                if i == j and otherCollider.layer == self.layer:

                    self.collided.append(other)

                    if not self.isTrigger:
                        self.onCollisionEnter2D(other)
                        # Check Y
                        if self.y < otherTransform.y:
                            otherTransform.blockMovement["down"] = True
                        elif self.y2 > otherTransform.getFullInformation()["end_y"]:
                            otherTransform.blockMovement["up"] = True

                        # Check X
                        if self.x > otherTransform.x:
                            otherTransform.blockMovement["left"] = True
                        elif self.x2 < otherTransform.getFullInformation()["end_x"]:
                            otherTransform.blockMovement["right"] = True
                    else:
                        self.onTriggerEnter2D(other)

                    return True

        # If no collision is detected return False
        return False

    def PreUpdate(self):
        self.updatePosition()
        self.setCoordinates()
        self.collided = []
        for obj in self.world.children:
            if obj.getComponentByType("collider2d"):
                self.checkCollision(obj)
