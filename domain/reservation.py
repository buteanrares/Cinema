class Reservation:

    """Represents a client reservation
    """

    def __init__(self, ID, movie_ID, clientcard_ID, date, time):
        """Parameterized constructor
            Attributes are self-explanatory
        """
        self.ID = ID
        self.movie_ID = movie_ID
        self.clientcard_ID = clientcard_ID
        self.date = date
        self.time = time

    def __str__(self):
        """String overloader for a reservation object

        :return: String representing reservation data
        :rtype: String
        """
        return "{}, {}, {}, {}, {}".format(self.ID, self.movie_ID,
                                           self.clientcard_ID, self.date,
                                           self.time)

    def __eq__(self, other):
        """Reservation objects '==' comparator

        :param other: reservation object 
        :type other: Reservation
        :return: true if they are the same entity ; false otherwise
        :rtype: bool
        """
        if not isinstance(other, Reservation):
            return False
        return self.ID == other.ID and self.movie_ID == other.movie_ID and self.clientcard_ID == other and \
            self.date == other.date and self.time == other.time

    def __ne__(self, other):
        """reservation objects '!=' comparator
           Opposite of __eq__
        """
        return not self == other

    #
    # Getters
    #

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

    #
    #