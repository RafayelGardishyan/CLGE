from engine import Screen, KeyDetector, setup

screenObj = Screen(60, 20, auto_clear_objects_list=True, auto_timeout=True, timeout=0.05)
bullets = []

class Player:
    xpos = 0
    ypos = 19
    speed = 1
    power = 0
    name = 'UnnamedPlayer'
    direction = None
    alive = True

    def __init__(self, x, y, speed, power, name, start_direction):
        self.xpos = x
        self.ypos = y
        self.speed = speed
        self.power = power
        self.name = name
        self.direction = start_direction

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
        self.direction = "right"

    def left(self):
        self.xpos -= self.speed
        self.bufferx = self.xpos
        self.direction = "left"

    def shoot(self):
        bullets.append([self.xpos, self.ypos, self.direction, self.name])

    def down(self):
        self.ypos = self.buffery
        self.buffery = self.ypos

    def check_collision(self, player, screen):
        for bullet in bullets:
            if bullet[0] == self.xpos and bullet[1] == self.ypos and bullet[3] != self.name:
                self.xpos = screen.field_width + 100
                self.ypos = screen.field_height + 100
                bullet = None
                self.alive = False
            else:
                pass

        if self.xpos == player.xpos and self.ypos == player.ypos:
            if self.power < player.power:
                self.xpos = screen.field_width + 100
                self.ypos = screen.field_height + 100
                self.alive = False
            elif self.power > player.power:
                player.xpos = screen.field_width + 100
                player.ypos = screen.field_height + 100
                player.alive = False
            else:
                pass

    def __str__(self):
        return self.name

p = Player(0, 19, 2, 1, "At", "right")
g = Player(59, 19, 1, 5, "Star", "left")
pup = KeyDetector("w")
pdown = KeyDetector("s")
pleft = KeyDetector("a")
pright = KeyDetector("d")
pshoot = KeyDetector("z")
gup = KeyDetector("up")
gdown = KeyDetector("down")
gleft = KeyDetector("left")
gright = KeyDetector("right")
gshoot = KeyDetector("l")
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
        screenObj.add_object(6, 5, "Z")
        screenObj.add_object(10, 5, "<")
        screenObj.add_object(12, 5, ">")
        screenObj.add_object(11, 4, "^")
        screenObj.add_object(11, 5, ".")
        screenObj.add_object(14, 5, "L")
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
    if pshoot.detect() and p.alive:
        p.shoot()
    if gshoot.detect() and p.alive:
        g.shoot()
    if pup.detect() and p.alive:
        for i in range(11):
            p.jump()
            if pshoot.detect() and p.alive:
                p.shoot()
            if gshoot.detect() and g.alive:
                g.shoot()
            if pdown.detect() and p.alive:
                p.down()
                break
            if gdown.detect() and g.alive:
                g.down()
            if pleft.detect() and p.alive:
                p.left()
            if pright.detect() and p.alive:
                p.right()
            if gleft.detect() and g.alive:
                g.left()
            if gright.detect() and g.alive:
                g.right()
            for bullet in bullets:
                try:
                    if bullet[2] == "right":
                        bullet[0] += 1
                    elif bullet[2] == "left":
                        bullet[0] -= 1
                    screenObj.add_object(bullet[0], bullet[1], "O")
                    if bullet[0] < 0 or bullet[0] > screenObj.field_width:
                        bullet = None
                except:
                    pass
            p.check_collision(g, screenObj)
            g.check_collision(p, screenObj)
            screenObj.add_object(p.xpos, p.ypos, '@')
            screenObj.add_object(g.xpos, g.ypos, '*')
            screenObj.render()
            screenObj.clear_screen()
    if pdown.detect() and p.alive:
        p.down()
    if pleft.detect() and p.alive:
        p.left()
    if pright.detect() and p.alive:
        p.right()
    if gup.detect() and g.alive:
        for i in range(11):
            g.jump()
            if pshoot.detect() and p.alive:
                p.shoot()
            if gshoot.detect() and g.alive:
                g.shoot()
            if gdown.detect() and g.alive:
                g.down()
                break
            if pdown.detect() and p.alive:
                p.down()
            if pleft.detect() and p.alive:
                p.left()
            if pright.detect() and p.alive:
                p.right()
            if gleft.detect() and g.alive:
                g.left()
            if gright.detect() and g.alive:
                g.right()
            for bullet in bullets:
                try:
                    if bullet[2] == "right":
                        bullet[0] += 1
                    elif bullet[2] == "left":
                        bullet[0] -= 1
                    screenObj.add_object(bullet[0], bullet[1], "O")
                    if bullet[0] < 0 or bullet[0] > screenObj.field_width:
                        bullet = None
                except:
                    pass
            p.check_collision(g, screenObj)
            g.check_collision(p, screenObj)
            screenObj.add_object(p.xpos, p.ypos, '@')
            screenObj.add_object(g.xpos, g.ypos, '*')
            screenObj.render()
            screenObj.clear_screen()
    if gleft.detect() and g.alive:
        g.left()
    if gdown.detect() and g.alive:
        g.down()
    if gright.detect() and g.alive:
        g.right()
    p.check_collision(g, screenObj)
    g.check_collision(p, screenObj)
    for bullet in bullets:
        try:
            if bullet[2] == "right":
                bullet[0] += 1
            elif bullet[2] == "left":
                bullet[0] -= 1
            screenObj.add_object(bullet[0], bullet[1], "O")
            if bullet[0] < 0 or bullet[0] > screenObj.field_width:
                bullet = None
        except:
            pass


    screenObj.add_object(p.xpos, p.ypos, '@')
    screenObj.add_object(g.xpos, g.ypos, '*')
    screenObj.render()
    screenObj.clear_screen()

