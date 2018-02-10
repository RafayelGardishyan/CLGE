import sys
import os
import coverage

class Testing:
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
        print("INFO: Testing: \"" + function.__name__ + "\"")
        self.blockPrint()
        try:
            function(*args, **kwargs)
            self.enablePrint()
            print("INFO: Testing \"" + function.__name__ + "\" passed\n\n")
        except Exception as e:
            self.enablePrint()
            print("INFO: Testing \"" + function.__name__ +"\" is not passed\n")
            print("ERROR: " + str(e) + "\n\n")

    def blockPrint(self):
        sys.stdout = open(os.devnull, 'w')

    def enablePrint(self):
        sys.stdout = sys.__stdout__