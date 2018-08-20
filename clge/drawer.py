import time
from colored import fg
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
    default_color = fg(255)
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
        self.coordinate_system = "std"
        self.camera = Camera(0, 0)
        self.previousFrame = datetime.now()
        self.deltaTime = 0.0000000
        self.FunctionManager = UserDefinedFunctionManager()
        self.loop = loop
        self.eventloop = asyncio.get_event_loop()
        self.fixedUpdateTimout = .05

    def setBeforeScreen(self, string):
        self.beforeScreen = string

    def setAfterScreen(self, string):
        self.afterScreen = string

    def setDeltatime(self):
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

    def change_coordinate_system(self, system="std"):

        self.coordinate_system = system

    def auto_clear_objects_list_setter(self, value):
        self.auto_clear_objects_list = value

    def auto_timeout_setter(self, value):
        self.auto_timeout = value

    def color_setter(self, value):
        self.default_color = fg(value)

    @staticmethod
    def clear_screen():
        print('\n' * 100)

    def add_object(self, x, y, symbol=default_symbol, color=default_color):
        xt, yt = CoordinateTranslator(x, y, self.field_height, self.field_width, self.coordinate_system)
        self.objectsList.append([round(xt), round(yt), symbol, color])

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

    def draw(self, objects):
        self.frame = ""
        if self.border:
            self.frame += self.default_color + self.default_symbol * (self.field_width + 2) + self.default_color + "\n"
        else:
            self.frame += self.default_color + " " * (self.field_width + 2) + self.default_color + "\n"
        for i in range(self.field_height):
            camI = i - self.camera.y
            spacer = [" "] * self.field_width
            if self.border:
                draw = self.default_color + self.default_symbol + self.default_color
            else:
                draw = self.default_color + " " + self.default_color
            for j in range(self.field_width):
                camJ = j - self.camera.x
                for obj in objects:
                    if obj[0] == camJ and obj[1] == camI:
                        spacer[j] = str(obj[3]) + obj[2] + str(self.default_color)

            for space in spacer:
                draw += space
            if self.border:
                draw += self.default_color + self.default_symbol + self.default_color
            else:
                draw += self.default_color + " " + self.default_color
            self.frame += draw + "\n"
        if self.border:
            self.frame += self.default_color + self.default_symbol * (self.field_width + 2) + self.default_color + "\n"
        else:
            self.frame += self.default_color + " " * (self.field_width + 2) + self.default_color + "\n"

        self.rendered_frame = self.frame

    def draw_windows(self, objects):
        self.frame = ""
        if self.border:
            self.frame += self.default_symbol * (self.field_width + 2) + "\n"
        else:
            self.frame += " " * (self.field_width + 2) + "\n"
        for i in range(self.field_height):
            spacer = [" "] * self.field_width
            draw = self.default_symbol
            for j in range(self.field_width):
                for obj in objects:
                    if obj[0] == j and obj[1] == i:
                        spacer[j] = obj[2]
            for space in spacer:
                draw += space
            draw += self.default_symbol
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
        if get_platform() == "Windows":
            self.draw_windows(self.objectsList)
        else:
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


    def Stop(self):
        self.eventloop.stop()

    def __str__(self):
        return "Screen Object"

    def destroy(self):
        self.FunctionManager.Destroy()
        self = None
