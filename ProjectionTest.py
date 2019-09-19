from clge.Behaviour import Vector3, Vector2, World
from clge.Behaviour.Components.ThreeDimensions.AsciiRenderer3D import AsciiRenderer3D
from clge.Behaviour.Components.ThreeDimensions.Mesh3D import Mesh3D
from clge.Behaviour.Components.ThreeDimensions.Transform3D import Transform3D
from clge.Constants import CoordinateSystems
from clge.GameMath import Matrix
from clge import AltScreen
from clge.Behaviour.Behaviour import Behaviour

w = 100
h = w / 2

scr = AltScreen(int(w), int(h), True)
scr.auto_clear_objects_list_setter(True)
scr.change_coordinate_system(CoordinateSystems.MIDDLE_MIDDLE)
scr.set_timeout(.05)

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
        # p = Matrix.project(r, aspect, field_of_view, near_plane, far_plane)
        p = Matrix.project(r, 100, 1.5)
        projected.append(p)

    for i in range(4):
        scr.add_line(
            projected[i].x * 2,
            projected[(i+1) % 4].x * 2,
            projected[i].y,
            projected[(i+1) % 4].y,
            "*"
        )
        scr.add_line(
            projected[i + 4].x * 2,
            projected[((i + 1) % 4) + 4].x * 2,
            projected[i + 4].y,
            projected[((i + 1) % 4) + 4].y,
            "*"
        )
        scr.add_line(
            projected[i].x * 2,
            projected[i + 4].x * 2,
            projected[i].y,
            projected[i + 4].y,
            "*"
        )

    for j in projected:
        scr.add_object(j.x * 2, j.y, "O")

    angle += .05

scr.FunctionManager.registerUpdate(update)

scr.Start()
