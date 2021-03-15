from domain.movie import Movie
from domain.movie_validator import MovieValidator
from domain.reservation_validator import ReservationValidator
from domain.clientcard_validator import ClientcardValidator
from domain.clientcard import Clientcard
from domain.reservation import Reservation
from service.UndoService import UndoService
from my_tools.my_sorted import my_sorted
from my_tools.binary_search import binary_search
from my_tools import permutation
import datetime
import random
import time


def str_time_prop(start, end, _format, prop):
    stime = time.mktime(time.strptime(start, _format))
    etime = time.mktime(time.strptime(end, _format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%d/%m/%Y', prop)


class MovieService(MovieValidator):

    def __init__(self, movie_repository, movie_validator, reservation_repository, undo_service: UndoService):
        self.__movie_repository = movie_repository
        self.__movie_validator = movie_validator
        self.__reservation_repository = reservation_repository
        self.__undo_service = undo_service

    def addMovie(self, ID, title, release, price, inSchedule):
        movie = Movie(ID, title, release, price, inSchedule)
        self.__movie_validator.validate(movie)
        action = lambda: self.__movie_repository.create(movie)
        reverse = lambda result: self.__movie_repository.delete(ID)
        self.__undo_service.clear_operations()
        self.__undo_service.add_new_operation(action, reverse)

    def updateMovie(self, ID, title, release, price, inSchedule):
        movie = Movie(ID, title, release, price, inSchedule)
        self.__movie_validator.validate(movie)
        self.__movie_repository.update(movie)

    def deleteMovie(self, movie_id):
        if isinstance(movie_id, int):
            movie = self.__movie_repository.read(movie_id)
            action = lambda: self.__movie_repository.delete(movie_id)
            reverse = lambda result: self.__movie_repository.create(movie)
            self.__undo_service.add_new_operation(action, reverse)
            for reservation in self.__reservation_repository.read():
                if reservation.getMovieID() == movie_id:
                    self.__reservation_repository.delete(reservation.getID())
        elif movie_id == "all":
            self.__movie_repository.clear()
            self.__reservation_repository.clear()

    def showAllMovies(self):
        moviesList = self.__movie_repository.read()
        return moviesList

    def searchMovie(self, toSearch):
        """
        Search in movies list
        return: list of movies with 'tosearch' in them
        """
        movies = []
        moviesList = self.__movie_repository.read()
        for movie in moviesList:
            if toSearch in movie.__str__():
                movies.append(movie)
        return movies

    def getMoviePrice(self, movie_id):
        movie = self.__movie_repository.read(movie_id)
        try:
            return movie.getPrice()
        except AttributeError:
            raise ValueError("No movie with that ID.")

    def populateMovies(self, n):
        """
        Populates movies with n movies with random attributes
        """
        titleList = ["The Godfather", "The Shawshank Redemption", "Raging Bull", "Casablanca", "Citizen Kane",
                     "Forrest Gump", "Star Wars: Episode IV - A New Hope", "Whiplash", "Boyhood", "The Master",
                     "Before Midnight", "Spotlight", "Bohemian Rhapsody", "Black Swan", "Stories We Tell",
                     "Angry Men", "The Dark Knight", "Inception", "Matrix", "Goodfellas", "Joker", "Seven Samurai"]
        random.seed()
        moviesList = self.__movie_repository.read()
        movieIDs = []
        for movie in moviesList:
            movieIDs.append(movie.getID())
        for i in range(n):
            while True:
                ID = random.randint(1, 9999999)
                if ID not in movieIDs:
                    break
            movie = Movie(ID, random.choice(titleList), random.randint(1940, 2018),
                          random.randint(5, 50), random.choice([True, False]))
            self.__movie_validator.validate(movie)
            action = lambda: self.__movie_repository.create(movie)
            reverse = lambda result: self.__movie_repository.delete(ID)
            self.__undo_service.add_new_operation(action, reverse)
            movieIDs.append(ID)

    def isInSchedule(self, movie_id):
        movie = self.__movie_repository.read(movie_id)
        if movie.getInSchedule():
            return True
        return False

    def reservationsForMovie(self, movie_id):
        """
        Returns the number of reservations for a movie by id.
        """
        nr = 0
        for res in self.__reservation_repository.read():
            if res.getMovieID() == movie_id:
                nr += 1
        return nr

    def showMoviesByReservations(self):
        """
        Returns a list of movies in desc. order by number of reservations
        """
        moviesList = self.__movie_repository.read()
        max_per_id = {}
        for res in self.__reservation_repository.read():
            movieID = res.getMovieID()
            if movieID not in max_per_id:
                max_per_id[movieID] = 0
            else:
                max_per_id[movieID] += 1
        new_moviesList = list(filter(lambda movie: movie.getID() in max_per_id, moviesList))
        final_list = my_sorted(new_moviesList, key=lambda movie: max_per_id[movie.getID()], reverse=True)
        list_of_res = []
        for movie in final_list:
            list_of_res.append(max_per_id[movie.getID()])
        output = zip(final_list, list_of_res)
        return output

    def search_id(self, id):
        """
        Searches for an id
        """
        list_of_id = []
        for movie in self.__movie_repository.read():
            list_of_id.append(movie.getID())
        sorted_list_of_id = sorted(list_of_id)
        return binary_search(sorted_list_of_id, id)

    def get_movie_permutations(self):
        """
        Returns the permutated list of movies.
        """
        list_of_movies = self.__movie_repository.read()
        id_list = []
        for movie in list_of_movies:
            id_list.append(movie.getID())
        permuted_list_of_id = permutation.elements_of_list(id_list)
        list_of_permuted_movies = []
        for list_of_id in permuted_list_of_id:
            intermediate_list_of_movies = []
            for id_to_append in list_of_id:
                intermediate_list_of_movies.append(self.__movie_repository.read(id_to_append))
            list_of_permuted_movies.append(intermediate_list_of_movies)
        return list_of_permuted_movies


class ReservationService(ReservationValidator):

    def __init__(self, reservation_repository, reservation_validator, movie_repository, clientcard_repository,
                 undo_service: UndoService):
        self.__reservation_repository = reservation_repository
        self.__reservation_validator = reservation_validator
        self.__movie_repository = movie_repository
        self.__clientcard_repository = clientcard_repository
        self.__undo_service = undo_service

    def addReservation(self, ID, movie_ID, clientcard_ID, date, _time):
        movie = self.__movie_repository.read(movie_ID)
        clientcard = self.__clientcard_repository.read(clientcard_ID)
        if movie.getInSchedule():
            clientcard.setPoints(clientcard.getPoints() + int((10 / 100 * movie.getPrice())))
            reservation = Reservation(ID, movie_ID, clientcard_ID, date, _time)
            self.__reservation_validator.validate(reservation)
            self.__clientcard_repository.update(clientcard)
            action = lambda: self.__reservation_repository.create(reservation)
            reverse = lambda result: self.__reservation_repository.delete(ID)
            self.__undo_service.add_new_operation(action, reverse)
        else:
            raise ValueError("That movie is no longer in schedule.")

    def updateReservation(self, reservationID, reservationMovieId, reservationClientcardId, reservationDate,
                          reservationTime):
        reservation = Reservation(reservationID, reservationMovieId, reservationClientcardId, reservationDate,
                                  reservationTime)
        self.__reservation_validator.validate(reservation)
        self.__reservation_repository.update(reservation)

    def deleteReservation(self, reservation_id):
        if reservation_id == "all":
            self.__reservation_repository.clear()
        else:
            res = self.__reservation_repository.read(reservation_id)
            self.__reservation_repository.delete(reservation_id)
            action = lambda: self.__reservation_repository.delete(reservation_id)
            reverse = lambda result: self.__reservation_repository.create(res)
            self.__undo_service.add_new_operation(action, reverse)

    def showAllReservations(self):
        reservationsList = self.__reservation_repository.read()
        return reservationsList

    def showReservationsInInterval(self, timeLeft, timeRight):
        """
        Returns a list of reservations in a given interval of time
        """
        resList = []
        timeLeft = datetime.datetime.strptime(timeLeft, '%H:%M')
        timeRight = datetime.datetime.strptime(timeRight, '%H:%M')
        reservationsList = self.__reservation_repository.read()
        for reservation in reservationsList:
            _time = reservation.getTime()
            _time = str(_time)
            _time = datetime.datetime.strptime(_time, '%H:%M')
            if timeLeft <= _time <= timeRight:
                resList.append(reservation)
        return resList

    def deleteReservationsInInterval(self, dateLeft, dateRight):
        """
        Deletes the reservation in the given interval of time.
        """
        dateLeft = datetime.datetime.strptime(dateLeft, '%d/%m/%Y')
        dateRight = datetime.datetime.strptime(dateRight, '%d/%m/%Y')
        reservationsList = self.__reservation_repository.read()
        for reservation in list(reservationsList):
            date = reservation.getDate()
            date = str(date)
            date = datetime.datetime.strptime(date, "%d/%m/%Y")
            if dateLeft <= date <= dateRight:
                self.__reservation_repository.delete(reservation.ID)

    def populateReservations(self, n):
        """
        Populates with n reservations with random attributes.
        """
        movieIDs = []
        moviesList = self.__movie_repository.read()
        for movie in moviesList:
            movieIDs.append(movie.getID())
        clientcardIDs = []
        clientcardsList = self.__clientcard_repository.read()
        for clientcard in clientcardsList:
            clientcardIDs.append(clientcard.getID())
        timeList = ['14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00',
                    '19:30',
                    '20:00', '20:30', '21:00', '21:30', '22:00', '22:30']
        random.seed()
        reservationsList = self.__reservation_repository.read()
        reservationIDs = []
        for res in reservationsList:
            reservationIDs.append(res.getID())
        for i in range(n):
            while True:
                ID = random.randint(1, 9999999)
                if ID not in reservationIDs:
                    break
            rngClientCardID = random.choice(clientcardIDs)
            rngMovieID = random.choice(movieIDs)
            reservation = Reservation(ID, rngMovieID, rngClientCardID,
                                      str(random_date("01/01/2015", "01/01/2019", random.random())),
                                      random.choice(timeList))
            clientcard = self.__clientcard_repository.read(rngClientCardID)
            movie = self.__movie_repository.read(rngMovieID)
            clientcard.setPoints(clientcard.getPoints() + int((10 / 100 * movie.getPrice())))
            self.__reservation_validator.validate(reservation)
            action = lambda: self.__reservation_repository.create(reservation)
            reverse = lambda result: self.__reservation_repository.delete(ID)
            self.__undo_service.add_new_operation(action, reverse)
            reservationIDs.append(ID)


class ClientcardService(ClientcardValidator):
    def __init__(self, clientcard_repository, clientcard_validator, reservation_repository, undo_service: UndoService):
        self.__clientcard_repository = clientcard_repository
        self.__clientcard_validator = clientcard_validator
        self.__reservation_repository = reservation_repository
        self.__undo_service = undo_service

    def addClientcard(self, ID, lastName, firstName, CNP, birthDate, registerDate, points):
        clientcard = Clientcard(ID, lastName, firstName, CNP, birthDate, registerDate, points)
        self.__clientcard_validator.validate(clientcard)
        action = lambda: self.__clientcard_repository.create(clientcard)
        reverse = lambda result: self.__clientcard_repository.delete(ID)
        self.__undo_service.add_new_operation(action, reverse)

    def updateClientcard(self, clientcardID, clientcardFirstName, clientcardLastname, clientcardCNP,
                         clientcardBirthDate,
                         clientcardRegisterDate, clientcardPoints):
        clientcard = Clientcard(clientcardID, clientcardFirstName, clientcardLastname, clientcardCNP,
                                clientcardBirthDate,
                                clientcardRegisterDate, clientcardPoints)
        self.__clientcard_validator.validate(clientcard)
        self.__clientcard_repository.update(clientcard)
        self.__clientcard_repository.update(clientcard)

    def deleteClientcard(self, clientcard_id):
        if clientcard_id == "all":
            self.__clientcard_repository.clear()
            self.__reservation_repository.clear()
        else:
            self.__clientcard_repository.delete(clientcard_id)
            for reservation in self.__reservation_repository.read():
                if clientcard_id == reservation.getClientcardID():
                    cc = self.__clientcard_repository.read(clientcard_id)
                    action = lambda: self.__clientcard_repository.delete(clientcard_id)
                    reverse = lambda result: self.__clientcard_repository.create(reservation)
                    self.__undo_service.add_new_operation(action, reverse)
                    self.__reservation_repository.delete(reservation.getID())

    def searchClientcard(self, toSearch):
        """
        Searches for a clientcard with 'tosearch' in it
        """
        clientcards = self.__clientcard_repository.read()
        result = list(filter(lambda cc: toSearch in str(cc), clientcards))
        return result

    def showAllClientcards(self):
        clientcardList = self.__clientcard_repository.read()
        return clientcardList

    def showClientcardsByPts(self):
        clientcardList = self.__clientcard_repository.read()
        clientcardList = sorted(clientcardList, key=lambda clientcard: clientcard.points, reverse=True)
        return clientcardList

    def addPoints(self, clientcard_id, price):
        """
        Adds points based on a percentage of movies made
        """
        points = 50 / 100 * price
        clientcard = self.__clientcard_repository.read(clientcard_id)
        clientcard.setPoints(clientcard.getPoints() + points)
        self.__clientcard_repository.update(clientcard)

    def __givePoints(self, cc, value):
        new_P = cc.getPoints() + value
        new_id = cc.getID()
        new_LN = cc.getLastName()
        new_FN = cc.getFirstName()
        new_CNP = cc.getCNP()
        new_BD = cc.getBirthDate()
        new_RD = cc.getRegisterDate()
        self.updateClientcard(new_id, new_FN, new_LN, new_CNP, new_BD, new_RD, new_P)
        return self.__clientcard_repository.read(new_id)

    def giveBirthdayBonus(self, value, dateLeft, dateRight):
        """
        Gives a birthday bonus
        """
        list_of_cc = self.__clientcard_repository.read_all()
        return self.__birthdayBonusRecursive(value, dateLeft, dateRight, list_of_cc)

    def __birthdayBonusRecursive(self, value, dateLeft, dateRight, list_of_cc):
        if not list_of_cc:
            return []
        updated = self.__birthdayBonusRecursive(value, dateLeft, dateRight, list_of_cc[1:])
        first_cc = list_of_cc[0]

        date = first_cc.getBirthDate()
        date = str(date)
        date = datetime.datetime.strptime(date, '%d/%m/%Y')
        dateLeft = datetime.datetime.strptime(dateLeft, '%d/%m/%Y')
        dateRight = datetime.datetime.strptime(dateRight, '%d/%m/%Y')

        if dateLeft <= date <= dateRight:
            updated_cc = self.__givePoints(first_cc,value)
            updated.append(updated_cc)
        return updated

    def populateClientcards(self, n):
        firstNames = ['Emma', 'Olivia', 'Ava', 'Isabella', 'Sophia', 'Charlotte', 'Mia', 'Amelia', 'Harper', 'Evelyn',
                      'Liam', 'Noah', 'William', 'James', 'Oliver', 'Benjamin', 'Elijah', 'Lucas', 'Mason', 'Logan']
        lastNames = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor',
                     'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Thompson', 'Garcia', 'Martinez', 'Robinson']
        clientcardList = self.__clientcard_repository.read()
        clientcardIDs = []
        for cc in clientcardList:
            clientcardIDs.append(cc.getID())
        random.seed()
        for i in range(n):
            while True:
                ID = random.randint(1, 9999999)
                if ID not in clientcardIDs:
                    break
            clientcard = Clientcard(ID, random.choice(lastNames), random.choice(firstNames),
                                    random.randint(10000, 100000),
                                    str(random_date("01/01/1990", "01/01/2006", random.random())),
                                    str(random_date("01/01/2012", "01/01/2019", random.random())),
                                    random.randint(1, 50))
            self.__clientcard_validator.validate(clientcard)
            self.__clientcard_repository.create(clientcard)
            action = lambda: self.__clientcard_repository.create(clientcard)
            reverse = lambda result: self.__clientcard_repository.delete(ID)
            self.__undo_service.add_new_operation(action, reverse)
            clientcardIDs.append(ID)
