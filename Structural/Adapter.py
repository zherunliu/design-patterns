from abc import ABC


# client interface
class USB(ABC):
    def charge(self):
        pass


# service interface
class TypeC(ABC):
    def charge(self):
        pass


# adapter
class AdapterUsb2TypeC(USB):
    def __init__(self, type_c: TypeC) -> None:
        self.type_c = type_c

    def charge(self):
        print("USB Adapter")
        self.type_c.charge()


# service
class TypeCComputer(TypeC):
    def charge(self):
        print("TypeC")


if __name__ == "__main__":
    n = int(input())

    for _ in range(n):
        choice = int(input())
        if choice == 1:
            TypeCComputer().charge()
        elif choice == 2:
            AdapterUsb2TypeC(TypeC()).charge()
