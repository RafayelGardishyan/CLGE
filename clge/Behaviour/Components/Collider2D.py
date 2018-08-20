from clge.Behaviour import Behaviour


class Collider2D:
    def __init__(self):
        self.layer = 0
        self.isTrigger = False
        self.my_type = "collider2d"
        self.coordinates = {}
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
        self.coordinates = {
            "top": [],
            "bottom": [],
            "right": [],
            "left": []
        }
        self.coordinatesForOthers = []
        # Set the Border Coordinates
        for i in range(self.x, self.x2):
            self.coordinates["top"].append((i, self.y - 1))
            self.coordinates["bottom"].append((i, self.y2))
        for i in range(self.y, self.y2):
            self.coordinates["right"].append((self.x2, i))
            self.coordinates["left"].append((self.x - 1, i))

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

        freturn = False

        if otherCollider == self:
            return False

        otherTransform = other.getComponentByType("transform2d")
        otherObjectCoordinates = otherCollider.getCoordinates()

        for otherCoordinate in otherObjectCoordinates:
            if otherCoordinate in self.coordinates["top"]:
                otherTransform.blockMovement["down"] = True
                self.transform2d.blockMovement["up"] = True
                freturn = True
            if otherCoordinate in self.coordinates["bottom"]:
                otherTransform.blockMovement["up"] = True
                self.transform2d.blockMovement["down"] = True
                freturn = True
            if otherCoordinate in self.coordinates["right"]:
                otherTransform.blockMovement["left"] = True
                self.transform2d.blockMovement["right"] = True
                freturn = True
            if otherCoordinate in self.coordinates["left"]:
                otherTransform.blockMovement["right"] = True
                self.transform2d.blockMovement["left"] = True
                freturn = True

        return freturn

    def FixedUpdate(self):
        self.updatePosition()
        self.setCoordinates()

        self.collided = []
        for obj in self.world.children:
            if obj.getComponentByType("collider2d"):
                self.checkCollision(obj)
