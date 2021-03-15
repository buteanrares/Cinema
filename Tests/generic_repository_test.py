import unittest

from domain.movie import Movie
from repository.generic_repository import GenericFileRepository


class GenericRepositoryTest(unittest.TestCase):

    def test_create(self):
        filename = "test.pickle"
        generic_repository = GenericFileRepository(filename)
        movie = Movie(1, "test", 2000, 10, True)
        generic_repository.create(movie)
        storage = generic_repository.read()
        self.assertEqual(len(storage), 1)
        generic_repository.delete(1)

    def test_update(self):
        filename = "test.pickle"
        generic_repository = GenericFileRepository(filename)
        movie = Movie(1, "test", 2000, 10, True)
        generic_repository.create(movie)
        movie_to_update = Movie(1, "test", 2000, 10, False)
        generic_repository.update(movie_to_update)
        obj = generic_repository.read(1)
        self.assertEqual(obj.getInSchedule(), False)
        generic_repository.delete(1)
