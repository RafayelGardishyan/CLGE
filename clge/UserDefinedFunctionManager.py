class UserDefinedFunctionManager:
    def __init__(self):
        self.StartCalled = False

    def Update(self):
        pass

    def fStart(self):
        pass

    def Start(self):
        if not self.StartCalled:
            self.fStart()
            self.StartCalled = True

    def LateUpdate(self):
        pass

    def PreUpdate(self):
        pass

    def Destroy(self):
        pass

    def registerUpdate(self, function):
        self.Update = function

    def registerStart(self, function):
        self.fStart = function

    def registerLateUpdate(self, function):
        self.LateUpdate = function

    def registerPreUpdate(self, function):
        self.PreUpdate = function

    def registerDestroy(self, function):
        self.Destroy = function