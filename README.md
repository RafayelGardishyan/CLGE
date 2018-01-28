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
* AudioPlayer
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
```
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
```

screen_object.set_timeout(5) will set screen timeout to 5 seconds
screen_object.do_timeout() will do timeout
screen_object.add_polygon(5, 5, 10, 10, "%") will result in a rectangle(5 by 5) out of %'s on cordinates x:10 y:10

### AudioPlayer
To play audio you can use the AudioPlayer

Usage:

To play a sound create AudioPlayer object and then when you want to play the sound use audioplayer_object.play()

Example:
```python
from engine import AudioPlayer

audioplayer_object = AudioPlayer("C:/Users/Example/Documents/Sound.mp3", async=True)
audioplayer_object.play()
```
This will play the sound located at C:/Users/Example/Documents/Sound.mp3

### KeyDetector
To use a key detector you have to create an object of a KeyDetector and every time you want to chech is a key is pressed you have to use the detect function.
Example:
```python
from engine import KeyDetector

detector_object = KeyDetector("a")

while True:
    if detector_object.detect():
        print("Output: You pressed a")
    else:
        print("Output: You don't press a")
```

This will result in: 
(1-5 time: I don't press a)
(6 time: I press a)
```
Output: You don't press a
Output: You don't press a
Output: You don't press a
Output: You don't press a
Output: You don't press a
Output: You pressed a
```

### convert_to_code
This functions converts a 1 character string into a charcter code
Usage:
```python 
from engine import convert_to_code

print(convert_to_code("a"))
```
### convert_to_char
This functions converts a character code into a charcter string
Usage:
```python 
from engine import convert_to_char

print(convert_to_char(36))
```
