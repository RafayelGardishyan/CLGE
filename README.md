# CLGE

## Command Line Game Engine

### Installation
To install CLGE download the engine folder and copy it to your project directory. Also if you want to user KeyDetector install python keyboard module by "pip/pip3 install keyboard"

### Example
```python
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
pleft = KeyDetector("a")
pright = KeyDetector("d")
gup = KeyDetector("up")
gleft = KeyDetector("left")
gright = KeyDetector("right")


while True:
    if pup.detect():
        for i in range(11):
            p.jump()
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
    if pleft.detect():
        p.left()
    if pright.detect():
        p.right()
    if gup.detect():
        for i in range(11):
            g.jump()
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
    if gright.detect():
        g.right()
    p.check_collision(g, screenObj)
    screenObj.add_object(p.xpos, p.ypos, '@')
    screenObj.add_object(g.xpos, g.ypos, '*')
    screenObj.render()
    screenObj.clear_screen()
```

## API reference
### Content
* Screen
* KeyDetector
* convert_to_code (For KeyDetector)
* convert_to_char (For KeyDetector)

### Screen
Example:
```python
from engine import Screen

screen_object = Screen(20, 20, symbol="/", timeout=0.5, auto_clear_objects_list=True, auto_timeout=True)

while True:
  screen_object.add_object(10, 10, "@")
  screen_object.render()
  screen_object.clear_screen()
```
This will result in:
//////////////////////
/                    /
/                    /
/                    /
/                    /
/                    /
/                    /
/                    /
/                    /
/                    /
/                    /
/          @         /
/                    /
/                    /
/                    /
/                    /
/                    /
/                    /
/                    /
/                    /
/                    /
//////////////////////

screen_object.add_polygon(5, 5, 10, 10, "%") will result in a rectangle(5 by 5) out of %'s on cordinates x:10 y:10
