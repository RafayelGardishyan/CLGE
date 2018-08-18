from clge.Behaviour import Vector2
from clge.Constants import *
from .Component import Component


class Transform2D(Component):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.blockMovement = {
            "up": False,
            "right": False,
            "down": False,
            "left": False
        }
        self.my_type = "transform2d"

    def changePositionBy(self, action, x, y):
        pass_x = pass_y = False

        # Check if any movement is blocked
        if self.blockMovement["up"] and x < self.x:
            pass_x = True
        if self.blockMovement["down"] and x > self.x:
            pass_x = True
        if self.blockMovement["right"] and y > self.y:
            pass_y = True
        if self.blockMovement['left'] and y < self.y:
            pass_y = True

        # Perform Movement
        if action == TRANSFORM2D_MV_POS:
            if not pass_x:
                self.x += x
            if not pass_y:
                self.y += y

        # Temporally Functionality. Will be removed later
        if action == TRANSFORM2D_SET_POS:
            self.x = x
            self.y = y

        self.blockMovement = False

    def getPosition(self):
        return self.x, self.y

    def getSize(self):
        return self.width, self.height

    def setSize(self, width, height):
        self.width = width
        self.height = height

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
