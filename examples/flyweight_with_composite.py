from abc import ABC, abstractmethod


# Flyweight
class GraphNode(ABC):
    @abstractmethod
    def show(self, external_state: str) -> None:
        raise NotImplementedError

    def get_childes(self) -> list["GraphNode"]:
        return []

    def add_child(self, child: "GraphNode") -> None:
        pass

    def remove_child(self, child: "GraphNode") -> None:
        pass


class LeafGraphNode(GraphNode):
    def show(self, external_state: str) -> None:
        print(f"Leaf node with external state \"{external_state}\"")

    def get_childes(self) -> list[GraphNode]:
        return []


# Composite
class CompositeGraphNode(GraphNode):
    def __init__(self) -> None:
        self._childes: list[GraphNode] = []

    def show(self, external_state: str) -> None:
        print(f"Composite node with external state \"{external_state}\"")

    def get_childes(self) -> list[GraphNode]:
        return self._childes

    def add_child(self, child: "GraphNode") -> None:
        self._childes.append(child)

    def remove_child(self, child: "GraphNode") -> None:
        if child in self._childes:
            self._childes.remove(child)
        else:
            raise ValueError("Received node is not a child of this node")


class GraphNodesFactory:
    def __init__(self) -> None:
        self._leaf_node = LeafGraphNode()

    def create_leaf_node(self) -> LeafGraphNode:
        return self._leaf_node

    def create_composite_node(self) -> CompositeGraphNode:
        return CompositeGraphNode()


def main() -> None:
    factory = GraphNodesFactory()
    head = factory.create_composite_node()

    for _ in range(3):
        head.add_child(factory.create_leaf_node())

    print(id(head))
    head.show("Composite external state")
    print()

    for child in head.get_childes():
        print(id(child))
        child.show("Leaf external state")
        print()


if __name__ == "__main__":
    main()
