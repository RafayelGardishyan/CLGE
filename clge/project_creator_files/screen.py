from clge import Screen


def open_screen(width, height, symbol, timeout, auto_timeout, auto_clear, color):
    scr = Screen(width, height, symbol, True)
    scr.set_timeout(timeout)
    scr.auto_timeout_setter(auto_timeout)
    scr.auto_clear_objects_list_setter(auto_clear)
    scr.color_setter(color)
    return scr
