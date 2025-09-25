from abc import ABC, abstractmethod


# product interface
class Block(ABC):
    @abstractmethod
    def product(self):
        pass


# concreteProductA
class CircleBlock(Block):
    def product(self):
        print("Circle Block")


# concreteProductB
class SquareBlock(Block):
    def product(self):
        print("Square Block")


# concreteCreator
class Factory:
    def product_blocks(self, product_type: Block, quantity: int):
        for _ in range(quantity):
            product_type.product()


def main():
    factory = Factory()
    n = int(input())
    for _ in range(n):
        block_type, quantity = input().split()
        quantity = int(quantity)
        if block_type == "Circle":
            factory.product_blocks(CircleBlock(), quantity)
        elif block_type == "Square":
            factory.product_blocks(SquareBlock(), quantity)


if __name__ == "__main__":
    main()
