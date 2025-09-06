from typing import List
from abc import ABC


# subscriber interface
class Observer(ABC):
    def update(self, hour: int):
        pass


# publisher interface
class Subject(ABC):
    def register_obs(self, obs: Observer):
        pass

    def remove_obs(self, obs: Observer):
        pass

    def notify_obs(self):
        pass


# concrete subscriber
class Student(Observer):
    def __init__(self, name: str) -> None:
        self.name = name

    def update(self, hour: int):
        print(self.name, hour)


# concrete publisher
class Clock(Subject):
    def __init__(self) -> None:
        self.observers: List[Observer] = []
        self.hour = 0

    def register_obs(self, obs: Observer):
        self.observers.append(obs)

    def remove_obs(self, obs: Observer):
        self.observers.remove(obs)

    def notify_obs(self):
        for obs in self.observers:
            obs.update(self.hour)

    def tick(self):
        self.hour = (self.hour + 1) % 24
        self.notify_obs()


if __name__ == "__main__":
    n = int(input())
    clock = Clock()

    for _ in range(n):
        name = input()
        clock.register_obs(Student(name))

    time = int(input())
    for _ in range(time):
        clock.tick()
