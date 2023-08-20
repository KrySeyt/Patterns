from abc import ABC, abstractmethod


class House:
    def __init__(self) -> None:
        self.rooms_count = 0
        self.floors_count = 0

    def __str__(self) -> str:
        return f"Rooms count: {self.rooms_count}, floors count: {self.floors_count}"


class HouseBuilder(ABC):
    def _add_room(self) -> None:
        pass

    def _add_floor(self) -> None:
        pass

    @abstractmethod
    def _get_house(self) -> House:
        raise NotImplementedError

    @abstractmethod
    def construct(self) -> House:
        raise NotImplementedError


class StandardHouseBuilder(HouseBuilder):
    def __init__(self) -> None:
        self._house = House()

    def _add_room(self) -> None:
        self._house.rooms_count += 1

    def _add_floor(self) -> None:
        self._house.floors_count += 1

    def _get_house(self) -> House:
        return self._house

    def construct(self) -> House:
        self._add_floor()
        self._add_room()
        self._add_room()

        return self._get_house()


def main() -> None:
    builder: HouseBuilder = StandardHouseBuilder()
    house = builder.construct()
    print(house)


if __name__ == "__main__":
    main()
