import unittest
from domain.movie import Movie


class MovieTest(unittest.TestCase):

    def test_Movie(self):
        movie_ID = 3
        movie_title = "Terminator"
        movie_release = 1986
        movie_price = 15
        movie_inSchedule = True
        m1 = Movie(movie_ID, movie_title, movie_release, movie_price,
                   movie_inSchedule)
        assert m1.getID() == movie_ID
        assert m1.getTitle() == movie_title
        assert m1.getPrice() == movie_price
        assert m1.getRelease() == movie_release
        assert m1.getInSchedule() == movie_inSchedule