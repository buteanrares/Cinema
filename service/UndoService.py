class Operationsss:
    def __init__(self, action, reverse_action):
        self.__action = action
        self.__reverse_action = reverse_action
        self.__last_result = None

    def apply_action(self):
        self.__last_result = self.__action()

    def apply_reverse_action(self):
        self.__reverse_action(self.__last_result)


class UndoService:
    def __init__(self):
        self.__list_for_undo = []
        self.__list_for_redo = []

    def clear_operations(self):
        self.__list_for_redo.clear()

    def add_new_operation(self, action, reverse):
        operation = Operationsss(action, reverse)
        self.__apply_operation(operation)

    def undo(self):
        if not self.__list_for_undo:
            return False
        operation = self.__list_for_undo.pop()
        operation.apply_reverse_action()
        self.__list_for_redo.append(operation)
        return True

    def redo(self):
        if not self.__list_for_redo:
            return False
        operation = self.__list_for_redo.pop()
        self.__apply_operation(operation)
        return True

    def __apply_operation(self, operation: Operationsss):
        operation.apply_action()
        self.__list_for_undo.append(operation)
