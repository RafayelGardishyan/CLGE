from clge import Screen

def open_screen(width, height, symbol, timeout, auto_timeout, auto_clear, color):
    return Screen(width=width, height=height, symbol=symbol, timeout=timeout, auto_clear_objects_list=auto_clear, auto_timeout=auto_timeout, default_color=color)
