from abc import ABC, abstractmethod


class Visitor:
    def visit_element_a(self, element: "ConcreteElementA") -> None:
        pass

    def visit_element_b(self, element: "ConcreteElementB") -> None:
        pass


class ConcreteVisitor1(Visitor):
    def visit_element_a(self, element: "ConcreteElementA") -> None:
        print("Visitor 1 Element A")

    def visit_element_b(self, element: "ConcreteElementB") -> None:
        print("Visitor 1 Element B")


class ConcreteVisitor2(Visitor):
    def visit_element_a(self, element: "ConcreteElementA") -> None:
        print("Visitor 2 Element A")

    def visit_element_b(self, element: "ConcreteElementB") -> None:
        print("Visitor 2 Element B")


class Element(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        raise NotImplementedError


class ConcreteElementA(Element):
    def accept(self, visitor: Visitor) -> None:
        visitor.visit_element_a(self)


class ConcreteElementB(Element):
    def accept(self, visitor: Visitor) -> None:
        visitor.visit_element_b(self)


class ObjectStructure:
    def __init__(self, objects: list[Element]) -> None:
        self.objects: list[Element] = objects

    def visit(self, visitor: Visitor) -> None:
        for obj in self.objects:
            obj.accept(visitor)


def main() -> None:
    object_structure = ObjectStructure(
        [
            ConcreteElementA(),
            ConcreteElementB(),
            ConcreteElementB(),
            ConcreteElementA()
        ]
    )
    visitor1 = ConcreteVisitor1()
    object_structure.visit(visitor1)

    print()

    visitor2 = ConcreteVisitor2()
    object_structure.visit(visitor2)


if __name__ == "__main__":
    main()
