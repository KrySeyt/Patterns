# Yes, you can just do parametrized Factory Methods instead if Prototype

from abc import ABC, abstractmethod


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


class ProductFactoryB(ProductFactory):
    def create_first_product(self) -> "FirstProductB":
        return FirstProductB()

    def create_second_product(self) -> "SecondProductB":
        return SecondProductB()

    def create_third_product(self) -> "ThirdProductB":
        return ThirdProductB()


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
    product_factory = ProductFactoryB()
    products_user(product_factory)


if __name__ == "__main__":
    main()
