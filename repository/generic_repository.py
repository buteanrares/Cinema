import pickle

from repository.exceptions import RepositoryError


class GenericFileRepository:
    def __init__(self, fileName):
        self.__storage = {}
        self.__fileName = fileName

    def __loadFromFile(self):
        try:
            with open(self.__fileName, 'rb') as fread:
                self.__storage = pickle.load(fread)
        except FileNotFoundError:
            self.__storage.clear()
        except RepositoryError:
            self.__storage.clear()

    def __saveToFile(self):
        with open(self.__fileName, 'wb') as fwrite:
            pickle.dump(self.__storage, fwrite)

    def create(self, entity):
        self.__loadFromFile()

        idEntity = entity.getID()
        if idEntity in self.__storage:
            raise RepositoryError('Entitatea cu id-ul acesta deja exista')

        self.__storage[idEntity] = entity
        self.__saveToFile()

    def read(self, idEntity=None):
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
        self.__loadFromFile()
        idEntity = entity.getID()

        if idEntity not in self.__storage:
            raise RepositoryError('Nu este o entitate cu id-ul asta')

        self.__storage[idEntity] = entity
        self.__saveToFile()

    def delete(self, idEntity):
        self.__loadFromFile()

        if idEntity not in self.__storage:
            raise RepositoryError('Nu exista o entitate cu id-ul asta')

        del self.__storage[idEntity]
        self.__saveToFile()

    def clear(self):
        self.__loadFromFile()
        self.__storage.clear()
        self.__saveToFile()
