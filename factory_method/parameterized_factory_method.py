from abc import ABC, abstractmethod
from typing import Callable


class Product(ABC):
    @abstractmethod
    def show_name(self) -> None:
        raise NotImplementedError


class ConcreteProductA(Product):
    def show_name(self) -> None:
        print("Product A")


class ConcreteProductB(Product):
    def show_name(self) -> None:
        print("Product B")


class Creator:
    # Or move product_factory to __init__
    def create_product(self, product_factory: Callable[[], Product]) -> Product:
        return product_factory()


def main() -> None:
    creator = Creator()
    product_factory = ConcreteProductB
    product = creator.create_product(product_factory)
    product.show_name()


if __name__ == "__main__":
    main()
