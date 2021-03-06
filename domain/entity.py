class Entity:

    """Entity class for domain-level objects"""

    def __init__(self, id_entity):
        self.__id_entity = id_entity

    @property
    def id_entity(self):
        return self.__id_entity
