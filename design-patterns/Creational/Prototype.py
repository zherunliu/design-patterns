from abc import ABC, abstractmethod


# prototype interface
class Prototype(ABC):
    @abstractmethod
    def clone(self) -> "Prototype":
        pass

    @abstractmethod
    def get_details(self):
        pass

    def clone_prototype(self):
        try:
            return self.clone()
        except Exception as e:
            print(e)
            return None


# concretePrototype
class RectanglePrototype(Prototype):
    def __init__(self, color: str, width: str, height: str) -> None:
        self.color = color
        self.width = width
        self.height = height

    def clone(self) -> Prototype:
        return RectanglePrototype(self.color, self.width, self.height)

    def get_details(self):
        print(
            "Color: %s, Width: %s, Height: %s" % (self.color, self.width, self.height)
        )


if __name__ == "__main__":
    color, width, height = input().split()
    n = int(input())
    rectanglePrototype = RectanglePrototype(color, width, height)
    for _ in range(n):
        rectanglePrototype.clone().get_details()
