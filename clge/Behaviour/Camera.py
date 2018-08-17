from clge.Constants import *
from .Behaviour import Behaviour


class Camera(Behaviour):
    def getPosition(self):
        return self.getComponentByType("tranfsorm2d").x, self.getComponentByType("tranfsorm2d").y

    def setPosition(self, xpos, ypos):
        self.getComponentByType("transform2d").changePosition(TRANSFORM2D_SET_POS, xpos, ypos)

    def changePosition(self, xoffset, yoffset):
        self.getComponentByType("transform2d").changePosition(TRANSFORM2D_MV_POS, xoffset, yoffset)
