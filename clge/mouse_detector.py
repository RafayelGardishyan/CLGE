import mouse


class MouseDetector:
    button = None

    def __init__(self, button):
        self.button = button

    def detect(self):
        return mouse.is_pressed(self.button)

    def __str__(self):
        return "Mouse Detector Object"


def generate_mousemap(buttons):
    mousemap = {}
    for key, value in buttons.items():
        mousemap[key] = MouseDetector(value)
    return mousemap