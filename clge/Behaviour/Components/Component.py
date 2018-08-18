from clge.Behaviour import Behaviour, Transform2D
from clge.drawer import Screen


class Component:
    my_type: str
    screen: Screen
    parent: Behaviour
    transform2d: Transform2D

