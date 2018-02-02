from clge import Screen, KeyDetector, generate_keymap
import random

scr = Screen(20, 20, auto_clear_objects_list=True, timeout=.5, auto_timeout=False)
game_over = """   _____                         ____                 
  / ____|                       / __ \                
 | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
 | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
 | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|"""

values = {
    'score': 0,
    'level': 1,
    'buffer': 0
}

tailX = [None] * (scr.field_width * scr.field_height)
tailY = [None] * (scr.field_width * scr.field_height)

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

snake = {
    'x': int(scr.field_width/2),
    'y': int(scr.field_height/2),
    'dir': 'stop',
    'length': 0
}

fruit = {
    'x': random.randint(0, scr.field_width - 1),
    'y': random.randint(0, scr.field_height - 1)
}


def detect():
    if keys['up'].detect() or keys['up_arrow'].detect():
        snake['dir'] = 'up'
    if keys['down'].detect() or keys['down_arrow'].detect():
        snake['dir'] = 'down'
    if keys['right'].detect() or keys['right_arrow'].detect():
        snake['dir'] = 'right'
    if keys['left'].detect() or keys['left_arrow'].detect():
        snake['dir'] = 'left'


def move():
    if snake['dir'] == "up":
        snake['y'] -= 1
    if snake['dir'] == "down":
        snake['y'] += 1
    if snake['dir'] == "right":
        snake['x'] += 1
    if snake['dir'] == "left":
        snake['x'] -= 1

    if snake['x'] < 0:
        snake['x'] = scr.field_width - 1
    elif snake['x'] > scr.field_width:
        snake['x'] = 0
    elif snake['y'] < 0:
        snake['y'] = scr.field_height - 1
    elif snake['y'] > scr.field_height:
        snake['y'] = 0


def check_collision():
    for i in range(snake['length']):
        if snake['x'] == tailX[i] and snake['y'] == tailY[i]:
            return True



def check_fruit_collision():
    if snake['x'] == fruit['x'] and snake['y'] == fruit['y']:
        fruit['x'] = random.randint(0, scr.field_width - 1)
        fruit['y'] = random.randint(0, scr.field_height - 1)
        values['score'] += 1
        snake['length'] += 1
        if values['buffer'] == (values['level'] * 2):
            values['buffer'] = 0
            values['level'] += 1
        else:
            values['buffer'] += 1

def set_speed():
    scr.timeout = (.5 / (values['level'] * 0.5))

def tailor():
    prevX = tailX[0]
    prevY = tailY[0]
    tailX[0] = snake['x']
    tailY[0] = snake['y']
    prev2X = 0
    prev2Y = 0
    for i in range(1, snake['length']):
        prev2X = tailX[i]
        prev2Y = tailY[i]
        tailX[i] = prevX
        tailY[i] = prevY
        prevX = prev2X
        prevY = prev2Y

while True:
    set_speed()
    scr.add_object(snake['x'], snake['y'], "O")
    scr.add_object(fruit['x'], fruit['y'], "F")
    scr.render()
    print("Score: {} Level: {}".format(values['score'], values['level']))
    scr.do_timeout()
    scr.clear_screen()
    detect()
    tailor()
    for i in range(snake['length']):
        scr.add_object(tailX[i], tailY[i], "o")
    move()
    check_fruit_collision()
    if check_collision():
        print(game_over)
        print("You reached {} level and your score was {}".format(values['level'], values['score']))
        raise SystemExit
