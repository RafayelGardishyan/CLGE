class AsciiRenderer2D:
    character = ""
    color = 12

    def __init__(self):
        self.my_type = "asciirenderer2d"

    def editData(self, ncharacter=character, ncolor=color):
        self.character = ncharacter
        self.color = ncolor

    def Update(self):
        self.character = self.screen.default_symbol
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
