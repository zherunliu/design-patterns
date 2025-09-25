from abc import ABC, abstractmethod


# strategy
class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, original_price: int) -> int:
        pass


# concrete strategyA
class ConcreteStrategyA(DiscountStrategy):
    def apply_discount(self, original_price: int):
        return round(original_price * 0.9)


# concrete strategyB
class ConcreteStrategyB(DiscountStrategy):
    def __init__(self) -> None:
        self.thresholds = [100, 150, 200, 300]
        self.discounts = [5, 15, 25, 40]

    def apply_discount(self, original_price: int) -> int:
        for threshold, discount in zip(
            reversed(self.thresholds), reversed(self.discounts)
        ):
            if original_price >= threshold:
                return original_price - discount
        return original_price


# context
class DiscountContext:
    def __init__(self) -> None:
        self.discount_strategy = None

    def set_discount_strategy(self, discount_strategy: DiscountStrategy):
        self.discount_strategy = discount_strategy

    def apply_discount(self, original_price: int):
        if self.discount_strategy:
            return self.discount_strategy.apply_discount(original_price)


if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        price, strategy_type = map(int, input().split(" "))

        if strategy_type == 1:
            discount_strategy = ConcreteStrategyA()
        elif strategy_type == 2:
            discount_strategy = ConcreteStrategyB()
        else:
            break

        context = DiscountContext()
        context.set_discount_strategy(discount_strategy)

        print(context.apply_discount(price))
