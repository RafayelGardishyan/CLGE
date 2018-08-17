from .Component import Component

class AsciiRenderer2D(Component):
    def __init__(self, transform2d, character, color, screen):
        self.transform2d = transform2d
        self.character = character
        self.color = color
        self.screen = screen
        self.my_type = "asciirenderer2d"
        transforminfo = transform2d.getFullInformation()
        screen.add_polygon(
            transforminfo["width"],
            transforminfo["height"],
            transforminfo["x"],
            transforminfo["y"],
            character,
            color
        )

    def updateData(self):
        transforminfo = self.transform2d.getFullInformation()
        self.screen.add_polygon(
            transforminfo["width"],
            transforminfo["height"],
            transforminfo["x"],
            transforminfo["y"],
            self.character,
            self.color
        )
