from .Component import Component
from .Transform2d import Transform2D


class AsciiRenderer2D(Component):
    character: str
    color: int

    def __init__(self):
        self.my_type = "asciirenderer2d"
        self.character = self.screen.default_symbol
        self.color = self.screen.default_color

    def editData(self, ncharacter=character, ncolor=color):
        self.character = ncharacter
        self.color = ncolor

    def Update(self):
        self.getPolygon()

    def getPolygon(self):
        transforminfo = self.transform2d.getFullInformation()
        self.screen.add_polygon(
            transforminfo["width"],
            transforminfo["height"],
            transforminfo["x"],
            transforminfo["y"],
            self.character,
            self.color
        )
