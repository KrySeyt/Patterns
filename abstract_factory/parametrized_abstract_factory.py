from abc import ABC, abstractmethod
from typing import Callable


class ProductFactory(ABC):
    @abstractmethod
    def create_first_product(self) -> "FirstProduct":
        raise NotImplementedError

    @abstractmethod
    def create_second_product(self) -> "SecondProduct":
        raise NotImplementedError

    @abstractmethod
    def create_third_product(self) -> "ThirdProduct":
        raise NotImplementedError


class ParametrizedFactory(ProductFactory):
    def __init__(
            self,
            first_product_factory: Callable[[], "FirstProduct"],
            second_product_factory: Callable[[], "SecondProduct"],
            third_product_factory: Callable[[], "ThirdProduct"]
    ) -> None:

        self.first_product_factory = first_product_factory
        self.second_product_factory = second_product_factory
        self.third_product_factory = third_product_factory

    def create_first_product(self) -> "FirstProduct":
        return self.first_product_factory()

    def create_second_product(self) -> "SecondProduct":
        return self.second_product_factory()

    def create_third_product(self) -> "ThirdProduct":
        return self.third_product_factory()


class FirstProduct(ABC):
    @abstractmethod
    def show_product(self) -> None:
        raise NotImplementedError


class FirstProductA(FirstProduct):
    def show_product(self) -> None:
        print("First A product")


class FirstProductB(FirstProduct):
    def show_product(self) -> None:
        print("First B product")


class SecondProduct(ABC):
    @abstractmethod
    def show_product(self) -> None:
        raise NotImplementedError


class SecondProductA(SecondProduct):
    def show_product(self) -> None:
        print("Second A product")


class SecondProductB(SecondProduct):
    def show_product(self) -> None:
        print("Second B product")


class ThirdProduct(ABC):
    @abstractmethod
    def show_product(self) -> None:
        raise NotImplementedError


class ThirdProductA(ThirdProduct):
    def show_product(self) -> None:
        print("Third A product")


class ThirdProductB(ThirdProduct):
    def show_product(self) -> None:
        print("Third B product")


def products_user(product_factory: ProductFactory) -> None:
    first_product: FirstProduct = product_factory.create_first_product()
    first_product.show_product()

    second_product: SecondProduct = product_factory.create_second_product()
    second_product.show_product()

    third_product: ThirdProduct = product_factory.create_third_product()
    third_product.show_product()


def main() -> None:
    first_product_factory = FirstProductB
    second_product_factory = SecondProductB
    third_product_factory = ThirdProductA
    products_factory = ParametrizedFactory(
        first_product_factory,
        second_product_factory,
        third_product_factory
    )
    products_user(products_factory)


if __name__ == "__main__":
    main()
