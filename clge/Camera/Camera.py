"""
@package docstring
Camera class -> ViewCamera
"""
class Camera:
    def __init__(self, xpos, ypos):
        self.x = xpos
        self.y = ypos

    def getPosition(self):
        return (self.x, self.y)

    def setPosition(self, xpos, ypos):
        self.x = xpos
        self.y = ypos

    def changePosition(self, xoffset, yoffset):
        self.x += xoffset
        self.y += yoffset
