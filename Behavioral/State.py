from abc import ABC, abstractmethod


# state
class State(ABC):
    @abstractmethod
    def handle(self) -> str:
        pass


# concrete states
class OnState(State):
    def handle(self):
        return "Light is ON"


class OffState(State):
    def handle(self):
        return "Light is OFF"


class BlinkState(State):
    def handle(self) -> str:
        return "Light is Blinking"


# context
class Light:
    def __init__(self) -> None:
        self.state = OffState()

    def set_state(self, new_state: State):
        self.state = new_state

    def perform_operation(self):
        return self.state.handle()


if __name__ == "__main__":
    n = int(input())
    light = Light()
    for _ in range(n):
        command = input().strip()

        if command == "ON":
            light.set_state(OnState())
        elif command == "OFF":
            light.set_state(OffState())
        elif command == "BLINK":
            light.set_state(BlinkState())
        else:
            continue

        print(light.perform_operation())
