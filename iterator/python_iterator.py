from typing import Generic, TypeVar, Self


T = TypeVar("T")


class MyIterator(Generic[T]):
    def __init__(self, aggregate: "Aggregate[T]"):
        self.aggregate = aggregate
        self.current_item_id = 0

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> T:
        if self.current_item_id < len(self.aggregate.items):
            result = self.aggregate.items[self.current_item_id]
            self.current_item_id += 1
            return result

        raise StopIteration


class Aggregate(Generic[T]):
    def __init__(self, values: list[T] | None = None) -> None:
        self.items: list[T] = values or []

    def get_items(self) -> list[T]:
        return self.items

    def __iter__(self) -> MyIterator[T]:
        return MyIterator(self)


def main() -> None:
    agg = Aggregate([1, 2, 3, 4, 5])
    for i in agg:
        print(i)


if __name__ == "__main__":
    main()
