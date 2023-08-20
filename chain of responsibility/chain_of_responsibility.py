class Handler:
    def __init__(self, successor: "Handler" | None = None) -> None:
        self._successor = successor

    def handle_request(self) -> None:
        if self._successor:
            return self._successor.handle_request()
        return None


class ConcreteHandlerA(Handler):
    pass


class ConcreteHandlerB(Handler):
    def handle_request(self) -> None:
        print("Handler B")


def main() -> None:
    handler = ConcreteHandlerA(
        ConcreteHandlerA(
            ConcreteHandlerB(
                ConcreteHandlerB(
                    ConcreteHandlerA()
                )
            )
        )
    )

    handler.handle_request()


if __name__ == "__main__":
    main()
