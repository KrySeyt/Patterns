from abc import ABC, abstractmethod


class TargetAndClient(ABC):
    @abstractmethod
    def get_product_name(self) -> str:
        ...

    def show_product_name(self) -> None:
        print(self.get_product_name())


class Adaptee:
    def get_name(self) -> str:
        return "Adaptee name"


class Adapter(TargetAndClient):
    def __init__(self) -> None:
        self.product = Adaptee()

    def get_product_name(self) -> str:
        return self.product.get_name()


def main() -> None:
    my_object: TargetAndClient = Adapter()
    my_object.show_product_name()


if __name__ == "__main__":
    main()
