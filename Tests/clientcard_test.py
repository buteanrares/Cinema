from domain.clientcard import Clientcard


def test_Clientcard():
    id = 2
    lastName = "Butean"
    firstName = "Rares"
    CNP = 12834
    birthDate = "14/05/2000"
    registerDate = "20/11/2019"
    points = 20
    test = Clientcard(id, lastName, firstName, CNP, birthDate, registerDate, points)
    assert test.getID() == id
    assert test.getLastName() == lastName
    assert test.getFirstName() == firstName
    assert test.getCNP() == CNP
    assert test.getBirthDate() == birthDate
    assert test.getRegisterDate() == registerDate
    assert test.getPoints() == points
    test.setPoints(10)
    assert test.getPoints() == 10
