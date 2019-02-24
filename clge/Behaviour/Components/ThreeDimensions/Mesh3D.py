from clge.Behaviour import Vector3


class Mesh3D:
    def __init__(self):
        self.my_type = "mesh"
        self.points = [
            Vector3(-10, -10, -10),
            Vector3(10, -10, -10),
            Vector3(10, 10, -10),
            Vector3(-10, 10, -10),
            Vector3(-10, -10, 10),
            Vector3(10, -10, 10),
            Vector3(10, 10, 10),
            Vector3(-10, 10, 10),
        ]

        self.scaling_factor = 1

        self.connecting_sequence = [
            (0, 4), (1, 5), (2, 6), (3, 7),
            (0, 1), (1, 2), (2, 3), (3, 0),
            (4, 5), (5, 6), (6, 7), (7, 4),
        ]

    def setScalingFactor(self, factor):
        self.scaling_factor = factor
        for i in range(len(self.points)):
            p = self.points[i]
            self.points[i] = Vector3(p.x * self.scaling_factor, p.y * self.scaling_factor, p.z * self.scaling_factor)

    def setPoints(self, points):
        self.setScalingFactor(self.scaling_factor)
        self.points = points

    def setSequence(self, sequence):
        self.connecting_sequence = sequence

    def setData(self, points, sequence):
        self.setPoints(points)
        self.setSequence(sequence)

    def getPoints(self):
        return self.points

    def getSequence(self):
        return self.connecting_sequence

    def readFromObjFile(self, filename):
        self.points = []
        self.connecting_sequence = []
        f = open(filename, "r")
        content = f.readlines()
        f.close()
        content = [x.strip() for x in content]
        content = [x.split() for x in content]
        for i in content:
            if i[0] == "v":
                self.points.append(Vector3(i[1], i[2], i[3]))
            if i[0] == "f":
                p = []
                for j in i:
                    p.append(j.split("/"))

                for k in range(1, len(p)):
                    if k == len(p) - 1:
                        self.connecting_sequence.append((int(p[k][0]) - 1, int(p[1][0]) - 1))
                    else:
                        self.connecting_sequence.append((int(p[k][0]) - 1, int(p[k + 1][0]) - 1))
        self.setScalingFactor(self.scaling_factor)
