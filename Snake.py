from clge import Screen, AudioPlayer, generate_keymap, paint_text
import secrets
import time

scr = Screen(27, 20, "#", True)
scr.color_setter(39)
scr.auto_timeout_setter(False)
scr.set_timeout(.5)
scr.auto_clear_objects_list_setter(True)

sound_prefix = "snake_sound"
sounds = [sound_prefix + "/level_up.wav", sound_prefix + "/player_moves.wav", sound_prefix + "/player_picks_fruit.wav",]
sound_objects = {}
for sound in sounds:
    sound_objects[sound] = AudioPlayer(sound)

game_over = """   _____                         ____
  / ____|                       / __ \                
 | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
 | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
 | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|"""

pause = """  _____       _    _  _____ ______
 |  __ \ /\  | |  | |/ ____|  ____|
 | |__) /  \ | |  | | (___ | |__   
 |  ___/ /\ \| |  | |\___ \|  __|  
 | |  / ____ \ |__| |____) | |____ 
 |_| /_/    \_\____/|_____/|______|"""

Exit = """  ______      _ _
 |  ____|    (_) |  
 | |__  __  ___| |_ 
 |  __| \ \/ / | __|
 | |____ >  <| | |_ 
 |______/_/\_\_|\__|"""

title = """  _____             _
 / ____|           | |       
| (___  _ __   __ _| | _____ 
 \___ \| '_ \ / _` | |/ / _ \\
 ____) | | | | (_| |   <  __/
|_____/|_| |_|\__,_|_|\_\___|"""

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
    'pause': 'p',
    'Exit': 'esc',
})

snake = {
    'x': int(scr.field_width/2),
    'y': int(scr.field_height/2),
    'dir': 'stop',
    'length': 0
}

fruit = {
    'x': secrets.randbelow(scr.field_width - 1),
    'y': secrets.randbelow(scr.field_height - 1)
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
    if keys['pause'].detect():
        while True:
            print(paint_text(pause, 23, 0, True))
            print(paint_text(" Press P to play", 64, 0, True))
            time.sleep(1)
            scr.clear_screen()
            if keys['pause'].detect():
                break

    if keys['Exit'].detect():
        print(paint_text(Exit, 23, 0, True))
        print(paint_text(" You reached {} level and your score was {}".format(values['level'], values['score']), 64, 0, True))
        raise SystemExit


def move():
    if snake['dir'] == "up":
        sound_objects['snake_sound/player_moves.wav'].play()
        snake['y'] -= 1
    if snake['dir'] == "down":
        sound_objects['snake_sound/player_moves.wav'].play()
        snake['y'] += 1
    if snake['dir'] == "right":
        sound_objects['snake_sound/player_moves.wav'].play()
        snake['x'] += 1
    if snake['dir'] == "left":
        sound_objects['snake_sound/player_moves.wav'].play()
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
        sound_objects['snake_sound/player_picks_fruit.wav'].play()
        fruit['x'] = secrets.randbelow(scr.field_width - 1)
        fruit['y'] = secrets.randbelow(scr.field_height - 1)
        values['score'] += 1
        snake['length'] += 1
        if values['buffer'] == (values['level'] * 2):
            sound_objects['snake_sound/level_up.wav'].play()
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
    scr.add_object(snake['x'], snake['y'], "O", 214)
    scr.add_object(fruit['x'], fruit['y'], "+", 202)
    scr.render(title, "{} {}".format(paint_text("Score: {}".format(values['score']), 3, 0, True), paint_text("Level: {}".format(values['level']), 50, 0, True)))
    scr.do_timeout()
    # scr.clear_screen()
    detect()
    tailor()
    for i in range(snake['length']):
        scr.add_object(tailX[i], tailY[i], symbol="o", color=114)
    move()
    check_fruit_collision()
    if check_collision():
        print(paint_text(game_over, 23, 0, True))
        print(paint_text(" You reached {} level and your score was {}".format(values['level'], values['score']), 64, 0, True))
        raise SystemExit
