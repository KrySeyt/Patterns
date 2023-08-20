from abc import ABC, abstractmethod


class Colleague(ABC):
    mediator: "Mediator"
    id: int

    @abstractmethod
    def change(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def colleague_changed_handler(self) -> None:
        raise NotImplementedError


class Mediator(ABC):
    colleagues: list[Colleague]

    @abstractmethod
    def colleague_changed(self, colleague: "Colleague") -> None:
        raise NotImplementedError

    @abstractmethod
    def create_colleague(self) -> Colleague:
        raise NotImplementedError


class ConcreteColleague(Colleague):
    next_colleague_id = 0

    def __init__(self, mediator: Mediator) -> None:
        self.mediator = mediator
        self.id = self.next_colleague_id
        type(self).next_colleague_id += 1

    def change(self) -> None:
        self.mediator.colleague_changed(self)

    def colleague_changed_handler(self) -> None:
        print(f"Colleague {self.id}: another colleague changing reaction")


class ConcreteMediator(Mediator):
    def __init__(self) -> None:
        self.colleagues: list[Colleague] = []

    def colleague_changed(self, changed_colleague: "Colleague") -> None:
        for colleague in self.colleagues:
            if colleague != changed_colleague:
                colleague.colleague_changed_handler()

    def create_colleague(self) -> Colleague:
        colleague = ConcreteColleague(self)
        self.colleagues.append(colleague)
        return colleague


def main() -> None:
    mediator = ConcreteMediator()
    colleagues: list[Colleague] = [
        mediator.create_colleague(),
        mediator.create_colleague(),
        mediator.create_colleague()
    ]

    for colleague in colleagues:
        print(f"Colleague {colleague.id} changing...")
        colleague.change()
        print()


if __name__ == "__main__":
    main()
