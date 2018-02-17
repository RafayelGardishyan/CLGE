import sys
import os
import coverage
import mouse
import keyboard


def blockPrint():
    sys.stdout = open(os.devnull, 'w')


def enablePrint():
    sys.stdout = sys.__stdout__

class Testing:
    testCount = 0
    passedTestCount = 0
    not_passed = []
    exceptions = []
    key = ""

    def __init__(self, testing_rounds):
        self.times = testing_rounds
    # Code Coverage is an experimental function
    def CoverageStart(self):
        print("WARNING: Code Coverage is an experimental function. It does not work good.")
        print("WARNING: Use it on your own risk\n")
        self.cov = coverage.Coverage()
        self.cov.start()

    def CoverageStop(self):
        self.cov.stop()
        self.cov.save()

    def getCoverage(self):
        print("\nCoverage:\n")
        self.cov.report()
        print("\n")

    def Test(self, function, *args, **kwargs):
        for t in range(self.times):
            print("Testing round: {}".format(t + 1))
            self.testCount += 1
            print("INFO: Testing: \"" + function.__name__ + "\"")
            blockPrint()
            try:
                function(*args, **kwargs)
                enablePrint()
                print("INFO: Test \"" + function.__name__ + "\" passed\n\n")
                self.passedTestCount += 1
            except Exception as e:
                self.not_passed.append(function.__name__)
                self.exceptions.append(str(e))
                enablePrint()
                print("WARNING: Test \"" + function.__name__ +"\" is not passed")
                print("ERROR: " + str(e) + "\n\n")

    def printTestResults(self):
        percent = int(self.passedTestCount * 100 / self.testCount)
        print("{}% of test are passed ({} / {})".format(percent, self.passedTestCount, self.testCount))
        if len(self.not_passed) > 0:
            print("Not passed:")
            for test in range(len(self.not_passed)):
                print("{}: {} --> {}".format(test + 1, self.not_passed[test], self.exceptions[test]))

    def simulate_keyboard_press(self, char):
        enablePrint()
        self.key = char
        print("Pressed: {}".format(self.key))
        blockPrint()
        keyboard.press(self.key)

    def simulate_keyboard_release(self, char):
        enablePrint()
        self.key = char
        print("Released: {}".format(self.key))
        blockPrint()
        keyboard.release(self.key)

    def simulate_mouse_press(self, button):
        enablePrint()
        self.key = button
        print("Pressed Mouse Button: {}".format(self.key))
        blockPrint()
        mouse.press(self.key)

    def simulate_mouse_release(self, button):
        enablePrint()
        self.key = button
        print("Released Mouse Button: {}".format(self.key))
        blockPrint()
        mouse.release(self.key)
