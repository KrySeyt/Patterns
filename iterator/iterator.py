from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Callable


T = TypeVar("T")


class ExternalIterator(ABC, Generic[T]):
    @abstractmethod
    def first(self) -> None:
        raise NotImplementedError

    def next(self) -> None:
        raise NotImplementedError

    def is_done(self) -> bool:
        raise NotImplementedError

    def current_item(self) -> T:
        raise NotImplementedError


class InternalIterator(ABC, Generic[T]):
    @abstractmethod
    def map(self, func: Callable[[T], bool]) -> bool:
        raise NotImplementedError


class Aggregate(list[T], ABC):
    @abstractmethod
    def create_iterator(self) -> ExternalIterator[T]:
        raise NotImplementedError


class ExternalConcreteIterator(ExternalIterator[T]):
    def __init__(self, aggregate: Aggregate[T]) -> None:
        self.aggregate = aggregate
        self.current_item_id: int = 0

    def first(self) -> None:
        self.current_item_id = 0

    def is_done(self) -> bool:
        return self.current_item_id >= len(self.aggregate)

    def current_item(self) -> T:
        return self.aggregate[self.current_item_id]

    def next(self) -> None:
        self.current_item_id += 1


class ConcreteInternalIterator(InternalIterator[T]):
    def __init__(self, aggregate: Aggregate[T]) -> None:
        self.aggregate = aggregate

    def map(self, func: Callable[[T], bool]) -> bool:
        for i in self.aggregate:
            result = func(i)
            if not result:
                return result

        return True


class ConcreteAggregate(Aggregate[T]):
    def create_iterator(self) -> ExternalConcreteIterator[T]:
        return ExternalConcreteIterator(self)


def main() -> None:
    agg = ConcreteAggregate((1, 2, 3))

    # External iterator
    external_iterator = agg.create_iterator()

    print("External iterator:")

    external_iterator.first()
    while not external_iterator.is_done():
        item = external_iterator.current_item()
        print(item)
        external_iterator.next()

    # Internal iterator
    internal_iterator = ConcreteInternalIterator(agg)

    print()
    print("Internal iterator:")

    def show_agg_elem(x: T) -> bool:
        print(x)
        return True

    internal_iterator.map(show_agg_elem)


if __name__ == "__main__":
    main()

