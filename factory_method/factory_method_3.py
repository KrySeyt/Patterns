from abc import ABC, abstractmethod
from typing import Callable


class Product(ABC):
    @abstractmethod
    def show_name(self) -> None:
        raise NotImplementedError


class ConcreteProduct(Product):
    def show_name(self) -> None:
        print(f"This is {type(self).__name__}")


class Creator(ABC):
    # This is Factory Method
    @abstractmethod
    def _get_product_factory(self) -> Callable[[], Product]:
        raise NotImplementedError

    # This is NOT Factory Method
    def create_product(self) -> Product:
        return self._get_product_factory()()

    def show_info(self) -> None:
        product = self.create_product()
        print(f"I am instance of {type(self).__name__} that creates {type(product).__name__} products")


class ConcreteCreator(Creator):
    def _get_product_factory(self) -> Callable[[], Product]:
        return ConcreteProduct


def main() -> None:
    creator: Creator = ConcreteCreator()
    creator.show_info()


if __name__ == "__main__":
    main()
