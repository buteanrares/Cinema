import unittest

from Tests.generic_repository_test import GenericRepositoryTest
#from Tests.generic_repository_test import GenericRepositoryTest
from Tests.movie_test import MovieTest
from Tests.reservation_test import ReservationTest
from Tests.clientcard_test import ClientcardTest


def run_tests():
    print("\n#\n# RUNNING TESTS\n#\n")
    loader = unittest.defaultTestLoader
    all_suites =\
         [
        loader.loadTestsFromTestCase(MovieTest),
        loader.loadTestsFromTestCase(ReservationTest),
        loader.loadTestsFromTestCase(ClientcardTest),
        loader.loadTestsFromTestCase(GenericRepositoryTest)
    ]
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(unittest.TestSuite(all_suites))
    print("\n#\n#\n#")


if __name__ == '__main__':
    run_tests()
