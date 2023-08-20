from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self) -> None:
        raise NotImplementedError


class Subject(ABC):
    observers: list[Observer]

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        raise NotImplementedError

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        raise NotImplementedError

    @abstractmethod
    def notify(self) -> None:
        raise NotImplementedError


class ConcreteSubject(Subject):
    def __init__(self) -> None:
        self.observers = []
        self.state = 5

    def get_state(self) -> int:
        return self.state

    def set_state(self, value: int) -> None:
        self.state = value

    def attach(self, observer: Observer) -> None:
        self.observers.append(observer)

    def detach(self, observer: Observer) -> None:
        if observer in self.observers:
            self.observers.remove(observer)

    def notify(self) -> None:
        for observer in self.observers:
            observer.update()


class ConcreteObserver(Observer):
    def __init__(self, subject: ConcreteSubject) -> None:
        self.subject = subject
        self.state = 0

        subject.attach(self)

    def update(self) -> None:
        print(f"Observer {id(self)} updated")
        self.state = self.subject.get_state()


def main() -> None:
    subject = ConcreteSubject()
    observers = [
        ConcreteObserver(subject),
        ConcreteObserver(subject),
        ConcreteObserver(subject)
    ]

    print("Subject notifying...")
    subject.notify()


if __name__ == "__main__":
    main()
