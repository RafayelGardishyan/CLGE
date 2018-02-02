import asyncio

try:
    import keyboard
    keyboardIsImported = True
except ImportError:
    keyboardIsImported = False
    print("Error: No keyboard detection, please install keyboard package by \"pip install keyboard\"")
    raise SystemExit


class KeyDetector:
    char = None

    def __init__(self, key):
        self.char = key

    def detect(self):
        if keyboardIsImported:
            try:
                if keyboard.is_pressed(self.char):
                    return True
                else:
                    return False
            except:
                return False
        else:
            print("Info: No keyboard detection, please install keyboard package by \"pip install keyboard\"")


def convert_to_code(char):
    return ord(char)

def convert_to_char(code):
    return chr(code)

def generate_keymap(keys):
    keymap = {}
    for key, value in keys.items():
        keymap[key] = KeyDetector(value)
    return keymap
