import time

from .drawer import Screen

offset = 4


scr = Screen(20, 10, False, "*")

scr.auto_clear_objects_list_setter(True)

for i in range(offset + 1):
    scr.add_polygon(12, 5, 4, 1, u'\u2593')
    scr.add_polygon(10, 5, 5, 1, u'\u2591')
    scr.add_polygon(8, 3, 6, 2, u'\u2592')

    scr.add_string(8, 3, "CLGE")

    scr.add_string(5, 7 + offset - i, "MADE")
    scr.add_string(11, 7 + offset - i, "WITH")
    scr.add_string(8, 8 + offset - i, "CLGE")

    scr.render()

time.sleep(5)

scr = None
