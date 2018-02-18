from clge import SimpleTester

t = SimpleTester(5)

t.CoverageStart()


from clge import KeymapGenerator
from clge import Screen
from clge import AltScreen
from clge import paint_text
from clge import convert_to_code
from clge import convert_to_char
from clge import CLGEException
from clge import generate_mousemap
from clge import Utils
from clge import AudioPlayer
from clge import PluginInstaller, UninstallPlugin, GetPlugins
from clge import ProjectCreator



def test_exception():
    raise CLGEException("Testing Exception")


def test_mouse():
    keys = generate_mousemap({
        "l": "left",
        "r": "right",
        "m": "middle"
    })

    for key in keys:
        t.simulate_mouse_press(keys[key].button)
        Utils.sleep(500)
        if keys[key].detect():
            print("Success!")
        else:
            Utils.sleep(500)
            t.simulate_mouse_release(keys[key].button)
            raise CLGEException("Key {} in not detected".format(keys[key].button))
        Utils.sleep(500)
        t.simulate_mouse_release(keys[key].button)
        print(keys[key])


def test_keyboard():
    keys = KeymapGenerator()
    keys.add('up', 'w')
    keys.add('up_arrow', 'up')
    keys.add('down', 's')
    keys.add('down_arrow', 'down')
    keys.add('right', 'd')
    keys.add('right_arrow', 'right')
    keys.add('left', 'a')
    keys.add('left_arrow', 'left')
    keys = keys.generate()
    print(convert_to_code("a"), convert_to_char(15))
    for button in keys:
        t.simulate_keyboard_press(keys[button].char)
        Utils.sleep(500)
        if keys[button].detect():
            print("Success!")
        else:
            t.simulate_keyboard_release(keys[button].char)
            Utils.sleep(500)
            raise CLGEException("Key {} in not detected".format(keys[button].char))
        t.simulate_keyboard_release(keys[button].char)
        Utils.sleep(500)
        print(keys[button])


def test_screen():
    scr = Screen(20, 20)
    scr.auto_clear_objects_list_setter(True)
    scr.set_timeout(.5)
    scr.auto_timeout_setter(True)
    scr.color_setter(39)
    for i in range(20):
        for j in range(20):
            scr.add_object(i, i*j, "I", i)
            scr.add_string(j, j, "Hello", j)
            scr.add_polygon(i, j, j, i, "L", j)
        scr.render()
        scr.clear_screen()
    print(scr)
    scr.do_timeout()

    scr = AltScreen(20, 20)
    scr.auto_clear_objects_list_setter(True)
    scr.set_timeout(.5)
    scr.auto_timeout_setter(True)
    scr.color_setter(39)
    for i in range(20):
        for j in range(20):
            scr.add_object(i, i * j, "I", i)
            scr.add_string(j, j, "Hello", j)
            scr.add_polygon(i, j, j, i, "L", j)
        scr.render()
        scr.clear_screen()
    print(scr)
    scr.do_timeout()


def test_color():
    for i in range(256):
        for j in range(256):
            print(paint_text("Test", i, j, True))
            print(paint_text("Test", j, i, False))


def test_utils():
    Utils.sleep(500)
    Utils.randint(5, 100)
    Utils.randcode(100)
    Utils.randchoice(["Test", 5, 6, Utils, "Me"])


def test_audio():
    p = AudioPlayer("snake_sound/level_up.wav", async=False)
    p.play()


def test_plugins():
    PluginInstaller("SamplePlugin.zip", "SamplePlugin")
    print(GetPlugins())
    UninstallPlugin("SamplePlugin")


def test_project_creator():
    ProjectCreator("Test" + str(Utils.randint(500, 1000)))



t.Test(test_exception)
t.Test(test_mouse)
t.Test(test_screen)
t.Test(test_keyboard)
t.Test(test_color)
t.Test(test_utils)
t.Test(test_audio)
t.Test(test_plugins)
t.Test(test_project_creator)
t.CoverageStop()
t.printTestResults()
t.getCoverage()
