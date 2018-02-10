from clge import Screen, DefaultAssets, generate_keymap

scr = Screen(40, 40, "#", 0.1, True)

keys = generate_keymap({
    "o": "o",
    "p": "p",
    "w": "w",
    "a": "a",
    "s": "s",
    "d": "d",
    "exit": "esc"
})

sampleobject = DefaultAssets.SampleObject(5, 5, 1, "^")
samplepolygon = DefaultAssets.SamplePolygon(5, 5, 5, 5, "%")


def detect_movement():
    if keys['w'].detect():
        sampleobject.move_up(1)
        samplepolygon.move_up(1)
    elif keys['s'].detect():
        sampleobject.move_down(1)
        samplepolygon.move_down(1)
    elif keys['a'].detect():
        sampleobject.move_left(1)
        samplepolygon.move_left(1)
    elif keys['d'].detect():
        sampleobject.move_right(1)
        samplepolygon.move_right(1)


while True:
    if keys['exit'].detect():
        raise SystemExit
    scr.clear_screen()
    detect_movement()
    if keys['o'].detect():
        sampleobject.add_to_screen(scr)
    elif keys['p'].detect():
        samplepolygon.add_to_screen(scr)
    scr.render()
