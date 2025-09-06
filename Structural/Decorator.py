from abc import ABC, abstractmethod
from sys import stdin


# component
class Coffee(ABC):
    @abstractmethod
    def brew(self):
        pass


# concrete componentA
class BlackCoffee(Coffee):
    def brew(self):
        print("Brewing Black Coffee")


# concrete componentB
class Latte(Coffee):
    def brew(self):
        print("Brewing Latte")


# decorator
class Decorator(Coffee, ABC):
    def __init__(self, coffee: Coffee) -> None:
        self.__coffee = coffee

    def brew(self):
        self.__coffee.brew()


# concrete decoratorA
class MilkDecorator(Decorator):
    def brew(self):
        super().brew()
        print("Adding Milk")


# concrete decoratorB
class SugarDecorator(Decorator):
    def brew(self):
        super().brew()
        print("Adding Sugar")


if __name__ == "__main__":
    for line in stdin:
        coffee_type, condiment_type = map(int, line.split())
        if coffee_type == 1:
            coffee = BlackCoffee()
        elif coffee_type == 2:
            coffee = Latte()
        else:
            print("Invalid coffee type")
            continue

        if condiment_type == 1:
            coffee = MilkDecorator(coffee)
        elif condiment_type == 2:
            coffee = SugarDecorator(coffee)
        else:
            print("Invalid condiment type")
            continue
        coffee.brew()
