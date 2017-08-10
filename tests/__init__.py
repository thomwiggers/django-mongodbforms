import unittest

from . import test_document, test_lazywrapper, test_recursive_reference


def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    for test in [test_document, test_lazywrapper, test_recursive_reference]:
        suite.addTest(loader.loadTestsFromModule(test))
    return suite
