from clge.Behaviour.Components.Transform2d import Transform2D
from clge.Constants import TRANSFORM2D_MV_POS


class Behaviour:

    # Components
    components = []
    disabledComponents = []

    # Children
    children = []

    def __init__(self, name, screen):
        self.name = name
        self.screen = screen
        self.screen.FunctionManager.registerLateUpdate(self.Update)
        self.addComponent(Transform2D, x=0, y=0, width=1, height=1)

    def addChild(self, child):
        self.children.append(child)

    def getChildByName(self, name):
        for child in self.children:
            if child.name == name:
                return name
        return None

    def addComponent(self, component, **kwargs):
        c = component()
        c.screen = self.screen
        c.parent = self
        c.transform2d = self.getComponentByType("transform2d")
        self.components.append(c)

        if hasattr(component, "Start"):
            self.screen.FunctionManager.registerStart(component.Start)
        if hasattr(component, "Update"):
            self.screen.FunctionManager.registerUpdate(component.Update)
        if hasattr(component, "PreUpdate"):
            self.screen.FunctionManager.registerPreUpdate(component.PreUpdate)
        if hasattr(component, "LateUpdate"):
            self.screen.FunctionManager.registerLateUpdate(component.LateUpdate)
        if hasattr(component, "Destroy"):
            self.screen.FunctionManager.registerDestroy(component.Destroy)

        if component.customInit:
            component.customInit(kwargs)


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

    def LateUpdate(self):
        offset = self.getComponentByType("transform2d").getPosition()
        for child in self.children:
            child.getComponentByType("transform2d").changePositionBy(TRANSFORM2D_MV_POS, offset.x, offset.y)
