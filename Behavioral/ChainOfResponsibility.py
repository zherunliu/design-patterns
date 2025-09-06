from abc import ABC
from typing import Optional


# handler
class LeaveHandler(ABC):
    def handle_request(self, name: str, days: int):
        pass


# concrete handlerA
class Supervisor(LeaveHandler):
    MAX_DAYS = 3

    def __init__(self, handler: Optional[LeaveHandler] = None) -> None:
        self.next_handler = handler

    def handle_request(self, name: str, days: int):
        if days <= self.MAX_DAYS:
            print(f"{name} Approved by Supervisor.")
        elif self.next_handler:
            self.next_handler.handle_request(name, days)
        else:
            print(f"{name} Denied by Supervisor.")


# concrete handlerB
class Manager(LeaveHandler):
    MAX_DAYS = 7

    def __init__(self, handler: Optional[LeaveHandler] = None) -> None:
        self.next_handler = handler

    def handle_request(self, name: str, days: int):
        if days <= self.MAX_DAYS:
            print(f"{name} Approved by Manager.")
        elif self.next_handler:
            self.next_handler.handle_request(name, days)
        else:
            print(f"{name} Denied by Manager.")


# concrete handlerC
class Director(LeaveHandler):
    MAX_DAYS = 10

    def handle_request(self, name: str, days: int):
        if days <= self.MAX_DAYS:
            print(f"{name} Approved by Director.")
        else:
            print(f"{name} Denied by Director.")


if __name__ == "__main__":
    n = int(input())
    director = Director()
    manager = Manager(director)
    supervisor = Supervisor(manager)

    for _ in range(n):
        name, days = input().split()
        days = int(days)
        supervisor.handle_request(name, days)
