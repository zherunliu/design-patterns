from typing import Dict
from enum import Enum
from abc import ABC
from sys import stdin


class ShapeType(Enum):
    CIRCLE = "CIRCLE"
    RECTANGLE = "RECTANGLE"
    TRIANGLE = "TRIANGLE"


class Position:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


# flyweight interface
class Shape(ABC):
    def draw(self, position: Position):
        pass

    def set_first_time(self, first_time: bool):
        pass


# concrete flyweight
class ConcreteShape(Shape):
    def __init__(self, shape_type: ShapeType) -> None:
        self.shape_type = shape_type
        self.is_first_time = True

    def draw(self, position: Position):
        print(
            f"{self.shape_type.value}{' drawn' if self.is_first_time else ' shared'} at ({position.x}, {position.y})"
        )

    def set_first_time(self, first_time: bool):
        self.is_first_time = first_time


# flyweight factory
class ShapeFactory(Shape):
    def __init__(self) -> None:
        self.shapes: Dict[ShapeType, Shape] = {}

    def get_shape(self, shape_type: ShapeType) -> Shape:
        if shape_type not in self.shapes:
            self.shapes[shape_type] = ConcreteShape(shape_type)
        return self.shapes[shape_type]


# client
def process_command(factory: ShapeFactory, command: str):
    shape_type, x, y = command.split(" ")
    x = int(x)
    y = int(y)

    shape_type = ShapeType(shape_type)
    shape = factory.get_shape(shape_type)
    shape.draw(Position(x, y))
    shape.set_first_time(False)


if __name__ == "__main__":
    factory = ShapeFactory()
    for line in stdin:
        process_command(factory, line)
