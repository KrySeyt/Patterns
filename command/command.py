from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        raise NotImplementedError


class ConcreteCommand(Command):
    def __init__(self, receiver: "Receiver") -> None:
        self.receiver = receiver

    def execute(self) -> None:
        return self.receiver.action()


class Invoker:
    def __init__(self, command: Command):
        self.command = command

    def event_handling(self) -> None:
        self.command.execute()


class Receiver:
    def action(self) -> None:
        print("Receiver action")


def main() -> None:
    command = ConcreteCommand(Receiver())
    invoker = Invoker(command)
    invoker.event_handling()


if __name__ == "__main__":
    main()
