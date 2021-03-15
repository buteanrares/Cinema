from domain.movie import Movie


class InMemoryRepository:
    """
    Repository for storing data in memory
    """

    def __init__(self):
        """
        Creates an in-memory repository
        """
        self.__storage = {}

    def create(self, movie):
        """
        Adds a new movie.
        :param movie: obj
        :return:
        :raises: KeyError if the ID already exists
        """
        movie_id = movie.getID()
        if movie_id in self.__storage:
            raise KeyError("The movie id already exists.")
        self.__storage[movie_id] = movie

    def read(self, movie_id=None):
        """
        Gets a movie by ID or all the movies.
        :param movie_id: (obj / optional)
        :return:
        """
        if movie_id is None:
            return self.__storage.values()
        if movie_id in self.__storage:
            return self.__storage[movie_id]
        return None

    def update(self, movie):
        """
        Updates a movie.
        :param movie: id of the movie to update
        :return:
        :raises KeyError if movie with movie_id does not exist
        """
        movie_id = movie.getID()
        if movie_id not in self.__storage:
            raise KeyError('No movie with id=' + str(movie_id))
        self.__storage[movie_id] = movie

    def delete(self, movie_id):
        """
        Deletes a movie.
        :param movie_id: id of the movie to delete
        :return:
        :raises: KeyError if movie with movie_id does not exist.
        """
        if movie_id not in self.__storage:
            raise KeyError("Movie with that id does not exist.")
        del self.__storage[movie_id]

    def clear(self):
        self.__storage.clear()


def test_InMemoryRepository():
    repo = InMemoryRepository()
    m1 = Movie(1, "Terminator", 1974, 15, 23, True)
    m2 = Movie(2, "Pulp Fiction", 1986, 20, 30, False)
    repo.create(m1)
    repo.create(m2)

    assert len(repo.read()) == 2
    repo.update(Movie(2, "Home Alone", 2001, 10, 31, True))
    updated = repo.read(2)
    assert updated.getID() == 2
    assert updated.getTitle() == "Home Alone"
    repo.delete(1)
    assert len(repo.read()) == 1
    assert repo.read(1) is None


test_InMemoryRepository()
