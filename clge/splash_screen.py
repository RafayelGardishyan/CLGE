import time

from .drawer import Screen


scr = Screen(20, 10, False, "*")

scr.add_polygon(12, 5, 4, 1, u'\u2593')
scr.add_polygon(10, 5, 5, 1, u'\u2591')
scr.add_polygon(8, 3, 6, 2, u'\u2592')

scr.add_string(8, 3, "CLGE")


scr.add_string(5, 7, "MADE")
scr.add_string(11, 7, "WITH")
scr.add_string(8, 8, "CLGE")

scr.render()

time.sleep(5)

scr = None
