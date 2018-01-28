from engine import Screen

screenObj = Screen(40, 20, auto_clear_objects_list=True, auto_timeout=True, timeout=0.05)

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

p = Player(9, 19, 2, 1, "At")
g = Player(10, 19, 1, 5, "Star")
text = "Welcome to CLGE Testing Sandbox"

while True:
    p.check_collision(g, screenObj)
    screenObj.add_object(p.xpos, p.ypos, '@')
    screenObj.add_object(g.xpos, g.ypos, '*')
    screenObj.render()
    if text:
        print(text)
        text = False
    c = input("Command: ")
    c = c.split()
    for command in c:
        if command == "jump":
            for i in range(11):
                screenObj.clear_screen()
                screenObj.add_object(p.xpos, p.ypos, '@')
                screenObj.add_object(g.xpos, g.ypos, '*')
                p.jump()
                g.jump()
                screenObj.render()
                text = "{} and {} were jumping".format(p, g)
                print(text)
        elif command == "jumpp":
            for i in range(11):
                screenObj.clear_screen()
                screenObj.add_object(p.xpos, p.ypos, '@')
                screenObj.add_object(g.xpos, g.ypos, '*')
                text = "{} was jumping".format(p)
                p.jump()
                screenObj.render()
                print(text)
        elif command == "jumpg":
            for i in range(11):
                screenObj.clear_screen()
                screenObj.add_object(g.xpos, g.ypos, '*')
                screenObj.add_object(p.xpos, p.ypos, '@')
                text = "{} was jumping".format(g)
                g.jump()
                screenObj.render()
                print(text)
        elif command == "right":
            p.right()
            g.right()
            text = "{} and {} are moving to right".format(p, g)
        elif command == "left":
            p.left()
            g.left()
            text = "{} and {} are moving to left".format(p, g)
        elif command == "rightp":
            p.right()
            text = "{} is moving to right".format(p)
        elif command == "leftp":
            p.left()
            text = "{} is moving to left".format(p)
        elif command == "rightg":
            g.right()
            text = "{} is moving to right".format(g)
        elif command == "leftg":
            g.left()
            text = "{} is moving to left".format(g)
        elif command == "quit":
            raise SystemExit
        elif command == "help":
            text = "Help text:\nCommands:\n\t{}:\n\t\tjumpp = JUMP\n\t\trightp or leftp = GO LEFT OR GO RIGHT\n\t{}:\n\t\tjumpg = JUMP\n\t\trightg or leftg = Go LEFT OR GO RIGHT".format(p, g)
        else:
            text = "For help input \"help\""

    screenObj.clear_screen()

