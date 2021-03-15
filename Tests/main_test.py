import unittest


from Tests.generic_repository_test import GenericRepositoryTest
from Tests.movie_test import test_Movie
from Tests.reservation_test import test_Reservation
from Tests.clientcard_test import test_Clientcard


def run_tests():
    loader = unittest.defaultTestLoader
    all_suites = \
        [loader.loadTestsFromTestCase(test_Movie),
         loader.loadTestsFromTestCase(test_Reservation),
         loader.loadTestsFromTestCase(test_Clientcard),
         loader.loadTestsFromTestCase(GenericRepositoryTest)
         ]
    runner = unittest.TextTestRunner(verbosity=0)
    runner.run(unittest.TestSuite(all_suites))


if __name__ == '__main__':
    run_tests()
