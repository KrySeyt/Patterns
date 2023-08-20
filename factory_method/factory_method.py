from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def show_name(self) -> None:
        raise NotImplementedError


class ConcreteProduct(Product):
    def show_name(self) -> None:
        print(f"This is {type(self).__name__}")


class Creator(ABC):
    @abstractmethod
    def create_product(self) -> Product:
        raise NotImplementedError


class ConcreteCreator(Creator):
    def create_product(self) -> Product:
        return ConcreteProduct()


def main() -> None:
    creator: Creator = ConcreteCreator()
    product: Product = creator.create_product()
    product.show_name()


if __name__ == "__main__":
    main()
