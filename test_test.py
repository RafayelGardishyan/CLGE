from clge import Tester
t = Tester()

def run(A):
    print(A)

def runNoError():
    print("Testing")

def runNoErrorB(aa):
    print(aa)

t.Test(run, run.__name__)
t.Test(runNoError)
t.Test(runNoErrorB, "Tello")
