from clge import KeymapGenerator
from clge.Behaviour import Vector2
from clge.Constants import TRANSFORM2D_MV_POS


class PlayerController:
    def __init__(self):
        self.keymap = None
        self.my_type = "std.playercontroller"

    def Start(self):
        kg = KeymapGenerator()

        kg.add("up", 'up')
        kg.add("down", 'down')
        kg.add("right", 'right')
        kg.add("left", 'left')

        self.keymap = kg.generate()

    def Update(self):
        vector = Vector2(0, 0)
        if self.keymap["up"].detect():
            vector.y += -4
        if self.keymap["down"].detect():
            vector.y += 4
        if self.keymap["left"].detect():
            vector.x += -4
        if self.keymap["right"].detect():
            vector.x += 4

        self.transform2d.changePositionBy(
            TRANSFORM2D_MV_POS,
            vector.x * self.screen.deltaTime,
            vector.y * self.screen.deltaTime
        )
