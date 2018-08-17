from clge.Behaviour.Components.Transform2d import Transform2D


class Behaviour:
    components = [Transform2D(0, 0, 1, 1)]
    disabledComponents = []

    def addComponent(self, component):
        self.components.append(component)

    def getComponentByType(self, component_type):
        for component in self.components:
            if component.my_type == component_type:
                return component
        return None

    def getComponentsByType(self, component_type):
        components = []
        for component in self.components:
            if component.my_type == component_type:
                components.append(component)
        return components

    def disableComponent(self, component_type):
        for component in self.components:
            if component.my_type == component_type:
                self.disabledComponents.append(self.components.pop(self.components.index(component)))

    def enableComponent(self, component_type):
        for component in self.disabledComponents:
            if component.my_type == component_type:
                self.components.append(self.disabledComponents.pop(self.disabledComponents.index(component)))

    def checkCollision(self, other):
        if self.getComponentByType("collider2d"):
            self.getComponentByType("collider2d").checkCollision(other)
