from clge.Constants import CoordinateSystems
from clge.GameMath import Matrix


class AsciiRenderer3D:

    def __init__(self):
        self.my_type = "asciirenderer3d"
        self.character = "#"
        self.color = 12
        self.coeficient = 1.5

    def editData(self, ncharacter="#", ncolor=12, ndistance=100):
        self.character = ncharacter
        self.color = ncolor
        self.distance = ndistance

    def Start(self):
        self.previous_system = self.screen.coordinate_system

    def Update(self):
        self.screen.change_coordinate_system(CoordinateSystems.MIDDLE_MIDDLE)
        transforminfo = self.parent.getComponentByType('transform3d').getFullInformation()
        mesh = self.parent.getComponentByType("mesh")
        points = mesh.getPoints()
        sequence = mesh.getSequence()
        projected = []
        for point in points:
            npoint = point + transforminfo["vector3"]
            r = Matrix.rotate_x(npoint, transforminfo["rotation"][0])
            r = Matrix.rotate_y(r, transforminfo["rotation"][1])
            r = Matrix.rotate_z(r, transforminfo["rotation"][2])
            p = Matrix.project(r, self.screen.field_height, 1.5)
            projected.append(p)
            self.screen.add_object(p.x * 2, p.y, self.character, self.color)

        for psequence in sequence:
            self.screen.add_line(
                projected[psequence[0]].x,
                projected[psequence[1]].x,
                projected[psequence[0]].y,
                projected[psequence[1]].y,
                self.character,
                self.color
            )

        self.screen.change_coordinate_system(self.previous_system)
