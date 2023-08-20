from abc import ABC, abstractmethod
from typing import Callable


class Target(ABC):
    @abstractmethod
    def show(self) -> None:
        raise NotImplementedError


class Adaptee:
    def get_classname(self) -> str:
        return type(self).__name__


class Adapter(Target):
    def __init__(
            self,
            adaptee: Adaptee,
            show_adapter: Callable[[Adaptee], None],
            show_first_letter_of_classname_adapter: Callable[[Adaptee], None]
    ) -> None:

        self.adaptee = adaptee
        self.show_adapter = show_adapter
        self.show_first_letter_of_classname_adapter = show_first_letter_of_classname_adapter

    def show(self) -> None:
        return self.show_adapter(self.adaptee)

    def show_first_letter_of_classname(self) -> None:
        return self.show_first_letter_of_classname_adapter(self.adaptee)


def adaptee_show_adapter(adaptee: Adaptee) -> None:
    print(adaptee.get_classname())


def adaptee_show_first_letter_of_classname_adapter(adaptee: Adaptee) -> None:
    print(adaptee.get_classname()[0])


def main() -> None:
    adaptee = Adaptee()
    adapter = Adapter(
        adaptee,
        adaptee_show_adapter,
        adaptee_show_first_letter_of_classname_adapter
    )
    adapter.show()
    adapter.show_first_letter_of_classname()


if __name__ == "__main__":
    main()
