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

    def show_info(self) -> None:
        product = self.create_product()
        print(f"I am instance of {type(self).__name__} that creates {type(product).__name__} products")


class ConcreteCreator(Creator):
    def create_product(self) -> Product:
        return ConcreteProduct()


def main() -> None:
    creator: Creator = ConcreteCreator()
    creator.show_info()


if __name__ == "__main__":
    main()
