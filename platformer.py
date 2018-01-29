from engine import Screen, generate_keymap

scr = Screen(60, 30, timeout=0.05, auto_clear_objects_list=True)


class Tile:
    xpos = 0
    ypos = 0

    def __init__(self, x, y):
        self.xpos = x
        self.ypos = y


class Player:
    xpos = 0
    ypos = 0
    up = True
    ground = True
    dir = "right"
    power = 1
    keys = generate_keymap({
        'down': 's',
        'down_arrow': 'down',
        'right': 'd',
        'right_arrow': 'right',
        'left': 'a',
        'left_arrow': 'left',
        'up': 'w',
        'up_arrow': 'up',
    })

    def __init__(self, x, y, direction, power):
        self.xpos = x
        self.ypos = y
        self.bufferx = self.xpos
        self.buffery = self.ypos
        self.dir = direction
        self.power = power

    def jump(self):
        if self.ypos > self.buffery - (5 * self.power) and self.up:
            self.ypos -= self.power
        elif self.ypos < self.buffery:
            self.up = False
            self.ypos += self.power
        else:
            self.up = True

    def right(self, steps):
        self.xpos += steps
        self.bufferx = self.xpos
        self.dir = "right"

    def left(self, steps):
        self.xpos -= steps
        self.bufferx = self.xpos
        self.dir = "left"

    def down(self):
        self.ypos = self.buffery

    def gravity(self, xpos, ypos):
        if self.xpos == xpos and self.ypos == ypos:
            self.buffery = self.ypos
            self.ground = True
        elif self.ypos == scr.field_height - 1:
            self.ground = True
        else:
            self.ground = False

    def grativy_move(self):
        if not self.ground:
            self.ypos += 1
        else:
            pass

tiles = [
    Tile(5, 28),
    Tile(6, 28),
    Tile(7, 28),
    Tile(8, 28),
    Tile(9, 28),
    Tile(10, 28),
]

player = Player(0, (scr.field_height - 1), 'right', 1)

while True:
    for tile in tiles:
        player.gravity(tile.xpos, tile.ypos)
        #player.grativy_move()

    if player.keys['up'].detect() or player.keys['up_arrow'].detect():

        for i in range(11):

            for tile in tiles:
                player.gravity(tile.xpos, tile.ypos)

            player.jump()
            scr.add_object(player.xpos, player.ypos, "@")

            for tile in tiles:
                scr.add_object(tile.xpos, tile.ypos)

            scr.render()
            scr.clear_screen()
            # for tile in tiles:
            #     player.check_tile_collision(tile)
            if player.keys['down'].detect() or player.keys['down_arrow'].detect():
                player.down()
                break

            if player.keys['right'].detect() or player.keys['right_arrow'].detect():
                player.right(1)

            if player.keys['left'].detect() or player.keys['left_arrow'].detect():
                player.left(1)

    if player.keys['down'].detect() or player.keys['down_arrow'].detect():
        player.down()

    if player.keys['right'].detect() or player.keys['right_arrow'].detect():
        player.right(1)

    if player.keys['left'].detect() or player.keys['left_arrow'].detect():
        player.left(1)

    for tile in tiles:
        scr.add_object(tile.xpos, tile.ypos)

    scr.add_object(player.xpos, player.ypos, "@")
    scr.render()
    scr.clear_screen()
