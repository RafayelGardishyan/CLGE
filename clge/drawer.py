import time

from clge.Constants import CoordinateSystems
from clge.utilities import sign
from .setup import get_platform
import sys
from .coord_translators import CoordinateTranslator
from datetime import datetime
from .Camera import Camera
from .UserDefinedFunctionManager import UserDefinedFunctionManager
import asyncio


"""
@package docstring
Screen class -> Renderer
"""
class Screen:
    default_symbol = '#'
    beforeScreen = afterScreen = ""
    
    def __init__(self, width, height, loop=False, symbol='#', border=True):
        """
        Sets screen object's main settings
        :param width: Field width
        :param height: Field height
        :param symbol: Field border symbol
        :param border: Bool: render border or not
        """
        self.field_width = 0
        self.field_height = 0
        self.timeout = .2
        self.objectsList = []
        self.auto_clear_objects_list = False
        self.auto_timeout = True
        self.rendered_frame = ""
        self.frame = ""
        self.multiple_screens = False
        self.field_width = width
        self.field_height = height
        self.default_symbol = symbol[0]
        self.border = border
        self.coordinate_system = CoordinateSystems.STANDARD
        self.camera = Camera(0, 0)
        self.previousFrame = datetime.now()
        self.deltaTime = 0.0000000
        self.FunctionManager = UserDefinedFunctionManager()
        self.loop = loop
        self.eventloop = asyncio.get_event_loop()
        self.fixedUpdateTimout = .05
        self.screen_spacing = 100 if self.field_height <= 100 else self.field_height

    def setBeforeScreen(self, string):
        """
        Set Before Screen Text
        :param string: Text
        :return: None
        """
        self.beforeScreen = string

    def setAfterScreen(self, string):
        """
        Set After Screen Text
        :param string: Text
        :return: None
        """
        self.afterScreen = string

    def setDeltatime(self):
        """
        Set time elapsed in this frame in the variable timedelta
        :return: None
        """
        thisFrame = datetime.now()
        td = thisFrame - self.previousFrame
        self.previousFrame = thisFrame
        self.deltaTime = td.total_seconds()

    def setActiveCamera(self, camera: Camera):
        """
        Function wich sets the active camera
        :param camera: A Camera class object
        :return: None
        """
        self.camera = camera

    def multiple_screen_setter(self, value):
        """
        Set multiple screen parameter
        :param value: Bool
        :return: None
        """
        self.multiple_screens = value

    def change_coordinate_system(self, system=CoordinateSystems.STANDARD):
        """
        Change Coordinate Origin
        :param system: Enum Value String
        :return:
        """
        self.coordinate_system = system

    def auto_clear_objects_list_setter(self, value):
        self.auto_clear_objects_list = value

    def auto_timeout_setter(self, value):
        self.auto_timeout = value

    def clear_screen(self):
        sys.stdout.write("\n" * self.screen_spacing)

    def add_object(self, x, y, symbol=default_symbol, color=0):
        xt, yt = CoordinateTranslator(x, y, self.field_height, self.field_width, self.coordinate_system)
        self.objectsList.append([round(xt), round(yt), symbol[0], color])

    def clear_objects_list(self):
        self.objectsList = []

    def add_string(self, x, y, text, color=0):
        x = x
        for letter in text:
            self.add_object(x, y, letter, color)
            x += 1

    def add_polygon(self, width, height, x, y, symbol=default_symbol, color=0):
        for i in range(height):
            for j in range(width):
                self.add_object(x + j, y + i, symbol, color)

    def add_line(self, x1, x2, y1, y2, symbol=default_symbol, color=0):
        # # Simple Line Drawing Algorithm
        # xs = min(x1, x2)
        # xe = max(x1, x2)
        # dx = xe - xs
        # if dx < 1:
        #     dx = 1
        # dy = y2 - y1
        #
        # for x in range(round(xs), round(xe)):
        #     y = y1 + dy * (x - xs) / dx
        #     self.add_object(x, y, symbol, color)

        # # Complex Line Drawing Algorithm
        dx = x2 - x1
        dy = y2 - y1

        sign_x = 1 if dx > 0 else -1 if dx < 0 else 0
        sign_y = 1 if dy > 0 else -1 if dy < 0 else 0

        if dx < 0: dx = -dx
        if dy < 0: dy = -dy

        if dx > dy:
            pdx, pdy = sign_x, 0
            es, el = dy, dx
        else:
            pdx, pdy = 0, sign_y
            es, el = dx, dy

        x, y = x1, y1

        error, t = el / 2, 0

        self.add_object(x, y, symbol, color)

        while t < el:
            error -= es
            if error < 0:
                error += el
                x += sign_x
                y += sign_y
            else:
                x += pdx
                y += pdy
            t += 1
            self.add_object(x, y, symbol, color)

    def set_timeout(self, seconds):
        self.timeout = seconds

    def write(self, before, after):
        if not self.multiple_screens:
            self.clear_screen()
        else:
            sys.stdout.write("")
        sys.stdout.write(before + "\n")
        sys.stdout.write(self.rendered_frame)
        sys.stdout.write(after + "\n")
        sys.stdout.flush()

    def draw(self, objects):
        self.frame = ""
        if self.border:
            self.frame += self.default_symbol * (self.field_width + 2) + "\n"
        else:
            self.frame += " " * (self.field_width + 2) + "\n"
        for i in range(self.field_height):
            camI = i - self.camera.y
            spacer = [" "] * self.field_width
            if self.border:
                draw = self.default_symbol
            else:
                draw = " "
            for j in range(self.field_width):
                camJ = j - self.camera.x
                for obj in objects:
                    if obj[0] == camJ and obj[1] == camI:
                        spacer[j] = obj[2]

            for space in spacer:
                draw += space
            if self.border:
                draw += self.default_symbol
            else:
                draw += " "
            self.frame += draw + "\n"
        if self.border:
            self.frame += self.default_symbol * (self.field_width + 2) + "\n"
        else:
            self.frame += " " * (self.field_width + 2) + "\n"

        self.rendered_frame = self.frame

    def render(self):
        self.FunctionManager.Start()
        self.FunctionManager.PreUpdate()
        self.FunctionManager.Update()
        self.setDeltatime()

        self.draw(self.objectsList)

        self.write(self.beforeScreen, self.afterScreen)

        if self.auto_clear_objects_list:
            self.clear_objects_list()
        if self.auto_timeout:
            time.sleep(self.timeout)

        self.FunctionManager.LateUpdate()

    async def runLoop(self):
        self.render()
        asyncio.ensure_future(self.runLoop())

    def Start(self):
        if self.loop:
            asyncio.ensure_future(self.runLoop())
            asyncio.ensure_future(self.FunctionManager.FixedUpdate(self.fixedUpdateTimout))
            self.eventloop.run_forever()
        else:
            self.render()


    def Stop(self):
        self.eventloop.stop()

    def __str__(self):
        return "Screen Object"

    def destroy(self):
        self.FunctionManager.Destroy()
        self = None
