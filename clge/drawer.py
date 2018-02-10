import time
from colored import fg, attr
from .setup import get_platform

class Screen:
    field_width = 0
    field_height = 0
    default_symbol = '#'
    timeout = 1
    objectsList = []
    auto_clear_objects_list = False
    auto_timeout = True
    default_color = attr(0)

    def __init__(self, width, height, symbol='#', timeout=1.0, auto_clear_objects_list=False, auto_timeout=True, default_color=attr(0)):
        self.field_width = width
        self.field_height = height
        self.default_symbol = symbol
        self.timeout = timeout
        self.auto_clear_objects_list = auto_clear_objects_list
        self.auto_timeout = auto_timeout
        if default_color != attr(0):
            self.default_color = fg(default_color)
        else:
            self.default_color = default_color

    def clear_screen(self):
        print('\n' * 100)

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

    def add_polygon(self, width, height, x, y, symbol=default_symbol, color=default_color):
        for i in range(height):
            for j in range(width):
                self.add_object(x + j, y + i, symbol, color)

    def do_timeout(self):
        time.sleep(self.timeout)

    def set_timeout(self, seconds):
        self.timeout = seconds

    def draw(self, objects):
        print(self.default_color + self.default_symbol * (self.field_width + 2) + self.default_color)
        for i in range(self.field_height):
            spacer = []
            for k in range(self.field_width):
                spacer.append(' ')
            draw = self.default_color + self.default_symbol + self.default_color
            for j in range(self.field_width):
                for obj in objects:
                    if obj[0] == j and obj[1] == i:
                        spacer[j] = str(obj[3]) + obj[2] + str(self.default_color)
                        
            for space in spacer:
                draw += space
            draw += self.default_color + self.default_symbol + self.default_color
            print(draw)
        print(self.default_color + self.default_symbol * (self.field_width + 2) + self.default_color)
    #TODO Add Windows COnsole Colors
    def draw_no_colors(self, objects):
        print(self.default_symbol * (self.field_width + 2))
        for i in range(self.field_height):
            spacer = []
            for k in range(self.field_width):
                spacer.append(' ')
            draw = self.default_symbol
            for j in range(self.field_width):
                for obj in objects:
                    if obj[0] == j and obj[1] == i:
                        spacer[j] = obj[2]
            for space in spacer:
                draw += space
            draw += self.default_symbol
            print(draw)
        print(self.default_symbol * (self.field_width + 2))

    def render(self):
        if get_platform() == "Windows":
            self.draw_no_colors(self.objectsList)
        else:
            self.draw(self.objectsList)
        if self.auto_clear_objects_list:
            self.clear_objects_list()
        if self.auto_timeout:
            self.do_timeout()

    def __str__(self):
        return "Screen Object"
