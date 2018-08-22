import asyncio

import time


def functionI():
    pass

class UserDefinedFunctionManager:
    def __init__(self):
        self.update = []

        self.start = []

        self.lateupdate = []

        self.fixedupdate = []

        self.preupdate = []

        self.destroy = []

    def Start(self):
        for i in self.start:
            if type(functionI) == type(i) or type(self.Start) == type(i):
                self.start.pop(self.start.index(i))()
            else:
                self.start.pop(self.start.index(i)).Start()

    def Update(self):
        for i in self.update:
            if type(functionI) == type(i) or type(self.Start) == type(i): i()
            else: i.Update()

    def LateUpdate(self):
        for i in self.lateupdate:
            if type(functionI) == type(i) or type(self.Start) == type(i): i()
            else: i.LateUpdate()

    def PreUpdate(self):
        for i in self.preupdate:
            if type(functionI) == type(i) or type(self.Start) == type(i): i()
            else: i.PreUpdate()

    def Destroy(self):
        for i in self.destroy:
            if type(functionI) == type(i) or type(self.Start) == type(i): i()
            else: i.Destroy()

    async def FixedUpdate(self, timeout):
        for i in self.fixedupdate:
            if type(functionI) == type(i) or type(self.Start) == type(i): i()
            else: i.FixedUpdate()
        time.sleep(timeout)
        asyncio.ensure_future(self.FixedUpdate(timeout))

    def registerUpdate(self, function):
        self.update.append(function)

    def registerStart(self, function):
        self.start.append(function)

    def registerLateUpdate(self, function):
        self.lateupdate.append(function)

    def registerFixedUpdate(self, function):
        self.fixedupdate.append(function)

    def registerPreUpdate(self, function):
        self.preupdate.append(function)

    def registerDestroy(self, function):
        self.destroy.append(function)