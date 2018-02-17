import keyboard


class KeyDetector:
    char = None

    def __init__(self, key):
        self.char = key

    def detect(self):
        return keyboard.is_pressed(self.char)

    def __str__(self):
        return "Key Detector Object"


def convert_to_code(char):
    return ord(char)


def convert_to_char(code):
    return chr(code)


def generate_keymap(keys):
    keymap = {}
    for key, value in keys.items():
        keymap[key] = KeyDetector(value)
    return keymap

class KeymapGenerator:
    keys = {}
    def add(self, name, key):
        self.keys[name] = key

    def generate(self):
        return generate_keymap(self.keys)
