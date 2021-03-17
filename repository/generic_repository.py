import pickle

from repository.exceptions import RepositoryError


class GenericFileRepository:

    def __init__(self, fileName):
        """Parameterized constructor

        :param fileName: filename to store data in
        """
        self.__storage = {}
        self.__fileName = fileName

    def __loadFromFile(self):
        """Loads data from filename
        """
        try:
            with open(self.__fileName, 'rb') as fread:
                self.__storage = pickle.load(fread)
        except FileNotFoundError:
            self.__storage.clear()
        except RepositoryError:
            self.__storage.clear()

    def __saveToFile(self):
        """Saves data into filename
        """
        with open(self.__fileName, 'wb') as fwrite:
            pickle.dump(self.__storage, fwrite)

    def create(self, entity):
        """Creates an entity and saves it into filename

        :param entity: Entity to be created
        :type entity: Entity (Movie/Clientcard/Reservation)
        :raises RepositoryError: If entity is a duplicate
        """
        self.__loadFromFile()

        idEntity = entity.getID()
        if idEntity in self.__storage:
            raise RepositoryError('Entitatea cu id-ul acesta deja exista')

        self.__storage[idEntity] = entity
        self.__saveToFile()

    def read(self, idEntity=None):
        """Reads an entity by its id, or all entities if id is none

        :raises ValueError: if ID doesnt exist
        :return: entity or list of all entities
        """
        self.__loadFromFile()
        if idEntity is None:
            return self.__storage.values()

        if idEntity in self.__storage:
            return self.__storage[idEntity]

        raise ValueError("No entity with that ID.")

    def read_all(self):
        """
        Function read all the objects from storage
        :return:a list of all objects
        """
        self.__loadFromFile()
        return list(self.__storage.values())

    def update(self, entity):
        """Updates enity's attributes EXCEPT id

        :param entity: updated entity
        :type entity: Entity
        :raises RepositoryError: ID does not exist
        """

        self.__loadFromFile()
        idEntity = entity.getID()

        if idEntity not in self.__storage:
            raise RepositoryError('Nu este o entitate cu id-ul acesta')

        self.__storage[idEntity] = entity
        self.__saveToFile()

    def delete(self, idEntity):
        """Deletes an entity

        :param idEntity: entity's ID
        :type idEntity: int
        :raises RepositoryError: entity with that ID does not exist
        """
        self.__loadFromFile()

        if idEntity not in self.__storage:
            raise RepositoryError('Nu exista o entitate cu id-ul acesta')

        del self.__storage[idEntity]
        self.__saveToFile()

    def clear(self):
        """Clears repository
        """
        self.__loadFromFile()
        self.__storage.clear()
        self.__saveToFile()
