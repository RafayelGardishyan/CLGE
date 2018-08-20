from clge.Behaviour.Components.Transform2D import Transform2D
from clge.Constants import TRANSFORM2D_MV_POS


class Behaviour:

    def __init__(self, name, screen, world):
        # Components
        self.components = []
        self.disabledComponents = []

        # Children
        self.children = []
        self.name = name
        self.screen = screen
        self.screen.FunctionManager.registerLateUpdate(self.LateUpdate)
        x = Transform2D()
        x.customInit(0, 0, 1, 1)
        self.components.append(x)
        world.addChild(self)
        self.world = world

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
        c.world = self.world
        c.transform2d = self.getComponentByType("transform2d")
        self.components.append(c)

        if hasattr(c, "Start"):
            self.screen.FunctionManager.registerStart(c)
        if hasattr(c, "Update"):
            self.screen.FunctionManager.registerUpdate(c)
        if hasattr(c, "FixedUpdate"):
            self.screen.FunctionManager.registerFixedUpdate(c)
        if hasattr(c, "PreUpdate"):
            self.screen.FunctionManager.registerPreUpdate(c)
        if hasattr(c, "LateUpdate"):
            self.screen.FunctionManager.registerLateUpdate(c)
        if hasattr(c, "Destroy"):
            self.screen.FunctionManager.registerDestroy(c)

        if hasattr(component, "customInit"):
            c.customInit(kwargs)


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

    def __del__(self):
        self.world.children.pop(self.world.children.index(self))
