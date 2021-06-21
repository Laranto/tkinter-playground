from typing import *
import unittest
import sys
import os

class ManualTestProgram(unittest.TestProgram):
    def __init__(self, module='__main__', defaultTest=None, argv=None,
                    testRunner=None, testLoader=unittest.defaultTestLoader,
                    exit=True, verbosity=1, failfast=None, catchbreak=None,
                    buffer=None, warnings=None, *, tb_locals=False):
        # We can not inherit from it, because the init runs it
        # super().__init__(module=module, defaultTest=defaultTest, argv=argv, testRunner=testRunner, testLoader=testLoader, exit=exit, verbosity=verbosity, failfast=failfast, catchbreak=catchbreak, buffer=buffer, warnings=warnings, tb_locals=tb_locals)
        self.exit = exit
        self.failfast = failfast
        self.catchbreak = catchbreak
        self.verbosity = verbosity
        self.buffer = buffer
        self.tb_locals = tb_locals
        if warnings is None and not sys.warnoptions:
            # even if DeprecationWarnings are ignored by default
            # print them anyway unless other warnings settings are
            # specified by the warnings arg or the -W python flag
            self.warnings = 'default'
        else:
            # here self.warnings is set either to the value passed
            # to the warnings args or to None.
            # If the user didn't pass a value self.warnings will
            # be None. This means that the behavior is unchanged
            # and depends on the values passed to -W.
            self.warnings = warnings
        self.defaultTest = defaultTest
        self.testRunner = testRunner
        self.testLoader = testLoader
        # Discovery options
        self.start = "src"
        self.pattern = 'test*.py'
        self.top = None

if __name__ == '__main__':
    tp = ManualTestProgram()
    tp.createTests(from_discovery=True)
    tp.runTests()