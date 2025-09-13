from abc import ABC, abstractmethod
from typing import List


# visitor
class Visitor(ABC):
    @abstractmethod
    def visit_circle(self, circle: "Circle"):
        pass

    @abstractmethod
    def visit_rectangle(self, rectangle: "Rectangle"):
        pass


# element
class Shape(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor):
        pass


# concrete elements
class Circle(Shape):
    def __init__(self, radius: int):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def accept(self, visitor: Visitor):
        visitor.visit_circle(self)


class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def accept(self, visitor: Visitor):
        visitor.visit_rectangle(self)


# concrete visitor
class AreaCalculator(Visitor):
    def visit_circle(self, circle: Circle):
        area = 3.14 * circle.get_radius() ** 2
        print(area)

    def visit_rectangle(self, rectangle: Rectangle):
        area = rectangle.get_width() * rectangle.get_height()
        print(area)


# client
class Drawing:
    def __init__(self, shapes: List[Shape]) -> None:
        self.shapes = shapes

    def accept(self, visitor: Visitor):
        for shape in self.shapes:
            shape.accept(visitor)


if __name__ == "__main__":
    n = int(input())
    shapes: List[Shape] = []

    for _ in range(n):
        shape, *params = input().split()

        if shape == "Circle":
            radius = int(params[0])
            shapes.append(Circle(radius))
        elif shape == "Rectangle":
            width, height = map(int, params)
            shapes.append(Rectangle(width, height))
        else:
            continue

    draw = Drawing(shapes)
    area_calculator = AreaCalculator()
    draw.accept(area_calculator)
