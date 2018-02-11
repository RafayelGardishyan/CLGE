from interaction import get_controls
from sounds import get_sounds
import random

keys = get_controls()
sounds = get_sounds()

def move(player, width, height, sound_enabled):
    if sound_enabled:
        if keys["keyboard"]["up"].detect():
            sounds["sound1"].play()
            player.move_up()
        if keys["keyboard"]["down"].detect():
            sounds["sound1"].play()
            player.move_down()
        if keys["keyboard"]["left"].detect():
            sounds["sound1"].play()
            player.move_left()
        if keys["keyboard"]["right"].detect():
            sounds["sound1"].play()
            player.move_right()
    else:
        if keys["keyboard"]["up"].detect():
            player.move_up()
        if keys["keyboard"]["down"].detect():
            player.move_down()
        if keys["keyboard"]["left"].detect():
            player.move_left()
        if keys["keyboard"]["right"].detect():
            player.move_right()

    if keys["keyboard"]["exit"].detect():
        print("\n"*100)
        print("You exited the game")
        raise SystemExit

    if player.xpos > width:
        player.xpos = 0
    elif player.xpos < 0:
        player.xpos = width

    if player.ypos > height:
        player.ypos = 0
    elif player.ypos < 0:
        player.ypos = height

def reposition_fruit(fruit, width, height):
    fruit.xpos = random.randint(0, width)
    fruit.ypos = random.randint(0, height)

def fruit_first_pos_x(width):
    return random.randint(0, width)

def fruit_first_pos_y(height):
    return random.randint(0, height)

def check_fruit_collision(player, fruit):
    if player.xpos == fruit.xpos and player.ypos == fruit.ypos:
        return True
    else:
        return False
def check_collision_and_add_points(player, fruit, points, field_params):
    if check_fruit_collision(player, fruit):
        reposition_fruit(fruit, field_params["width"], field_params["height"])
        return points + 1
    else:
        return points
