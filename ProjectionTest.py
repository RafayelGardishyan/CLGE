from clge.Behaviour import Vector3, Vector2
from clge.GameMath import Matrix
from clge import AltScreen

scr = AltScreen(200, 100, True)
scr.auto_clear_objects_list_setter(True)
scr.change_coordinate_system("mm")
scr.set_timeout(.5)

angle = 0

points = [
    Vector3(-20, -20, -20),
    Vector3(20, -20, -20),
    Vector3(20, 20, -20),
    Vector3(-20, 20, -20),
    Vector3(-20, -20, 20),
    Vector3(20, -20, 20),
    Vector3(20, 20, 20),
    Vector3(-20, 20, 20),
]


def update():
    global angle
    projected: list[Vector2] = []
    for i in points:
        r = Matrix.rotate_y(i, angle)
        r = Matrix.rotate_z(r, angle)
        r = Matrix.rotate_x(r, angle)
        p = Matrix.project(r)
        projected.append(p)

    for j in projected:
        scr.add_object(j.x, j.y, "O")

    for i in range(4):
        scr.add_line(
            projected[i].x,
            projected[(i+1) % 4].x,
            projected[i].y,
            projected[(i+1) % 4].y,
            "O"
        )
        scr.add_line(
            projected[i + 4].x,
            projected[((i + 1) % 4) + 4].x,
            projected[i + 4].y,
            projected[((i + 1) % 4) + 4].y,
            "O"
        )
        scr.add_line(
            projected[i].x,
            projected[i + 4].x,
            projected[i].y,
            projected[i + 4].y,
            "O"
        )

    angle += .05


scr.FunctionManager.registerUpdate(update)

scr.Start()
