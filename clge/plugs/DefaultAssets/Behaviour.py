from .Transform2d import Transform2D


class Behaviour:
    components = [Transform2D(0, 0, 1, 1)]

    def addComponent(self, component):
        self.components.append(component)

    def getComponent(self, component_type):
        for component in self.components:
            if component.my_type == component_type:
                return component

        return None

    def checkCollision(self, other):
        self.getComponent("collider2d").checkCollision(other)
