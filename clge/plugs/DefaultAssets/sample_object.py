class SampleObject:
    """
    Sample Object
    """
    def __init__(self, xpos, ypos, step=1, symbol="#"):
        """
        Function which inits a Sample object
        :param xpos: X position of the object
        :param ypos: Y position of the object
        :param step: step for move_* functions
        :param symbol: symbol which will be rendered as this object
        """
        self.xpos = xpos
        self.ypos = ypos
        self.bufferx = self.xpos
        self.step = step
        self.symbol = symbol

    def move_up(self, step):
        """
        Move self up
        :param step: how many steps should the object do
        :return: None
        """
        self.ypos -= step

    def move_down(self, step):
        """
        Move self down
        :param step: how many steps should the object do
        :return: None
        """
        self.ypos += step

    def move_right(self, step):
        """
        Move self right
        :param step: how many steps should the object do
        :return: None
        """
        self.xpos += step
        self.bufferx = self.xpos

    def move_left(self, step):
        """
        Move self left
        :param step: how many steps should the object do
        :return: None
        """
        self.xpos -= step
        self.bufferx = self.xpos

    def set_step(self, step):
        """
        Change step value
        :param step: int, step value
        :return: None
        """
        self.step = step

    def add_to_screen(self, screen_object):
        """
        Add the object in the rendering queue
        :param screen_object: clge.Screen object
        :return: None
        """
        screen_object.add_object(self.xpos, self.ypos, self.symbol)
