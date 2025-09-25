# subsystemA
class AirConditioner:
    def turn_off(self):
        print("Air Conditioner is turned off.")


# subsystemB
class DeskLamp:
    def turn_off(self):
        print("Desk Lamp is turned off.")


# subsystemC
class Television:
    def turn_off(self):
        print("Television is turned off.")


class PowerSwitchFacade:
    def __init__(self) -> None:
        self.air_conditioner = AirConditioner()
        self.desk_lamp = DeskLamp()
        self.television = Television()

    def turn_off_device(self, device_code: int):
        if device_code == 1:
            self.air_conditioner.turn_off()
        elif device_code == 2:
            self.desk_lamp.turn_off()
        elif device_code == 3:
            self.television.turn_off()
        else:
            print("All devices are off.")


if __name__ == "__main__":
    n = int(input())
    device_code = [int(input()) for _ in range(n)]
    power_switch = PowerSwitchFacade()

    for code in device_code:
        power_switch.turn_off_device(code)
