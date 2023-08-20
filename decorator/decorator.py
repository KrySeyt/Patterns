from abc import ABC, abstractmethod
from typing import Any


class Component(ABC):
    @abstractmethod
    def method(self) -> None:
        raise NotImplementedError


class ConcreteComponent(Component):
    def method(self) -> None:
        print("Concrete component method called")


class Decorator(Component):
    def __init__(self, component: Component) -> None:
        self._component = component

    def method(self) -> None:
        return self._component.method()


class ConcreteDecoratorA(Decorator):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self._added_state = 0

    def method(self) -> None:
        self._added_state += 1
        super().method()
        

class ConcreteDecoratorB(Decorator):
    def added_behavior(self) -> None:
        print("Added behavior")
        
    def method(self) -> None:
        self.added_behavior()
        super().method()


def main() -> None:
    component: Component = ConcreteDecoratorA(
        ConcreteDecoratorB(
            ConcreteComponent()
        )
    )
    component.method()


if __name__ == "__main__":
    main()
