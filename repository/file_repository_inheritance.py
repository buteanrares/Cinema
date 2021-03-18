import json

from domain.movie import Movie
from repository.in_memory_repository import InMemoryRepository

@DeprecationWarning # No longer used
class FileRepositoryInheritance(InMemoryRepository):

    """In file repository class
    """

    def __init__(self, filename):
        """Parameterized constructor

        :param filename: filename to store data in
        """
        super(FileRepositoryInheritance, self).__init__()
        self.__filename = filename

    def __load_from_file(self):
        """Loads data from file
        """
        try:
            with open(self.__filename, 'r') as f_read:
                saved_movies = json.load(f_read)
                super(FileRepositoryInheritance, self).clear()
                for saved_movie in saved_movies:
                    movie = Movie(*saved_movie)
                    super(FileRepositoryInheritance, self).create(movie)
        except FileNotFoundError:
            super(FileRepositoryInheritance, self).clear()

    def __save_to_file(self):
        """Saves data to file
        """
        to_save = []
        for movie in super(FileRepositoryInheritance, self).read():
            movie_repr = [
                movie.getID(),
                movie.getTitle(),
                movie.getRelease(),
                movie.getPrice(),
                movie.getTicket(),
                movie.getInSchedule()
            ]
            to_save.append(movie_repr)
        with open(self.__filename, 'w') as f_write:
            json.dump(to_save, f_write)

    def create(self, movie):
        """
        Adds a new movie
        :param movie: (obj)
        :return:
        """
        self.__load_from_file()
        super(FileRepositoryInheritance, self).create(movie)
        self.__save_to_file()

    def read(self, movie_id=None):
        """
        Reads a movie or all movies.
        :param movie_id:
        :return:
        """
        self.__load_from_file()
        return super(FileRepositoryInheritance, self).read()

    def update(self, movie):
        """
        Updates a movie
        :param movie:
        :return:
        """
        self.__load_from_file()
        super(FileRepositoryInheritance, self).update(movie)
        self.__save_to_file()

    def delete(self, movie_id):
        """Deletes a movie by id
        """
        self.__load_from_file()
        super(FileRepositoryInheritance, self).delete(movie_id)
        self.__save_to_file()

    def clear(self):
        """Clears all data inside repository
        """
        super(FileRepositoryInheritance, self).clear()
