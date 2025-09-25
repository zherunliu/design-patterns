from abc import ABC, abstractmethod

# ABC 用于标识一个类为抽象基类
# @abstractmethod 装饰器用于将抽象基类中的方法标记为抽象方法


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


# creator
class BlockFactory(ABC):
    @abstractmethod
    def create_block(self) -> Block:
        pass


# concreteCreatorA
class CircleBlockFactory(BlockFactory):
    def create_block(self) -> Block:
        return CircleBlock()


# concreteCreatorB
class SquareBlockFactory(BlockFactory):
    def create_block(self) -> Block:
        return SquareBlock()


class BlockFactorySystem:
    def product_blocks(self, factory: BlockFactory, quantity: int):
        black = factory.create_block()
        for _ in range(quantity):
            black.product()


def main():
    factory_system = BlockFactorySystem()
    n = int(input())
    for _ in range(n):
        block_type, quantity = input().split()
        quantity = int(quantity)
        if block_type == "Circle":
            factory_system.product_blocks(CircleBlockFactory(), quantity)
        elif block_type == "Square":
            factory_system.product_blocks(SquareBlockFactory(), quantity)


if __name__ == "__main__":
    main()
