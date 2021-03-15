class Reservation:

    def __init__(self, ID, movie_ID, clientcard_ID, date, time):
        self.ID = ID
        self.movie_ID = movie_ID
        self.clientcard_ID = clientcard_ID
        self.date = date
        self.time = time

    def __str__(self):
        return "{}, {}, {}, {}, {}".format(self.ID, self.movie_ID, self.clientcard_ID, self.date, self.time)

    def __eq__(self, other):
        if not isinstance(other, Reservation):
            return False
        return self.ID == other.ID and self.movie_ID == other.movie_ID and self.clientcard_ID == other and \
            self.date == other.date and self.time == other.time

    def __ne__(self, other):
        return not self == other

    def getID(self):
        return self.ID

    def getMovieID(self):
        return self.movie_ID

    def getClientcardID(self):
        return self.clientcard_ID

    def getDate(self):
        return self.date

    def getTime(self):
        return self.time

