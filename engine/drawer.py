import time


class Screen:
    field_width = 0
    field_height = 0
    default_symbol = '#'
    timeout = 1
    objectsList = []
    auto_clear_objects_list = False
    auto_timeout = True

    def __init__(self, width, height, symbol='#', timeout=1.0, auto_clear_objects_list=False, auto_timeout=True):
        self.field_width = width
        self.field_height = height
        self.default_symbol = symbol
        self.timeout = timeout
        self.auto_clear_objects_list = auto_clear_objects_list
        self.auto_timeout = auto_timeout
        
    def clear_screen(self):
        print('\n' * 100)

    def add_object(self, x, y, symbol=default_symbol):
        if not len(symbol) > 1:
            self.objectsList.append([x, y, symbol])
        else:
            self.objectsList.append([x, y, symbol[:1]])

    def clear_objects_list(self):
        self.objectsList = []


    def add_polygon(self, width, height, x, y, symbol=default_symbol):
        for i in range(height):
            for j in range(width):
                self.add_object(x + j, y + i, symbol)


    def draw(self, objects):
        print(self.default_symbol * (self.field_width + 2))
        for i in range(self.field_height):
            spacer = []
            for k in range(self.field_width):
                spacer.append(' ')
            draw = self.default_symbol
            for j in range(self.field_width):
                for obj in objects:
                    if obj[0] == j and obj[1] == i:
                        try:
                            spacer[j] = obj[2]
                        except:
                            spacer[j] = self.default_symbol

            for space in spacer:
                draw += space
            draw += self.default_symbol
            print(draw)
        print(self.default_symbol * (self.field_width + 2))
        if self.auto_clear_objects_list:
            self.clear_objects_list()
        if self.auto_timeout:
            time.sleep(self.timeout)

    def render(self):
        self.draw(self.objectsList)
