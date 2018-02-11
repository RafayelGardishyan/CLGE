class SamplePolygon:
    def __init__(self, x, y, width, height, symbol="#"):
        self.width = width
        self.height = height
        self.xpos = x
        self.ypos = y
        self.symbol = symbol
        self.bufferx = self.xpos
        self.buffery = self.ypos

    def move_up(self, step):
        self.ypos -= step

    def move_down(self, step):
        self.ypos += step

    def move_right(self, step):
        self.xpos += step
        self.bufferx = self.xpos

    def move_left(self, step):
        self.xpos -= step
        self.bufferx = self.xpos

    def set_step(self, step):
        self.step = step

    def add_to_screen(self, screen_object):
        screen_object.add_polygon(self.width, self.height, self.xpos, self.ypos, self.symbol)
