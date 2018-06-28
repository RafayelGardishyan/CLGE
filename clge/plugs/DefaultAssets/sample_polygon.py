class SamplePolygon:
    """
    Sample Polygon class
    """
    def __init__(self, x, y, width, height, symbol="#", step=1):
        """
        Function which inits a Polygon object
        :param x: X position of the polygon
        :param y: Y position of the polygon
        :param width: polygon width
        :param height: polygon height
        :param symbol: symbol which will be used to render the polygon
        :param step: How many steps should the polygon dot in a move_* function
        """
        self.width = width
        self.height = height
        self.xpos = x
        self.ypos = y
        self.symbol = symbol
        self.bufferx = self.xpos
        self.buffery = self.ypos
        self.step = step

    def move_up(self, step):
        """
        Move the polygon up
        :param step: How many steps should the polygon do
        :return: None
        """
        self.ypos -= step

    def move_down(self, step):
        """
        Move the polygon down
        :param step: How many steps should the polygon do
        :return: None
        """
        self.ypos += step

    def move_right(self, step):
        """
        Move the polygon right
        :param step: How many steps should the polygon do
        :return: None
        """
        self.xpos += step
        self.bufferx = self.xpos

    def move_left(self, step):
        """
        Move the polygon left
        :param step: How many steps should the polygon do
        :return: None
        """
        self.xpos -= step
        self.bufferx = self.xpos

    def set_step(self, step):
        """
        Function which sets the step variable
        :param step: int, step
        :return: None
        """
        self.step = step

    def add_to_screen(self, screen_object):
        """
        Add the polygon in the rendering queue
        :param screen_object: clge.Screen object
        :return: None
        """
        screen_object.add_polygon(self.width, self.height, self.xpos, self.ypos, self.symbol)
