from abc import ABC, abstractmethod


class Target(ABC):
    @abstractmethod
    def show(self) -> None:
        raise NotImplementedError


class Adaptee:
    def get_classname(self) -> str:
        return type(self).__name__


class Adapter(Target):
    def __init__(self) -> None:
        self.adaptee = Adaptee()

    def show(self) -> None:
        print(self.adaptee.get_classname())


def main() -> None:
    adapter = Adapter()
    adapter.show()


if __name__ == "__main__":
    main()
