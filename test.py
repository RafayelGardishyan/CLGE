from engine import Screen

screenObj = Screen(41, 21, auto_clear_objects_list=False, auto_timeout=False)

x = 21
y = 11

while True:
    screenObj.add_object(x, y, '@')
    screenObj.render()
    d = input("Choose movement direction: ")
    if d == "u":
        y -= 1
    if d == "d":
        y += 1
    if d == "r":
        x += 1
    if d == "l":
        x -= 1
    if d == "`":
        raise SystemExit
    screenObj.clear_screen()

