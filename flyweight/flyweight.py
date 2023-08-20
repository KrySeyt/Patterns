from abc import ABC, abstractmethod


class Flyweight(ABC):
    @abstractmethod
    def operation(self, number: int) -> None:
        raise NotImplementedError


class ConcreteFlyweight(Flyweight):
    def operation(self, number: int) -> None:
        incremented_number = number + 1
        print(f"Incremented number is {incremented_number}. Flyweight id: {id(self)}")


class UnsharedConcreteFlyweight(Flyweight):
    def operation(self, number: int) -> None:
        decremented_number = number - 1
        print(f"Decremented number is {decremented_number}. Flyweight id: {id(self)}")


class FlyweightFactory:
    def __init__(self) -> None:
        self._flyweights: dict[str, Flyweight] = {}

    def get_flyweight(self, key: str) -> Flyweight:
        if key == "unique":
            return UnsharedConcreteFlyweight()

        if key in self._flyweights:
            return self._flyweights[key]

        flyweight = ConcreteFlyweight()
        self._flyweights[key] = flyweight
        return flyweight


def main() -> None:
    factory = FlyweightFactory()

    fw1 = factory.get_flyweight("key1")
    fw2 = factory.get_flyweight("key2")
    print(f"Flyweights unique by keys: {fw1 != fw2}")
    fw3 = factory.get_flyweight("key2")
    print(f"One flyweight per key: {fw2 == fw3}")

    fw4 = factory.get_flyweight("unique")
    fw5 = factory.get_flyweight("unique")
    print(f"Unique flyweights are unique {fw4 != fw5}")


if __name__ == "__main__":
    main()
