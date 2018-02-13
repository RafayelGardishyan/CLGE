from colored import fg, bg, attr
from .setup import get_platform

def paint_text(text, foreground=2, background=5, reset=True):
    if get_platform() != "Windows":
        if reset:
            return "{} {} {} {}".format(fg(foreground), bg(background), text, attr(0))
        else:
            return "{} {} {}".format(fg(foreground), bg(background), text)
    else:
        return text