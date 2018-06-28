class SamplePlayer:
    """
    Sample Player class
    """
    def __init__(self, xpos, ypos, step, lives, symbol="#"):
        """
        Function which inits a Sample Player
        :param xpos: X position of the Player
        :param ypos: Y position of the Player
        :param step: How many steps should the Player do in move_* functions
        :param lives: How many lives has the player
        :param symbol: Symbol used to render the player
        """
        self.xpos = xpos
        self.ypos = ypos
        self.step = step
        self.lives = lives
        self.bufferx = self.xpos
        self.buffery = self.ypos
        self.jump = True
        self.symbol = symbol

    def move_up(self):
        """
        Move the Player up
        :return: None
        """
        self.ypos -= self.step

    def move_down(self):
        """
        Move the Player down
        :return: None
        """
        self.ypos += self.step

    def move_right(self):
        """
        Move the Player right
        :return: None
        """
        self.xpos += self.step
        self.bufferx = self.xpos

    def move_left(self):
        """
        Move the Player left
        :return: None
        """
        self.xpos -= self.step
        self.bufferx = self.xpos

    def set_step(self, step):
        """
        Set the step variable for Player object
        :param step: int, step
        :return: None
        """
        self.step = step

    def get_lives(self):
        """
        Function which return how many lives the player has
        :return: Player lives
        """
        return self.lives

    def is_alive(self):
        """
        Returns is Player live status
        :return: True(If the lives-var contains a higher int than 0)/False
        """
        if self.lives <= 0:
            return False
        else:
            return True

    def jump_algo(self, level):
        """
        Function which should be called every frame to let the Player jump
        :param level: How high the player has to jump
        :return: None
        """
        if self.ypos > level and self.jump:
            self.move_up()
        elif self.ypos == level:
            self.jump = False
            self.move_down()
        else:
            self.jump = True

    def check_if_on_tile(self, tile):
        """
        Function which checks is the player is on a tile(coming soon)
        :param tile: Tile object -> Polygon child
        :return: True/False
        """
        if self.xpos == tile.xpos and self.ypos == tile.ypos - 1:
            return True
        else:
            return False

    def add_to_screen(self, screen_object):
        """
        Add the Player in the rendering queue
        :param screen_object: clge.Screen object
        :return: None
        """
        screen_object.add_object(self.xpos, self.ypos, self.symbol)

