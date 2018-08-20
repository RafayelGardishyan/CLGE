from clge.Behaviour.Vector2 import Vector2
from clge.Constants import *


class Transform2D:
    def __init__(self):
        self.x: int
        self.y: int
        self.width: int
        self.height: int
        self.offsetLastFrame = Vector2(0, 0)
        self.blockMovement = {
            "up": False,
            "right": False,
            "down": False,
            "left": False
        }
        self.my_type = "transform2d"

    def customInit(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h

    def changePositionBy(self, action, x, y):
        pass_x = pass_y = False

        # Check if any movement is blocked
        if self.blockMovement["right"] and x > 0:
            pass_x = True
        if self.blockMovement["left"] and x < 0:
            pass_x = True
        if self.blockMovement["up"] and y < 0:
            pass_y = True
        if self.blockMovement['down'] and y > 0:
            pass_y = True

        previous = Vector2(x, y)

        # Perform Movement
        if action == TRANSFORM2D_MV_POS:
            if not pass_x:
                self.x += x
            if not pass_y:
                self.y += y

        self.offsetLastFrame = Vector2(Vector2(self.x, self.y) - previous)

        self.blockMovement["up"] = False
        self.blockMovement["down"] = False
        self.blockMovement["right"] = False
        self.blockMovement["left"] = False

    def getPosition(self):
        return Vector2(self.x, self.y)

    def getSize(self):
        return self.width, self.height

    def setSize(self, width, height):
        self.width = width
        self.height = height

    def PreUpdate(self):
        self.offsetLastFrame = Vector2(0, 0)

    def getFullInformation(self):
        return {
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height,
            "end_x": self.x + self.width,
            "end_y": self.y + self.height,
            "vector2": {
                "start": Vector2(self.x, self.y),
                "end": Vector2(self.x + self.width, self.y + self.height,)
            }
        }
