import time
from colored import fg, attr
from clge.setup import get_platform
import sys


class Screen:
    field_width = 0
    field_height = 0
    default_symbol = '#'
    timeout = 1
    objectsList = []
    auto_clear_objects_list = False
    auto_timeout = True
    default_color = attr(0)
    rendered_frame = ""
    frame = []
    multiple_screens = False

    def __init__(self, width, height, symbol='#', border=True):
        self.field_width = width
        self.field_height = height
        self.default_symbol = symbol[0]
        self.border = border
        self.last_element_id = self.field_height - 1

    def multiple_screen_setter(self, value):
        self.multiple_screens = value

    def auto_clear_objects_list_setter(self, value):
        self.auto_clear_objects_list = value

    def auto_timeout_setter(self, value):
        self.auto_timeout = value

    def color_setter(self, value):
        if value != attr(0):
            self.default_color = fg(value)
        else:
            self.default_color = value

    # def clear_screen(self):
    #     print('\n' * 100)

    def add_object(self, x, y, symbol=default_symbol, color=default_color):
        try:
            if not len(symbol) > 1:
                self.objectsList.append([x, y, symbol, fg(color)])
            else:
                self.objectsList.append([x, y, symbol[:1], fg(color)])
        except KeyError:
            if not len(symbol) > 1:
                self.objectsList.append([x, y, symbol, color])
            else:
                self.objectsList.append([x, y, symbol[:1], color])

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

    def render_frame(self):
        print(self.frame)
        for line in self.frame:
            for pos in line:
                self.rendered_frame += pos
            self.rendered_frame += "\n"

    def draw(self, objects):
        self.frame = [[" "] * self.field_width] * self.field_height
        if self.border:
            self.frame[0] = [(self.default_color + self.default_symbol + self.default_color)] * (self.field_width + 2)
        else:
            self.frame[0] = [(self.default_color + " " + self.default_color)] * (self.field_width + 2)

        for x in objects:
            self.frame[x[1]][x[0]] = x[3] + x[2] + self.default_color

        if self.border:
            self.frame[self.last_element_id] = [(self.default_color + self.default_symbol + self.default_color)] * (self.field_width + 2)
        else:
            self.frame[self.last_element_id] = [(self.default_color + " " + self.default_color)] * (self.field_width + 2)

    def draw_no_colors(self, objects):
        self.frame = [[" "] * self.field_width] * self.field_height
        if self.border:
            self.frame[0] = [self.default_symbol] * (self.field_width + 2)
        else:
            self.frame[0] = [" "] * (self.field_width + 2)

        for x in objects:
            self.frame[x[1]][x[0]] = x[3] + x[2]

        if self.border:
            self.frame[self.last_element_id] = [self.default_symbol] * (self.field_width + 2)
        else:
            self.frame[self.last_element_id] = [" "] * (self.field_width + 2)

    def render(self, before_screen="", after_screen=""):
        if get_platform() == "Windows":
            self.draw_no_colors(self.objectsList)
        else:
            self.draw(self.objectsList)

        self.render_frame()
        self.write(before_screen, after_screen)

        if self.auto_clear_objects_list:
            self.clear_objects_list()
        if self.auto_timeout:
            self.do_timeout()

    def __str__(self):
        return "Screen Object"



test = Screen(20, 20)
test.add_object(10, 10)
test.add_object(5, 15)
test.render()
