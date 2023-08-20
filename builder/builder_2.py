from abc import ABC, abstractmethod


class House:
    def __init__(self) -> None:
        self.rooms_count = 0
        self.floors_count = 0

    def __str__(self) -> str:
        return f"Rooms count: {self.rooms_count}, floors count: {self.floors_count}"


class HouseBuilder(ABC):
    def add_room(self) -> None:
        pass

    def add_floor(self) -> None:
        pass

    @abstractmethod
    def get_house(self) -> House:
        raise NotImplementedError


class StandardHouseBuilder(HouseBuilder):
    def __init__(self) -> None:
        self.house = House()

    def add_room(self) -> None:
        self.house.rooms_count += 1

    def add_floor(self) -> None:
        self.house.floors_count += 1

    def get_house(self) -> House:
        return self.house


class HouseDirector:
    def __init__(self, builder: HouseBuilder) -> None:
        self.builder = builder

    def construct(self) -> House:
        self.builder.add_floor()
        self.builder.add_room()
        self.builder.add_room()

        return self.builder.get_house()


def main() -> None:
    builder = StandardHouseBuilder()
    director = HouseDirector(builder)
    house = director.construct()
    print(house)


if __name__ == "__main__":
    main()
