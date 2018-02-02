class SamplePlayer:
    def __init__(self, xpos, ypos, step, lives):
        self.xpos = xpos
        self.ypos = ypos
        self.step = step
        self.lives = lives
        self.bufferx = self.xpos
        self.buffery = self.ypos
        self.jump = True

    def move_up(self):
        self.ypos -= self.step

    def move_down(self):
        self.ypos += self.step

    def move_right(self):
        self.xpos += self.step
        self.bufferx = self.xpos

    def move_left(self):
        self.xpos -= self.step
        self.bufferx = self.xpos

    def set_step(self, step):
        self.step = step

    def get_lives(self):
        return self.lives

    def is_alive(self):
        if self.lives <= 0:
            return False
        else:
            return True

    def jump_algo(self, level):
        if self.ypos > level and self.jump:
            self.move_up()
        elif self.ypos == level:
            self.jump = False
            self.move_down()
        else:
            self.jump = True

    def check_if_on_tile(self, tile):
        if self.xpos == tile.xpos and self.ypos == tile.ypos - 1:
            return True
        else:
            return False