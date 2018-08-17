from .Behaviour import Behaviour

class Camera(Behaviour):
    def __init__(self, xpos, ypos):
        self.x = self.getComponent("tranfsorm2d").x
        self.y = self.getComponent("tranfsorm2d").y

    def getPosition(self):
        return (self.x, self.y)

    def setPosition(self, xpos, ypos):
        self.x = xpos
        self.y = ypos

    def changePosition(self, xoffset, yoffset):
        self.x += xoffset
        self.y += yoffset
