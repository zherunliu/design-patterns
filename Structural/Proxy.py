from abc import ABC


# serviceInterface
class HomePurchase(ABC):
    def request_purchase(self, area: int):
        pass


# service
class HomeBuyer(HomePurchase):
    def request_purchase(self, area: int):
        print("YES")


# proxy
class HomeAgentProxy(HomePurchase):
    def __init__(self) -> None:
        self.home_buyer = HomeBuyer()

    def request_purchase(self, area: int):
        if area > 100:
            self.home_buyer.request_purchase(area)
        else:
            print("NO")


if __name__ == "__main__":
    proxy = HomeAgentProxy()
    n = int(input())
    for _ in range(n):
        area = int(input())
        proxy.request_purchase(area)
