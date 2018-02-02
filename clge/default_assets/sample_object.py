class SampleObject:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.bufferx = self.xpos

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
