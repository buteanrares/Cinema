class Movie:
    """
    Represents a movie.
    """
    moviesIdList = []

    def __init__(self, ID, title, release, price, inSchedule):
        """
        Creates a movie with:
        :param ID: (int)
        :param title: (str)
        :param release: (int > 0)
        :param price: (int > 0)
        :param inSchedule: (bool)
        """
        self.ID = ID
        self.title = title
        self.release = release
        self.price = price
        if inSchedule is True:
            self.inSchedule = True
        else:
            self.inSchedule = False
        Movie.moviesIdList.append(self.ID)

    def __str__(self):
        return "{}, {}, {}, {}, {}".format(
            self.ID,
            self.title,
            self.release,
            self.price,
            self.inSchedule
        )

    def __eq__(self, other):
        if not isinstance(other, Movie):
            raise TypeError("other is not type Movie")
        return self.ID == other.ID

    def __ne__(self, other):
        return not self == other

    def getID(self):
        return self.ID

    def getTitle(self):
        return self.title

    def getRelease(self):
        return self.release

    def getPrice(self):
        return self.price

    def getInSchedule(self):
        return self.inSchedule
