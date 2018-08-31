from clge.Behaviour import Vector3, Vector2
from clge.Constants import CoordinateSystems
from clge.GameMath import Matrix
from clge import AltScreen

w = 100
h = w / 2

aspect = w / h
field_of_view = 60
near_plane = 10
far_plane = 60

scr = AltScreen(int(w), int(h), True)
scr.auto_clear_objects_list_setter(True)
scr.change_coordinate_system(CoordinateSystems.MIDDLE_MIDDLE)
scr.set_timeout(.1)

angle = 0

points = [
    Vector3(-10, -10, -10),
    Vector3(10, -10, -10),
    Vector3(10, 10, -10),
    Vector3(-10, 10, -10),
    Vector3(-10, -10, 10),
    Vector3(10, -10, 10),
    Vector3(10, 10, 10),
    Vector3(-10, 10, 10),
]


def update():
    global angle
    projected: list[Vector2] = []
    for i in points:
        r = Matrix.rotate_x(i, angle)
        r = Matrix.rotate_y(r, angle)
        r = Matrix.rotate_z(r, angle)
        p = Matrix.project(r, aspect, field_of_view, near_plane, far_plane)
        projected.append(p)

    for i in range(4):
        scr.add_line(
            projected[i].x * 2,
            projected[(i+1) % 4].x * 2,
            projected[i].y,
            projected[(i+1) % 4].y,
            "O"
        )
        scr.add_line(
            projected[i + 4].x * 2,
            projected[((i + 1) % 4) + 4].x * 2,
            projected[i + 4].y,
            projected[((i + 1) % 4) + 4].y,
            "O"
        )
        scr.add_line(
            projected[i].x * 2,
            projected[i + 4].x * 2,
            projected[i].y,
            projected[i + 4].y,
            "O"
        )

    for j in projected:
        scr.add_object(j.x * 2, j.y, "O")

    angle += .05


scr.FunctionManager.registerUpdate(update)

scr.Start()
