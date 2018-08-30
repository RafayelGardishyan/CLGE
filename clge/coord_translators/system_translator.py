"""
@package docstring
Coordinate system translator
"""

"""
Coordinate system list
"""
cmodes = ['std', 'lt', 'lm', 'lb', 'mt', 'mm', 'mb', 'rt', 'rm', 'rb']

def to_std(x, y, height, width, Sfrom):
    """
    Function which translates Sfrom corner coordinate system coordinates to Left-Upper corner system
    Width and Height of game field required

    :param x: input X
    :param y: input Y
    :param height: field height
    :param width: field width
    :param Sfrom: output coordinate system
    :return: (output X, output Y)
    """
    if Sfrom not in cmodes:
        raise Exception("Error: Not existing coordinate mode")
    if Sfrom == "lb":
        return x, height + y
    if Sfrom == "lm":
        return x, int(height / 2) - y
    if Sfrom == "mt":
        return int(x + (width / 2)), y
    if Sfrom == "mm":
        return int(x + (width / 2)), int(height / 2) - y
    if Sfrom == "mb":
        return int(x + (width / 2)), height + y
    if Sfrom == "rt":
        return width + x, y
    if Sfrom == "rm":
        return width + x, int(height / 2) - y
    if Sfrom == "rb":
        return width + x, height + y
    if Sfrom == "std":
        return x, y

def from_std(x, y, height, width, Sto):
    """
    Function which translates Left-Upper corner coordinate system coordinates to Sto coordinate system
    Width and Height of game field required

    :param x: input X
    :param y: input Y
    :param height: field height
    :param width: field width
    :param Sto: output coordinate system
    :return: (output X, output Y)
    """
    if Sto == "lb":
        return x, height - y
    if Sto == "lm":
        return x, int(height / 2) + y
    if Sto == "mt":
        return int(x - (width / 2)), y
    if Sto == "mm":
        return int(x - (width / 2)), int(height / 2) + y
    if Sto == "mb":
        return int(x - (width / 2)), height - y
    if Sto == "rt":
        return width - x, y
    if Sto == "rm":
        return width - x, int(height / 2) + y
    if Sto == "rb":
        return width - x, height - y
    if Sto == "std":
        return x, y

def translate_coord_system(x, y, height, width, Sfrom="std", Sto="std"):
    """
    Function which translates coordinates to another coordinate system
    Width and Height of game field required

    :param x: input X coordinate
    :param y: input Y coordinate
    :param height: field height
    :param width: field width
    :param Sfrom: input coordinate system
    :param Sto: output coordinate system
    :return: (output X, output Y)
    """
    if (Sfrom not in cmodes) or (Sto not in cmodes):
        raise Exception("Error: Not existing coordinate mode")
    if Sfrom == Sto:
        return x, y

    if (Sfrom == "std") or (Sfrom == "lt"):
        return from_std(x, y, height, width, Sto)

    if (Sto == "sdt") or (Sto == "lt"):
        return to_std(x, y, height, width, Sfrom)

    xt, yt = to_std(x, y, height, width, Sfrom)
    return from_std(xt, yt, height, width, Sto)
