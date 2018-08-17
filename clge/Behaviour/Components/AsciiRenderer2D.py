from .Component import Component
from .Transform2d import Transform2D

class AsciiRenderer2D(Component):
    transform2d: Transform2D
    character: str
    color: int

    def __init__(self, transform2d, character, color):
        self.transform2d = transform2d
        self.character = character
        self.color = color
        self.my_type = "asciirenderer2d"

    def editData(self, ntransform2d=transform2d, ncharacter=character, ncolor=color):
        self.transform2d = ntransform2d
        self.character = ncharacter
        self.color = ncolor

    def getPolygon(self, screen):
        transforminfo = self.transform2d.getFullInformation()
        screen.add_polygon(
            transforminfo["width"],
            transforminfo["height"],
            transforminfo["x"],
            transforminfo["y"],
            self.character,
            self.color
        )
