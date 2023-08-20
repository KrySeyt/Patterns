class Originator:
    def __init__(self) -> None:
        self.state = 5

    def show_state(self) -> None:
        print(self.state)

    def change_state(self) -> None:
        self.state += 1

    def create_memento(self) -> "Memento":
        return Memento(self.state)

    def set_memento(self, memento: "Memento") -> None:
        self.state = memento.get_state()


class Memento:
    def __init__(self, state: int) -> None:
        self.state = state

    def get_state(self) -> int:
        return self.state


def main() -> None:
    orig = Originator()
    orig.show_state()

    memento = orig.create_memento()

    orig.change_state()
    orig.show_state()

    orig.set_memento(memento)
    orig.show_state()


if __name__ == "__main__":
    main()
