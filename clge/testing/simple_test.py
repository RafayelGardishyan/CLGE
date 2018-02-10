import sys
import os
import coverage
import keyboard

class Testing:
    testCount = 0
    passedTestCount = 0
    not_passed = []
    # Code Coverage is an expoerimental function
    def CoverageStart(self):
        print("INFO: Code Coverage is an experimental function. It does not work good.")
        print("INFO: Use it on your own risk")
        self.cov = coverage.Coverage()
        self.cov.start()

    def CoverageStop(self):
        self.cov.stop()
        self.cov.save()

    def getCoverage(self):
        self.cov.report()
        print("\n")

    def Test(self, function, *args, **kwargs):
        self.testCount += 1
        print("INFO: Testing: \"" + function.__name__ + "\"")
        self.blockPrint()
        try:
            function(*args, **kwargs)
            self.enablePrint()
            print("INFO: Testing \"" + function.__name__ + "\" passed\n\n")
            self.passedTestCount += 1
        except Exception as e:
            self.not_passed.append(function.__name__)
            self.enablePrint()
            print("WARNING: Test \"" + function.__name__ +"\" is not passed")
            print("ERROR: " + str(e) + "\n\n")

    def blockPrint(self):
        sys.stdout = open(os.devnull, 'w')

    def enablePrint(self):
        sys.stdout = sys.__stdout__

    def printTestResults(self):
        percent = int(self.passedTestCount * 100 / self.testCount)
        print("{} percent of test are passed ({} / {})".format(percent, self.passedTestCount, self.testCount))
        print("Not passed:")
        for test in self.not_passed:
            print("{}: {}".format(self.not_passed.index(test) + 1, test))

    def simulate_keyboard_press(self, char):
        keyboard.press(char)

    def simulate_keyboard_release(self, char):
        keyboard.release(char)