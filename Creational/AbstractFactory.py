from abc import ABC, abstractmethod
from typing import Optional


# abstractProductA
class Chair(ABC):
    @abstractmethod
    def show_info(self):
        pass


# concreteProductA1
class ModernChair(Chair):
    def show_info(self):
        print("modern chair")


# concreteProductA2
class ClassicalChair(Chair):
    def show_info(self):
        print("classical chair")


# abstractProductB
class Sofa(ABC):
    @abstractmethod
    def show_info(self):
        pass


# concreteProductB1
class ModernSofa(Sofa):
    def show_info(self):
        print("modern sofa")


# concreteProductB2
class ClassicalSofa(Sofa):
    def show_info(self):
        print("classical sofa")


# abstractFactory
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_sofa(self) -> Sofa:
        pass


# concreteFactoryA
class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()

    def create_sofa(self) -> Sofa:
        return ModernSofa()


# concreteFactoryB
class ClassicalFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ClassicalChair()

    def create_sofa(self) -> Sofa:
        return ClassicalSofa()


def main():
    n = int(input())
    for _ in range(n):
        furniture_type = input()
        factory: Optional[FurnitureFactory] = None
        if furniture_type == "modern":
            factory = ModernFurnitureFactory()
        elif furniture_type == "classical":
            factory = ClassicalFurnitureFactory()
        else:
            continue

        factory.create_chair().show_info()
        factory.create_sofa().show_info()


if __name__ == "__main__":
    main()
