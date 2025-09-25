from abc import ABC, abstractmethod


# command
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


# concrete command
class OrderCommand(Command):
    def __init__(self, drink_name: str, receiver: "DrinkMaker") -> None:
        self.drink_name = drink_name
        self.receiver = receiver

    def execute(self) -> None:
        return self.receiver.make_drink(self.drink_name)


# receiver
class DrinkMaker:
    def make_drink(self, drink_name: str) -> None:
        print(f"{drink_name} is ready!")


# invoker
class OrderMachine:
    def __init__(self) -> None:
        self.command = None

    def set_command(self, command: Command):
        self.command = command

    def execute_order(self):
        if self.command is not None:
            self.command.execute()
        else:
            print("No command has been set.")


if __name__ == "__main__":
    drink_maker = DrinkMaker()
    n = int(input())

    for _ in range(n):
        drink_name = input().strip()
        command = OrderCommand(drink_name, drink_maker)

        order_machine = OrderMachine()
        order_machine.set_command(command)
        order_machine.execute_order()
