from colored import fg, bg, attr

def paint_text(text, foreground=2, background=5, reset=True):
    if reset:
        return "{} {} {} {}".format(fg(foreground), bg(background), text, attr(0))
    else:
        return "{} {} {}".format(fg(foreground), bg(background), text)
