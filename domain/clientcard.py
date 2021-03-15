class Clientcard:
    """
    Represents a client's card.
    """
    clientacardIdList = []

    def __init__(self, ID, lastName, firstName, CNP, birthDate, registerDate, points):
        self.ID = ID
        self.lastName = lastName
        self.firstName = firstName
        self.CNP = CNP
        self.birthDate = birthDate
        self.registerDate = registerDate
        self.points = points
        Clientcard.clientacardIdList.append(self.ID)

    def __str__(self):
        return "{}, {}, {}, {}, {}, {}, {}".format(
            self.ID,
            self.lastName,
            self.firstName,
            self.CNP,
            self.birthDate,
            self.registerDate,
            self.points
        )

    def __eq__(self, other):
        if not isinstance(other, Clientcard):
            return False
        return self.ID == other.ID

    def __ne__(self, other):
        return not self == other

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
