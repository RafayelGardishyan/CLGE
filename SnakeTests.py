from clge import Tester, Screen, generate_keymap

t = Tester()

t.CoverageStart()

class SnakeTestException(Exception):
    def __init__(self, message):
        self.message = message

def test_screen():
    scr = Screen(20, 20, auto_clear_objects_list=True, timeout=.5, auto_timeout=False, default_color=39)
    return scr


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
    keys = generate_keymap({
        'up': 'w',
        'up_arrow': 'up',
        'down': 's',
        'down_arrow': 'down',
        'right': 'd',
        'right_arrow': 'right',
        'left': 'a',
        'left_arrow': 'left',
    })
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


t.Test(test_screen)
t.Test(test_keyboard)
t.Test(test_tail)
t.Test(test_collision, [[0, 1, 2, 3], [0, 0, 2, 4], [3, 1, 3, 3]])
t.CoverageStop()
t.printTestResults()
t.getCoverage()