from abc import ABC, abstractmethod
from sys import stdin


# abstract class
class CoffeeMakerTemplate(ABC):
    def __init__(self, coffee_name: str) -> None:
        self.coffee_name = coffee_name

    @abstractmethod
    def grind_coffee_beans(self):
        pass

    @abstractmethod
    def brew_coffee(self):
        pass

    def add_condiments(self):
        print("Adding condiments")

    def make_coffee(self):
        print(f"Making {self.coffee_name}:")
        self.grind_coffee_beans()
        self.brew_coffee()
        self.add_condiments()
        print()


# concrete class
class AmericanCoffeeMaker(CoffeeMakerTemplate):
    def __init__(self):
        super().__init__("American Coffee")

    def grind_coffee_beans(self):
        print("Grinding coffee beans")

    def brew_coffee(self):
        print("Brewing coffee")


# concrete class
class LatteCoffeeMaker(CoffeeMakerTemplate):
    def __init__(self):
        super().__init__("Latte")

    def grind_coffee_beans(self):
        print("Grinding coffee beans")

    def brew_coffee(self):
        print("Brewing coffee")

    # 添加调料的特定实现
    def add_condiments(self):
        print("Adding milk")
        print("Adding condiments")


if __name__ == "__main__":
    for line in stdin:
        coffee_type = int(line.strip())
        coffee_maker = None
        if coffee_type == 1:
            coffee_maker = AmericanCoffeeMaker()
        elif coffee_type == 2:
            coffee_maker = LatteCoffeeMaker()
        else:
            continue

        coffee_maker.make_coffee()
