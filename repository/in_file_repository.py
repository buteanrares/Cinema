import json
from domain.movie import Movie
from domain.reservation import Reservation
from domain.clientcard import Clientcard


@DeprecationWarning     # No longer used
class MovieFileRepository:

    def __init__(self, filename):
        self.__filename = filename
        self.__storage = {}

    def __load_from_file(self):
        try:
            with open(self.__filename, 'r') as f_read:
                saved_movies = json.load(f_read)
                self.__storage.clear()
                for saved_movie in saved_movies:
                    movie = Movie(*saved_movie)
                    self.__storage[movie.getID()] = movie
        except FileNotFoundError:
            print("File not found.")
            self.__storage = {}

    def __save_to_file(self):
        to_save = []
        for movie in self.__storage.values():
            movie_repr = [
                movie.getID(),
                movie.getTitle(),
                movie.getRelease(),
                movie.getPrice(),
                movie.getInSchedule()
            ]
            to_save.append(movie_repr)
        with open(self.__filename, 'w') as f_write:
            json.dump(to_save, f_write)

    def create(self, movie):
        """
        Adds a new movie.
        :param movie: obj
        :return:
        """
        self.__load_from_file()
        movie_id = movie.getID()
        if movie_id in self.__storage:
            raise KeyError("Movie with given id already exists!")
        self.__storage[movie_id] = movie
        Movie.moviesIdList.append(movie_id)
        self.__save_to_file()

    def read(self, movie_id=None):
        """
        Reads a movie with given id or reads all movies.
        :param movie_id: (optional / int)
        :return:
        """
        self.__load_from_file()
        if movie_id is None:
            return self.__storage.values()
        if movie_id in self.__storage:
            return self.__storage[movie_id]
        return None

    def update(self, movie):
        """
        Updates a movie.
        :param movie:
        :return:
        """
        self.__load_from_file()
        movie_id = movie.getID()
        if movie_id not in self.__storage:
            raise KeyError("Movie with given ID does not exist!")
        self.__storage[movie_id] = movie
        self.__save_to_file()

    def delete(self, movie_id):
        """
        Removes a movie with given ID.
        :param movie_id:
        :return:
        """
        self.__load_from_file()
        if movie_id not in self.__storage:
            raise KeyError("Movie with given ID does not exist!")
        del self.__storage[movie_id]
        self.__save_to_file()


@DeprecationWarning     # No longer used
class ReservationFileRepository:

    def __init__(self, filename):
        self.__filename = filename
        self.__storage = {}

    def __load_from_file(self):
        try:
            with open(self.__filename, 'r') as f_read:
                saved_reservations = json.load(f_read)
                self.__storage.clear()
                for saved_reservation in saved_reservations:
                    reservation = Reservation(*saved_reservation)
                    self.__storage[reservation.getID()] = reservation
        except FileNotFoundError:
            self.__storage = {}

    def __save_to_file(self):
        to_save = []
        for reservation in self.__storage.values():
            reservation_repr = [
                reservation.getID(),
                reservation.getMovieID(),
                reservation.getClientcardID(),
                reservation.getDate(),
                reservation.getTime(),
            ]
            to_save.append(reservation_repr)
        with open(self.__filename, 'w') as f_write:
            json.dump(to_save, f_write)

    def create(self, reservation):
        """
        Adds a new movie.
        :param reservation: obj
        :return:
        """
        self.__load_from_file()
        reservation_id = reservation.getID()
        if reservation_id in self.__storage:
            raise KeyError("Reservation with given id already exists!")
        self.__storage[reservation_id] = reservation
        self.__save_to_file()

    def read(self, reservation_id=None):
        """
        Reads a movie with given id or reads all movies.
        :param reservation_id: (optional / int)
        :return:
        """
        self.__load_from_file()
        if reservation_id is None:
            return self.__storage.values()
        if reservation_id in self.__storage:
            return self.__storage[reservation_id]
        return None

    def update(self, reservation):
        """
        Updates a movie.
        :param reservation:
        :return:
        """
        self.__load_from_file()
        reservation_id = reservation.getID
        if reservation_id not in self.__storage:
            raise KeyError("Reservation with given ID does not exist!")
        self.__storage[reservation_id] = reservation
        self.__save_to_file()

    def delete(self, reservation_id):
        """
        Removes a movie with given ID.
        :param reservation_id:
        :return:
        """
        self.__load_from_file()
        if reservation_id not in self.__storage:
            raise KeyError("Reservation with given ID does not exist!")
        del self.__storage[reservation_id]
        self.__save_to_file()


@DeprecationWarning     # No longer used
class ClientcardFileRepository:

    def __init__(self, filename):
        self.__filename = filename
        self.__storage = {}

    def __load_from_file(self):
        try:
            with open(self.__filename, 'r') as f_read:
                saved_clientcards = json.load(f_read)
                self.__storage.clear()
                for saved_clientcard in saved_clientcards:
                    clientcard = Clientcard(*saved_clientcard)
                    self.__storage[clientcard.getID()] = clientcard
        except FileNotFoundError:
            self.__storage = {}

    def __save_to_file(self):
        to_save = []
        for clientcard in self.__storage.values():
            clientcard_repr = [
                clientcard.getID(),
                clientcard.getFirstName(),
                clientcard.getLastName(),
                clientcard.getCNP(),
                clientcard.getBirthDate(),
                clientcard.getRegisterDate(),
                clientcard.getPoints()
            ]
            to_save.append(clientcard_repr)
        with open(self.__filename, 'w') as f_write:
            json.dump(to_save, f_write)

    def create(self, clientcard):
        self.__load_from_file()
        if clientcard.getID() in self.__storage:
            raise KeyError("Clientcard with that ID already exists!")
        if clientcard.getCNP() in self.__storage:
            raise KeyError("Clientcard with that CNP already exists!")
        self.__storage[clientcard.getID()] = clientcard
        Clientcard.clientacardIdList.append(clientcard.getID())
        self.__save_to_file()

    def read(self, clientcard_id=None):
        self.__load_from_file()
        if clientcard_id is None:
            return self.__storage.values()
        else:
            return self.__storage[clientcard_id]

    def update(self, clientcard):
        clientcard_id = clientcard.getID()
        if clientcard_id not in self.__storage:
            raise KeyError("Clientcard with that ID does not exist!")
        else:
            self.__storage[clientcard_id] = clientcard
            self.__save_to_file()

    def delete(self, clientcard_id):
        if clientcard_id not in self.__storage:
            raise KeyError("Clientcard with that ID does not exist!")
        else:
            del self.__storage[clientcard_id]
            self.__save_to_file()
