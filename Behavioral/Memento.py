from typing import List
from sys import stdin


# memento
class Memento:
    def __init__(self, value: int) -> None:
        self.__value = value

    def get_value(self):
        return self.__value


# originator
class Originator:
    def __init__(self) -> None:
        self.__value = 0

    def increment(self):
        self.__value += 1
        print(self.__value)

    def decrement(self):
        self.__value -= 1
        print(self.__value)

    def save2Memento(self):
        return Memento(self.__value)

    def restoreFromMemento(self, memento: Memento):
        self.__value = memento.get_value()
        print(self.__value)


# caretaker
class Caretaker:
    def __init__(self, originator: Originator) -> None:
        self.originator = originator
        self.undo_stack: List[Memento] = []
        self.redo_stack: List[Memento] = []

    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.originator.save2Memento())
            originator.restoreFromMemento(self.undo_stack.pop())

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.originator.save2Memento())
            self.originator.restoreFromMemento(self.redo_stack.pop())

    def save(self, memento: Memento):
        self.redo_stack = []
        self.undo_stack.append(memento)


if __name__ == "__main__":
    originator = Originator()
    caretaker = Caretaker(originator)
    for line in stdin:
        operation = line.strip()
        if operation == "Increment":
            caretaker.save(originator.save2Memento())
            originator.increment()
        elif operation == "Decrement":
            caretaker.save(originator.save2Memento())
            originator.decrement()
        elif operation == "Undo":
            caretaker.undo()
        elif operation == "Redo":
            caretaker.redo()
