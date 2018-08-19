class World:
    def __init__(self):
        self.children = []

    def addChild(self, child):
        child.world = self
        self.children.append(child)

    def getChildByName(self, name):
        for child in self.children:
            if child.name == name:
                return name
        return None

    def getAllChildren(self):
        return self.children
