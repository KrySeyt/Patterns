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


class ConcreteImplementationA(Implementor):
    def get_name(self) -> str:
        return "Implementation A"


class ConcreteImplementationB(Implementor):
    def get_name(self) -> str:
        return "Implementation B"


class AbstractionFactory(ABC):
    @abstractmethod
    def get_abstraction(self) -> Abstraction:
        raise NotImplementedError


class ConcreteFactoryA(AbstractionFactory):
    def get_abstraction(self) -> RefinedAbstraction:
        return RefinedAbstraction(ConcreteImplementationA())


class ConcreteFactoryB(AbstractionFactory):
    def get_abstraction(self) -> RefinedAbstraction:
        return RefinedAbstraction(ConcreteImplementationB())


class Client:
    def __init__(self, abstraction_factory: AbstractionFactory) -> None:
        self.abstraction = abstraction_factory.get_abstraction()

    def do_something(self) -> None:
        self.abstraction.show()


def main() -> None:
    abstraction_factory = ConcreteFactoryB()
    client = Client(abstraction_factory)
    client.do_something()


if __name__ == "__main__":
    main()
