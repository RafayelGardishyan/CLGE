from clge.Behaviour.Vector3 import Vector3


class Transform3D:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.scale = [1, 1, 1]
        self.rotation = [0, 0, 0]
        self.offsetLastFrame = Vector3(0, 0, 0)
        self.blockMovement = {
            "up": False,
            "right": False,
            "down": False,
            "left": False
        }
        self.my_type = "transform3d"

    def changePositionBy(self, x, y, z):
        self.x += x
        self.y += y
        self.z += z

    def getPosition(self):
        return Vector3(self.x, self.y, self.z)

    def getSize(self):
        return self.scale

    def setSize(self, scale):
        self.scale = scale

    def getRotation(self):
        return self.scale

    def setRotation(self, scale):
        self.scale = scale

    def getFullInformation(self):
        return {
            "x": self.x,
            "y": self.y,
            "z": self.z,
            "rotation": self.rotation,
            "scale": self.scale,
            "vector3": Vector3(self.x, self.y, self.z)
        }
