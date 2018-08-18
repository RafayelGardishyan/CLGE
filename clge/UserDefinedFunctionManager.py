class Functions:
    def __init__(self):
        self.StartCalled = False

    update = []

    start = []

    lateupdate = []

    preupdate = []

    destroy = []

    def Start(self):
        if not self.StartCalled:
            for i in self.start:
                i()
            self.StartCalled = True

    def Update(self):
        for i in self.update:
            i()

    def LateUpdate(self):
        for i in self.lateupdate:
            i()

    def PreUpdate(self):
        for i in self.preupdate:
            i()

    def Destroy(self):
        for i in self.destroy:
            i()

    def registerUpdate(self, function):
        self.update.append(function)

    def registerStart(self, function):
        self.start.append(function)

    def registerLateUpdate(self, function):
        self.lateupdate.append(function)

    def registerPreUpdate(self, function):
        self.preupdate.append(function)

    def registerDestroy(self, function):
        self.destroy.append(function)