from abc import ABC, abstractmethod


class State(ABC):
    @abstractmethod
    def handle(self) -> None:
        raise NotImplementedError


class ConcreteStateA(State):
    def handle(self) -> None:
        print("State A")


class ConcreteStateB(State):
    def handle(self) -> None:
        print("State B")


class Context:
    def __init__(self, state: State) -> None:
        self.state = state

    def request(self) -> None:
        return self.state.handle()

    def change_state(self, state: State) -> None:
        self.state = state


def main() -> None:
    state1 = ConcreteStateA()
    context = Context(state1)

    context.request()

    state2 = ConcreteStateB()
    context.change_state(state2)

    context.request()


if __name__ == "__main__":
    main()
