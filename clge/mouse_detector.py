from .exceptions import CLGEException
try:
    import mouse
    import multitasking
    import signal
    signal.signal(signal.SIGINT, multitasking.killall)
    keyboardIsImported = True
except ImportError:
    keyboardIsImported = False
    raise CLGEException("Error: No mouse detection or multitasking, please install mouse and multitasking packages by \"pip install mouse multitasking\"")


class MouseDetector:
    button = None

    def __init__(self, button):
        self.button = button

    @multitasking.task
    def setAsyncDetecting(self, function):
        while True:
            if self.detect():
                function()

    def detect(self):
        if keyboardIsImported:
            try:
                if mouse.is_pressed(self.button):
                    mouse.release(button=self.button)
                    return True
                else:
                    return False
            except:
                return False
        else:
            print("Info: No mouse detection, please install mouse package by \"pip install mouse\"")


def generate_mousemap(buttons):
    mousemap = {}
    for key, value in buttons.items():
        mousemap[key] = MouseDetector(value)
    return mousemap
