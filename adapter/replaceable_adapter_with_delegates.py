from abc import ABC, abstractmethod


class AdapteeAccessorDelegate(ABC):
    @abstractmethod
    def get_name(self) -> str:
        raise NotImplementedError


class Client(ABC):
    def __init__(self, adaptee_accessor: AdapteeAccessorDelegate):
        self.product_accessor = adaptee_accessor

    def show_product_name(self) -> None:
        print(self.product_accessor.get_name())


class FirstAdaptee:
    def get_obj_name(self) -> str:
        return "First adaptee name"


class SecondAdaptee:
    def name_of_this_object(self) -> str:
        return "Second adaptee name"


class FirstAdapter(AdapteeAccessorDelegate):
    def __init__(self) -> None:
        self.adaptee = FirstAdaptee()

    def get_name(self) -> str:
        return self.adaptee.get_obj_name()


class SecondAdapter(AdapteeAccessorDelegate):
    def __init__(self) -> None:
        self.adaptee = SecondAdaptee()

    def get_name(self) -> str:
        return self.adaptee.name_of_this_object()


def main() -> None:
    adaptee_delegate = FirstAdapter()
    my_object = Client(adaptee_delegate)
    my_object.show_product_name()


if __name__ == "__main__":
    main()
