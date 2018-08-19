from clge.Behaviour.Vector2 import Vector2
from clge.Constants import TRANSFORM2D_MV_POS


class Physiqs:
    def __init__(self):
        self.gravity = 2.0
        self.mass = 1.0
        self.gravityFrame = 1
        self.gravityForce = Vector2(0, self.GetGravityForce())
        self.forces = []
        self.forceDecreasing = []
        self.frame = Vector2(0, 0)
        self.my_type = "physiqs"

    def changeData(self, ngravity, nmass):
        self.gravity = ngravity
        self.mass = nmass
        self.gravityForce = self.GetGravityForce()

    def addForce(self, vector2, influence):
        self.forces.append(vector2)
        self.forceDecreasing.append((self.mass * self.gravity / 2) * (self.mass ** self.gravity / influence))

    def appendForces(self):
        del_indexes = []

        self.frame = Vector2(0, self.GetGravityForce() * self.screen.deltaTime)
        for i in range(len(self.forces)):
            self.frame += Vector2(self.forces[i].x * self.screen.deltaTime, self.forces[i].y * self.screen.deltaTime)
            self.forces[i] -= Vector2(self.forceDecreasing[i], self.forceDecreasing[i])
            self.forceDecreasing[i] += self.forceDecreasing[i] * .2 - self.mass * .2

            if self.forces[i].x < 0:
                self.forces[i].x = 0

            if self.forces[i].y < 0:
                self.forces[i].y = 0

            if self.forces[i].x <= 0 and self.forces[i].y <= 0:
                del_indexes.append(i)

        for i in del_indexes:
            self.forceDecreasing.pop(i)
            self.forces.pop(i)
            for j in range(len(del_indexes)):
                if del_indexes[j] > i:
                    del_indexes[j] -= 1

    def GetGravityForce(self):
        return self.gravity * self.gravityFrame * self.mass / 2

    def Update(self):
        self.appendForces()
        self.transform2d.changePositionBy(TRANSFORM2D_MV_POS, self.frame.x, self.frame.y)
        self.checkReset()
        self.updateGravityFrame()

    def updateGravityFrame(self):
        self.gravityFrame += 1 * self.screen.deltaTime

    def clampGravityFrame(self):
        self.gravityFrame = max(min(self.gravityFrame, 1), 3)

    def checkReset(self):
        if self.transform2d.blockMovement["down"]:
            self.gravityFrame = 1
