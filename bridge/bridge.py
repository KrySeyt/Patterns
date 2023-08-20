from abc import ABC, abstractmethod


class Abstraction(ABC):
    @abstractmethod
    def __init__(self, implementation: "Implementor") -> None:
        raise NotImplementedError

    @abstractmethod
    def show(self) -> None:
        raise NotImplementedError


class Implementor(ABC):
    @abstractmethod
    def get_name(self) -> str:
        raise NotImplementedError


class RefinedAbstraction(Abstraction):
    def __init__(self, implementation: Implementor) -> None:
        self._imp = implementation

    def show(self) -> None:
        print(self._imp.get_name())

    def get_info(self) -> str:
        return f"Info of {self._imp.get_name()}"


class ConcreteImplementationA(Implementor):
    def get_name(self) -> str:
        return "Implementation A"


class ConcreteImplementationB(Implementor):
    def get_name(self) -> str:
        return "Implementation B"


def main() -> None:
    imp = ConcreteImplementationB()
    abstraction = RefinedAbstraction(imp)
    abstraction.show()
    print(abstraction.get_info())


if __name__ == "__main__":
    main()
