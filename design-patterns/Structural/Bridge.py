from abc import ABC


# implementation interface
class TV(ABC):
    def turn_on(self):
        pass

    def turn_off(self):
        pass

    def switch_channel(self):
        pass


# concrete implementationA
class SonyTV(TV):
    def turn_on(self):
        print("Sony TV is ON")

    def turn_off(self):
        print("Sony TV is OFF")

    def switch_channel(self):
        print("Switching Sony TV channel")


# concrete implementationB
class TCLTV(TV):
    def turn_on(self):
        print("TCL TV is ON")

    def turn_off(self):
        print("TCL TV is OFF")

    def switch_channel(self):
        print("Switching TCL TV channel")


# abstraction
class RemoteControl(ABC):
    def __init__(self, tv: TV) -> None:
        self.tv = tv

    def perform_operation(self):
        pass


# refined abstraction
class PowerOperation(RemoteControl):
    def perform_operation(self):
        self.tv.turn_on()


class OffOperation(RemoteControl):
    def perform_operation(self):
        self.tv.turn_off()


class ChannelSwitchOperation(RemoteControl):
    def perform_operation(self):
        self.tv.switch_channel()


if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        brand, operation = map(int, input().split())

        if brand == 0:
            tv = SonyTV()
        else:
            tv = TCLTV()

        if operation == 2:
            control = PowerOperation(tv)
        elif operation == 3:
            control = OffOperation(tv)
        else:
            control = ChannelSwitchOperation(tv)

        control.perform_operation()
