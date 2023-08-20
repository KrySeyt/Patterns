from abc import ABC, abstractmethod
from typing import Self


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


class ProductFactoryA(ProductFactory):
    def create_first_product(self) -> "FirstProductA":
        return FirstProductA()

    def create_second_product(self) -> "SecondProductA":
        return SecondProductA()

    def create_third_product(self) -> "ThirdProductA":
        return ThirdProductA()


class PrototypeProductFactory(ProductFactory):
    def __init__(
            self,
            first_product_prototype: "FirstProduct",
            second_product_prototype: "SecondProduct",
            third_product_prototype: "ThirdProduct"
    ) -> None:

        self.first_product_prototype = first_product_prototype
        self.second_product_prototype = second_product_prototype
        self.third_product_prototype = third_product_prototype

    def create_first_product(self) -> "FirstProduct":
        return self.first_product_prototype.clone()

    def create_second_product(self) -> "SecondProduct":
        return self.second_product_prototype.clone()

    def create_third_product(self) -> "ThirdProduct":
        return self.third_product_prototype.clone()


class Prototype(ABC):
    @abstractmethod
    def clone(self) -> Self:
        raise NotImplementedError


class FirstProduct(Prototype):
    @abstractmethod
    def show_product(self) -> None:
        raise NotImplementedError


class FirstProductA(FirstProduct):
    def show_product(self) -> None:
        print("First A product")

    def clone(self) -> Self:
        return type(self)()


class FirstProductB(FirstProduct):
    def show_product(self) -> None:
        print("First B product")

    def clone(self) -> Self:
        return type(self)()


class SecondProduct(Prototype):
    @abstractmethod
    def show_product(self) -> None:
        raise NotImplementedError


class SecondProductA(SecondProduct):
    def show_product(self) -> None:
        print("Second A product")

    def clone(self) -> Self:
        return type(self)()


class SecondProductB(SecondProduct):
    def show_product(self) -> None:
        print("Second B product")

    def clone(self) -> Self:
        return type(self)()


class ThirdProduct(Prototype):
    @abstractmethod
    def show_product(self) -> None:
        raise NotImplementedError


class ThirdProductA(ThirdProduct):
    def show_product(self) -> None:
        print("Third A product")

    def clone(self) -> Self:
        return type(self)()


class ThirdProductB(ThirdProduct):
    def show_product(self) -> None:
        print("Third B product")

    def clone(self) -> Self:
        return type(self)()


def products_user(product_factory: ProductFactory) -> None:
    first_product: FirstProduct = product_factory.create_first_product()
    first_product.show_product()

    second_product: SecondProduct = product_factory.create_second_product()
    second_product.show_product()

    third_product: ThirdProduct = product_factory.create_third_product()
    third_product.show_product()


def main() -> None:
    first_product_proto = FirstProductB()
    second_product_proto = SecondProductA()
    third_product_proto = ThirdProductB()
    product_factory = PrototypeProductFactory(
        first_product_proto,
        second_product_proto,
        third_product_proto
    )
    products_user(product_factory)


if __name__ == "__main__":
    main()
