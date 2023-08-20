class Singleton:
    _instance = None

    def __new__(cls) -> "Singleton":
        if cls._instance:
            return cls._instance
        cls._instance = super().__new__(cls)
        return cls._instance


def main() -> None:
    inst1 = Singleton()
    print(id(inst1))

    inst2 = Singleton()
    print(id(inst2))

    print(id(inst1) == id(inst2))


if __name__ == "__main__":
    main()

