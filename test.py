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
            else:
                player.xpos = screen.field_width + 100
                player.ypos = screen.field_height + 100

    def __str__(self):
        return self.name

p = Player(0, 19, 2, 1, "At")
g = Player(10, 19, 1, 5, "Star")
text = False

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
        elif command == "jumpp":
            for i in range(11):
                screenObj.clear_screen()
                screenObj.add_object(p.xpos, p.ypos, '@')
                screenObj.add_object(g.xpos, g.ypos, '*')
                p.jump()
                screenObj.render()
        elif command == "jumpg":
            for i in range(11):
                screenObj.clear_screen()
                screenObj.add_object(g.xpos, g.ypos, '*')
                screenObj.add_object(p.xpos, p.ypos, '@')
                g.jump()
                screenObj.render()
        elif command == "right":
            p.right()
            g.right()
        elif command == "left":
            p.left()
            g.left()
        elif command == "rightp":
            p.right()
        elif command == "leftp":
            p.left()
        elif command == "rightg":
            g.right()
        elif command == "leftg":
            g.left()
        elif command == "help":
            text = "Help text:\nCommands:\n\t{}:\n\t\tjumpp = JUMP\n\t\trightp or leftp = GO LEFT OR GO RIGHT\n\t{}:\n\t\tjumpg = JUMP\n\t\trightg or leftg = Go LEFT OR GO RIGHT".format(p, g)
        else:
            text = "For help input \"help\""

    screenObj.clear_screen()

