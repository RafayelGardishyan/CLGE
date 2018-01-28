from engine import Screen, KeyDetector

screenObj = Screen(60, 20, auto_clear_objects_list=True, auto_timeout=True, timeout=0.05)

class Player:
    xpos = 0
    ypos = 19
    speed = 1
    power = 0
    name = 'UnnamedPlayer'

    def __init__(self, x, y, speed, power, name):
        self.xpos = x
        self.ypos = y
        self.speed = speed
        self.power = power
        self.name = name

    bufferx = xpos
    buffery = ypos

    up = True

    def jump(self):
        if self.ypos > self.buffery - (5 * self.speed) and self.up is True:
            self.ypos -= self.speed
        elif self.ypos < self.buffery:
            self.up = False
            self.ypos += self.speed
        else:
            self.up = True

    def right(self):
        self.xpos += self.speed
        self.bufferx = self.xpos

    def left(self):
        self.xpos -= self.speed
        self.bufferx = self.xpos

    def down(self):
        self.ypos = self.buffery
        self.buffery = self.ypos

    def check_collision(self, player, screen):
        if self.xpos == player.xpos and self.ypos == player.ypos:
            if self.power < player.power:
                self.xpos = screen.field_width + 100
                self.ypos = screen.field_height + 100
            elif self.power > player.power:
                player.xpos = screen.field_width + 100
                player.ypos = screen.field_height + 100
            else:
                pass

    def __str__(self):
        return self.name

p = Player(0, 19, 2, 1, "At")
g = Player(59, 19, 1, 5, "Star")
pup = KeyDetector("w")
pdown = KeyDetector("s")
pleft = KeyDetector("a")
pright = KeyDetector("d")
gup = KeyDetector("up")
gdown = KeyDetector("down")
gleft = KeyDetector("left")
gright = KeyDetector("right")
help = KeyDetector("h")


while True:
    if help.detect():
        screenObj.timeout = 1
        screenObj.add_object(2, 2, "H")
        screenObj.add_object(3, 2, "E")
        screenObj.add_object(4, 2, "L")
        screenObj.add_object(5, 2, "P")
        screenObj.add_object(7, 2, "T")
        screenObj.add_object(8, 2, "E")
        screenObj.add_object(9, 2, "X")
        screenObj.add_object(3, 4, "W")
        screenObj.add_object(3, 5, "S")
        screenObj.add_object(2, 5, "A")
        screenObj.add_object(4, 5, "D")
        screenObj.add_object(10, 5, "<")
        screenObj.add_object(12, 5, ">")
        screenObj.add_object(11, 4, "^")
        screenObj.add_object(11, 5, ".")
        screenObj.add_object(2, 6, "a")
        screenObj.add_object(3, 6, "t")
        screenObj.add_object(10, 6, "s")
        screenObj.add_object(11, 6, "t")
        screenObj.add_object(12, 6, "a")
        screenObj.add_object(13, 6, "r")
        screenObj.add_object(10, 2, "T")

        screenObj.render()
        screenObj.clear_screen()
        screenObj.timeout = 0.05
    if pup.detect():
        for i in range(11):
            p.jump()
            if pdown.detect():
                p.down()
                break
            if gdown.detect():
                g.down()
            if pleft.detect():
                p.left()
            if pright.detect():
                p.right()
            if gleft.detect():
                g.left()
            if gright.detect():
                g.right()
            screenObj.add_object(p.xpos, p.ypos, '@')
            screenObj.add_object(g.xpos, g.ypos, '*')
            screenObj.render()
            screenObj.clear_screen()
    if pdown.detect():
        p.down()
    if pleft.detect():
        p.left()
    if pright.detect():
        p.right()
    if gup.detect():
        for i in range(11):
            g.jump()
            if gdown.detect():
                g.down()
                break
            if pdown.detect():
                p.down()
            if pleft.detect():
                p.left()
            if pright.detect():
                p.right()
            if gleft.detect():
                g.left()
            if gright.detect():
                g.right()
            screenObj.add_object(p.xpos, p.ypos, '@')
            screenObj.add_object(g.xpos, g.ypos, '*')
            screenObj.render()
            screenObj.clear_screen()
    if gleft.detect():
        g.left()
    if gdown.detect():
        g.down()
    if gright.detect():
        g.right()
    p.check_collision(g, screenObj)
    screenObj.add_object(p.xpos, p.ypos, '@')
    screenObj.add_object(g.xpos, g.ypos, '*')
    screenObj.render()
    screenObj.clear_screen()

