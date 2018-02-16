from clge import KeymapGenerator
from clge import SimpleTester
from clge import Screen
from clge import paint_text
from clge import convert_to_code
from clge import convert_to_char
from clge import CLGEException
from clge import generate_mousemap

t = SimpleTester(5)

t.CoverageStart()

class SnakeTestException(Exception):
    def __init__(self, message):
        self.message = message

def test_exception():
    raise CLGEException("Testing Exception")

def mouse_test():
    keys = generate_mousemap({"l":"left", "r": "right", "m": "middle"})
    for key in keys:
        t.simulate_mouse_press(keys[key].button)
        if keys[key].detect():
            pass
        else:
            t.simulate_mouse_release(keys[key].button)
            raise SnakeTestException("Key {} in not detected".format(keys[key].button))
        t.simulate_mouse_release(keys[key].button)

def test_screen():
    scr = Screen(20, 20, auto_clear_objects_list=True, timeout=.5, auto_timeout=False, default_color=39)
    for i in range(20):
        for i in range(20):
            scr.add_object(i, i*i, "I", i)
        scr.render()

def color_test():
    for i in range(200):
        for j in range(200):
            print(paint_text("Test", i, 5, True))
            print(paint_text("Test", i, 5, False))

def test_tail():
    tailX = [None] * 20
    tailY = [None] * 20
    for j in range(5):
        prevX = tailX[0]
        prevY = tailY[0]
        tailX[0] = j
        tailY[0] = j*2
        prev2X = 0
        prev2Y = 0
        for i in range(1, 20):
            prev2X = tailX[i]
            prev2Y = tailY[i]
            tailX[i] = prevX
            tailY[i] = prevY
            prevX = prev2X
            prevY = prev2Y

def test_keyboard():
    keys = KeymapGenerator()
    keys.add('up', 'w')
    keys.add('up_arrow', 'up')
    keys.add('down', 's')
    keys.add('down_arrow', 'down')
    keys.add('right', 'd')
    keys.add('right_arrow', 'right')
    keys.add('left', 'a')
    keys.add('left_arrow', 'left')
    keys = keys.generate()
    # keys["up"].detAsyncDetecting()
    keys["up"].setAsyncDetecting()
    print(convert_to_code("a"), convert_to_char(15))
    for key in keys:
        t.simulate_keyboard_press(keys[key].char)
        if keys[key].detect():
            pass
        else:
            t.simulate_keyboard_release(keys[key].char)
            raise SnakeTestException("Key {} in not detected".format(keys[key].char))
        t.simulate_keyboard_release(keys[key].char)

def test_collision(cases):
    for i in cases:
        if i[0] == i[1] and i[2] == i[3]:
            print(i)
        else:
            pass


t.Test(test_exception)
t.Test(mouse_test)
t.Test(test_screen)
t.Test(test_keyboard)
t.Test(test_tail)
t.Test(test_collision, [[0, 1, 2, 3], [0, 0, 2, 4], [3, 1, 3, 3]])
t.Test(color_test)
t.CoverageStop()
t.printTestResults()
t.getCoverage()
