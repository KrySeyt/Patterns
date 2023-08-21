from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def algorithm_interface(self) -> None:
        raise NotImplementedError


class ConcreteStrategyA(Strategy):
    def algorithm_interface(self) -> None:
        print("Strategy A")


class ConcreteStrategyB(Strategy):
    def algorithm_interface(self) -> None:
        print("Strategy B")


class Context:
    def __init__(self, strategy: Strategy) -> None:
        self.strategy = strategy

    def context_interface(self) -> None:
        return self.strategy.algorithm_interface()

    def set_strategy(self, strategy: Strategy) -> None:
        self.strategy = strategy


def main() -> None:
    strategy1 = ConcreteStrategyA()
    context = Context(strategy1)
    context.context_interface()

    strategy2 = ConcreteStrategyB()
    context.set_strategy(strategy2)
    context.context_interface()


if __name__ == "__main__":
    main()
