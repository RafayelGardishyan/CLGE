from clge import KeymapGenerator, MouseDetector

def get_controls():
    controls = {}

    keys = KeymapGenerator()
    keys.add("up", "up")
    keys.add("down", "down")
    keys.add("left", "left")
    keys.add("right", "right")
    keys.add("exit", "esc")

    mouse_left = MouseDetector("left")
    mouse_middle = MouseDetector("middle")
    mouse_right = MouseDetector("right")
    mouse = {
        "left": mouse_left,
        "middle": mouse_middle,
        "right": mouse_right
        }

    controls['keyboard'] = keys.generate()
    controls['mouse'] = mouse

    return controls
