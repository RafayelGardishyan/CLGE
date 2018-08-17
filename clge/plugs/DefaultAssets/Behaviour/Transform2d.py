from.Component import Component
from .Constants import *

class Transform2D(Component):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.my_type = "transform2d"

    def changePosition(self, action, x, y):
        if action == TRANSFORM2D_MV_POS:
            self.x += x
            self.y += y
        if action == TRANSFORM2D_SET_POS:
            self.x = x
            self.y = y

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
            "end_y": self.y + self.height
        }
