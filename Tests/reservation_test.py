import unittest
from domain.reservation import Reservation


class ReservationTest(unittest.TestCase):
    # Reservations test case

    def test_Reservation(self):
        id = 1
        movie_id = 3
        clientcard_id = 7
        date = "15/7/2019"
        time = "20:30"
        test = Reservation(id, movie_id, clientcard_id, date, time)
        assert test.getID() == id
        assert test.getMovieID() == movie_id
        assert test.getClientcardID() == clientcard_id
        assert test.getDate() == date
        assert test.getTime() == time
