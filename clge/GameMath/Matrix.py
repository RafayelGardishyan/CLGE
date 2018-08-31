import math

from clge.Behaviour import Vector2
from clge.Behaviour import Vector3


def matmult(a,b):
    zip_b = zip(*b)
    zip_b = list(zip_b)
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b))
             for col_b in zip_b] for row_a in a]

def deg_to_rad(fov):
    return 2.0 * math.pi * fov / 360


def project(point: Vector3, aspect, fov, near, far) -> Vector2:
    perspective_matrix = [
        [1/(aspect * math.tan(deg_to_rad(fov / 2))), 0, 0, 0],
        [0, 1/(math.tan(deg_to_rad(fov / 2))), 0, 0],
        [0, 0, - ((far + near) / (far - near)), -((2 * far * near) / far - near)],
        [0, 0, -1, 0]
    ]

    # perspective_point = matmult(perspective_matrix, [[point.x], [point.y], [point.z], [1]])
    # perspective_point.pop()
    coefficient = 1
    projection_matrix = [
        [coefficient, 0, 0],
        [0, coefficient, 0]
    ]
    m = matmult(projection_matrix, [[point.x], [point.y], [point.z]])
    # m = matmult(projection_matrix, perspective_point)
    return Vector2(m[0][0], m[1][0])


def rotate_x(point: Vector3, angle: float) -> Vector3:
    rotation_x = [
        [1, 0, 0],
        [0, math.cos(angle), -math.sin(angle)],
        [0, math.sin(angle), math.cos(angle)]
    ]
    m = matmult(rotation_x, [[point.x], [point.y], [point.z]])
    return Vector3(m[0][0], m[1][0], m[2][0])


def rotate_z(point: Vector3, angle: float) -> Vector3:
    rotation_x = [
        [math.cos(angle), -math.sin(angle), 0],
        [math.sin(angle), math.cos(angle), 0],
        [0, 0, 1]
    ]
    m = matmult(rotation_x, [[point.x], [point.y], [point.z]])
    return Vector3(m[0][0], m[1][0], m[2][0])


def rotate_y(point: Vector3, angle: float) -> Vector3:
    rotation_x = [
        [math.cos(angle), 0, math.sin(angle)],
        [0, 1, 0],
        [-math.sin(angle), 0, math.cos(angle)]
    ]
    m = matmult(rotation_x, [[point.x], [point.y], [point.z]])
    return Vector3(m[0][0], m[1][0], m[2][0])
