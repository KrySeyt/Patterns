from abc import ABC, abstractmethod
from typing import Self


class Prototype(ABC):
    @abstractmethod
    def clone(self) -> Self:
        raise NotImplementedError

    def __str__(self) -> str:
        return f"{type(self).__name__}"


class ConcretePrototypeA(Prototype):
    def clone(self) -> Self:
        return type(self)()


class ConcretePrototypeB(Prototype):
    def clone(self) -> Self:
        return type(self)()


class Client:
    def __init__(self, prototype: Prototype) -> None:
        self.prototype = prototype

    def get_product(self) -> Prototype:
        return self.prototype.clone()


def main() -> None:
    prototype = ConcretePrototypeB()
    client = Client(prototype)
    product = client.get_product()
    print(product)


if __name__ == "__main__":
    main()
