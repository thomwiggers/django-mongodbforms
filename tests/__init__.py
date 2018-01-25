import unittest


from django.conf import settings


def suite():
    settings.configure()
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    from . import test_document, test_lazywrapper, test_recursive_reference
    for test in [test_document, test_lazywrapper, test_recursive_reference]:
        suite.addTest(loader.loadTestsFromModule(test))
    return suite
