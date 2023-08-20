from __future__ import annotations
from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def operation(self) -> None:
        raise NotImplementedError

    def add(self, component: "Component") -> None:
        pass

    def remove(self, component: "Component") -> None:
        pass

    def get_child(self, child_id: int) -> "Component" | None:
        return None


class Leaf(Component):
    def operation(self) -> None:
        print("Leaf operation")


class Composite(Component):
    def __init__(self) -> None:
        self.childes: list[Component] = []

    def operation(self) -> None:
        print("Composite childes operations START")
        for child in self.childes:
            child.operation()
        print("Composite childes operations END")

    def add(self, component: "Component") -> None:
        self.childes.append(component)

    def remove(self, component: "Component") -> None:
        self.childes.remove(component)

    def get_child(self, child_id: int) -> Component | None:
        if len(self.childes) >= child_id:
            return self.childes[child_id]
        return None


def main() -> None:
    composite = Composite()
    composite.add(Leaf())
    composite.add(Leaf())
    components: list[Component] = [
        Leaf(),
        Leaf(),
        composite,
        Leaf()
    ]

    for component in components:
        component.operation()


if __name__ == "__main__":
    main()
