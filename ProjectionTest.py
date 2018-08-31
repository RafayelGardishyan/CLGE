from clge.Behaviour import Vector3, Vector2
from clge.Constants import CoordinateSystems
from clge.GameMath import Matrix
from clge import AltScreen

w = 200
h = w / 2

aspect = w / h
field_of_view = 10

scr = AltScreen(200, 100, True)
scr.auto_clear_objects_list_setter(True)
scr.change_coordinate_system(CoordinateSystems.MIDDLE_MIDDLE)
scr.set_timeout(.1)

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
        r = Matrix.rotate_x(i, angle)
        r = Matrix.rotate_y(r, angle)
        r = Matrix.rotate_z(r, angle)
        p = Matrix.project(r, aspect, field_of_view, 1, 100)
        projected.append(p)

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

    for j in projected:
        scr.add_object(j.x, j.y, "O")

    angle += .05

scr.FunctionManager.registerUpdate(update)

scr.Start()
