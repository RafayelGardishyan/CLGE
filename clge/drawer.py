import time
from colored import fg
from .setup import get_platform
import sys

class Screen:
    def __init__(self, width, height, symbol='#', border=True):
        self.field_width = 0
        self.field_height = 0
        self.default_symbol = '#'
        self.timeout = 1
        self.objectsList = []
        self.auto_clear_objects_list = False
        self.auto_timeout = True
        self.default_color = 256
        self.rendered_frame = ""
        self.frame = ""
        self.multiple_screens = False
        self.field_width = width
        self.field_height = height
        self.default_symbol = symbol[0]
        self.border = border

    def multiple_screen_setter(self, value):
        self.multiple_screens = value

    def auto_clear_objects_list_setter(self, value):
        self.auto_clear_objects_list = value

    def auto_timeout_setter(self, value):
        self.auto_timeout = value

    def color_setter(self, value):
        self.default_color = fg(value)

    @staticmethod
    def clear_screen():
        print('\n' * 100)

    def add_object(self, x, y, symbol=default_symbol, color=default_color):
        self.objectsList.append([x, y, symbol, fg(color)])

    def clear_objects_list(self):
        self.objectsList = []

    def add_string(self, x, y, text, color=default_color):
        x = x
        for letter in text:
            self.add_object(x, y, letter, color)
            x += 1

    def add_polygon(self, width, height, x, y, symbol=default_symbol, color=default_color):
        for i in range(height):
            for j in range(width):
                self.add_object(x + j, y + i, symbol, color)

    def do_timeout(self):
        time.sleep(self.timeout)

    def set_timeout(self, seconds):
        self.timeout = seconds

    def write(self, before, after):
        if not self.multiple_screens:
            sys.stdout.write("\n" * 100)
        else:
            sys.stdout.write("")
        sys.stdout.write(before + "\n")
        sys.stdout.write(self.rendered_frame)
        sys.stdout.write(after + "\n")
        sys.stdout.flush()

    def draw(self, objects):
        self.frame = ""
        if self.border:
            self.frame += self.default_color + self.default_symbol * (self.field_width + 2) + self.default_color + "\n"
        else:
            self.frame += self.default_color + " " * (self.field_width + 2) + self.default_color + "\n"
        for i in range(self.field_height):
            spacer = [" "] * self.field_width
            if self.border:
                draw = self.default_color + self.default_symbol + self.default_color
            else:
                draw = self.default_color + " " + self.default_color
            for j in range(self.field_width):
                for obj in objects:
                    if obj[0] == j and obj[1] == i:
                        spacer[j] = str(obj[3]) + obj[2] + str(self.default_color)

            for space in spacer:
                draw += space
            if self.border:
                draw += self.default_color + self.default_symbol + self.default_color
            else:
                draw += self.default_color + " " + self.default_color
            self.frame += draw + "\n"
        if self.border:
            self.frame += self.default_color + self.default_symbol * (self.field_width + 2) + self.default_color + "\n"
        else:
            self.frame += self.default_color + " " * (self.field_width + 2) + self.default_color + "\n"

        self.rendered_frame = self.frame

    def draw_no_colors(self, objects):
        self.frame = ""
        if self.border:
            self.frame += self.default_symbol * (self.field_width + 2) + "\n"
        else:
            self.frame += " " * (self.field_width + 2) + "\n"
        for i in range(self.field_height):
            spacer = [" "] * self.field_width
            draw = self.default_symbol
            for j in range(self.field_width):
                for obj in objects:
                    if obj[0] == j and obj[1] == i:
                        spacer[j] = obj[2]
            for space in spacer:
                draw += space
            draw += self.default_symbol
            self.frame += draw + "\n"
        if self.border:
            self.frame += self.default_symbol * (self.field_width + 2) + "\n"
        else:
            self.frame += " " * (self.field_width + 2) + "\n"

        self.rendered_frame = self.frame

    def render(self, before_screen="", after_screen=""):
        if get_platform() == "Windows":
            self.draw_no_colors(self.objectsList)
        else:
            self.draw(self.objectsList)

        self.write(before_screen, after_screen)

        if self.auto_clear_objects_list:
            self.clear_objects_list()
        if self.auto_timeout:
            self.do_timeout()

    def __str__(self):
        return "Screen Object"
