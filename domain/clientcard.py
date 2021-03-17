class Clientcard:

    """
    Represents a client's card.
    """
    clientacardIdList = []

    def __init__(self, ID, lastName, firstName, CNP, birthDate, registerDate,
                 points):
        """Parameterized constructor
            Attributes are self-explanatory
        """
        self.ID = ID
        self.lastName = lastName
        self.firstName = firstName
        self.CNP = CNP
        self.birthDate = birthDate
        self.registerDate = registerDate
        self.points = points
        Clientcard.clientacardIdList.append(self.ID)

    def __str__(self):
        """String overloader for a clientcard object

        :return: String representing clientcard data
        :rtype: String
        """
        return "{}, {}, {}, {}, {}, {}, {}".format(self.ID, self.lastName,
                                                   self.firstName, self.CNP,
                                                   self.birthDate,
                                                   self.registerDate,
                                                   self.points)

    def __eq__(self, other):
        """Clientcard objects '==' comparator

        :param other: clientcard object 
        :type other: clientcard
        :return: true if they are the same entity ; false otherwise
        :rtype: bool
        """
        if not isinstance(other, Clientcard):
            return False
        return self.ID == other.ID

    def __ne__(self, other):
        """Clientcard objects '!=' comparator
           Opposite of __eq__
        """
        return not self == other

    #
    # Getters and setters
    #

    def getID(self):
        return self.ID

    def getLastName(self):
        return self.lastName

    def getFirstName(self):
        return self.firstName

    def getCNP(self):
        return self.CNP

    def getBirthDate(self):
        return self.birthDate

    def getRegisterDate(self):
        return self.registerDate

    def getPoints(self):
        return self.points

    def setPoints(self, newPoints):
        self.points = newPoints

    #
    #
