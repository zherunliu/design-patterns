from abc import ABC, abstractmethod


# product
class Bike:
    def __init__(self) -> None:
        self.frame = None
        self.tires = None

    def set_frame(self, frame: str):
        self.frame = frame

    def set_tires(self, tires: str):
        self.tires = tires

    def __str__(self) -> str:
        return f"{self.frame} {self.tires}"


# builder interface
class BikeBuilder(ABC):
    def build_frame(self):
        pass

    def build_tires(self):
        pass

    @abstractmethod
    def get_result(self) -> Bike:
        pass


# concrete builderA
class MountainBikeBuilder(BikeBuilder):
    def __init__(self) -> None:
        self.bike = Bike()

    def build_frame(self):
        self.bike.set_frame("Aluminum Frame")

    def build_tires(self):
        self.bike.set_tires("Knobby Tires")

    def get_result(self) -> Bike:
        return self.bike


# concrete builderB
class RoadBikeBuilder(BikeBuilder):
    def __init__(self):
        self.bike = Bike()

    def build_frame(self):
        self.bike.set_frame("Carbon Frame")

    def build_tires(self):
        self.bike.set_tires("Slim Tires")

    def get_result(self):
        return self.bike


# director
class BikeDirector:
    def constructor(self, builder: BikeBuilder):
        builder.build_frame()
        builder.build_tires()
        return builder.get_result()


def main():
    n = int(input())
    bikeDirector = BikeDirector()
    for _ in range(n):
        bike_type = input()
        if bike_type == "mountain":
            bike = bikeDirector.constructor(MountainBikeBuilder())
        elif bike_type == "road":
            bike = bikeDirector.constructor(RoadBikeBuilder())
        else:
            continue
        print(bike)


if __name__ == "__main__":
    main()
