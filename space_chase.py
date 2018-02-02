from engine import Screen, generate_keymap
import random

scr = Screen(80, 40, timeout=.1, auto_clear_objects_list=True)


class SpaceStone:

    def __init__(self, xpos, ypos, speed):
        self.speed = speed
        self.ypos = ypos
        self.xpos = xpos

    def move(self):
        self.xpos -= self.speed

    def return_to_0x(self):
        if self.xpos == -1:
            self.xpos = scr.field_width - 1
            self.speed = random.randint(1, 9)
            self.ypos = random.randint(0, scr.field_height - 1)

class SpaceShip:

    def __init__(self, ypos, lives):
        self.lives = lives
        self.ypos = ypos

    keys = generate_keymap({
        'up': 'w',
        'up_a': 'up',
        'down': 's',
        'down_a': 'down',
    })

    def up(self):
        self.ypos -= 1

    def down(self):
        self.ypos += 1

    def detect_key_press(self):
        if self.keys['up'].detect() or self.keys['up_a'].detect():
            self.up()
        if self.keys['down'].detect() or self.keys['down_a'].detect():
            self.down()

    def check_collision(self, space_stone):
        if self.ypos == space_stone.ypos and space_stone.xpos == 0:
            self.lives -= 1
            return True
        else:
            return False

player = SpaceShip(int(scr.field_height/2), 5)
stones = []
for i in range(10):
    stones.append(SpaceStone(scr.field_width - 1, random.randint(0, scr.field_height - 1), random.randint(1, 9)))

while True:
    player.detect_key_press()
    scr.add_object(0, player.ypos, ">")
    for stone in stones:
        player.check_collision(stone)
        scr.add_object(stone.xpos, stone.ypos, "@")
    scr.add_object((scr.field_width - 1 - 8), 0, "L")
    scr.add_object((scr.field_width - 1 - 7), 0, "I")
    scr.add_object((scr.field_width - 1 - 6), 0, "V")
    scr.add_object((scr.field_width - 1 - 5), 0, "E")
    scr.add_object((scr.field_width - 1 - 4), 0, "S")
    scr.add_object((scr.field_width - 1 - 3), 0, ":")
    scr.add_object((scr.field_width - 1 - 1), 0, str(player.lives))
    scr.render()
    scr.clear_screen()
    for stone in stones:
        stone.move()
        stone.return_to_0x()
