from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self) -> None:
        raise NotImplementedError


class Subject(ABC):
    change_manager: "ChangeManager"

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        raise NotImplementedError

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        raise NotImplementedError

    @abstractmethod
    def notify(self) -> None:
        raise NotImplementedError


class ChangeManager(ABC):
    subject_to_observers_mapping: dict[Subject, list[Observer]]

    @abstractmethod
    def register(self, subject: Subject, observer: Observer) -> None:
        raise NotImplementedError

    @abstractmethod
    def unregister(self, subject: Subject, observer: Observer) -> None:
        raise NotImplementedError

    @abstractmethod
    def notify(self) -> None:
        raise NotImplementedError


class ConcreteSubject(Subject):
    def __init__(self, change_manager: ChangeManager) -> None:
        self.change_manager = change_manager
        self.state = 5

    def get_state(self) -> int:
        return self.state

    def set_state(self, value: int) -> None:
        self.state = value

    def attach(self, observer: Observer) -> None:
        self.change_manager.register(self, observer)

    def detach(self, observer: Observer) -> None:
        self.change_manager.unregister(self, observer)

    def notify(self) -> None:
        self.change_manager.notify()


class ConcreteObserver(Observer):
    def __init__(self, subject: ConcreteSubject) -> None:
        self.subject = subject
        self.state = 0

        subject.attach(self)

    def update(self) -> None:
        print(f"Observer {id(self)} updated")
        self.state = self.subject.get_state()


class ConcreteChangeManager(ChangeManager):
    def __init__(self) -> None:
        self.subject_to_observers_mapping = {}

    def register(self, subject: Subject, observer: Observer) -> None:
        if subject not in self.subject_to_observers_mapping:
            self.subject_to_observers_mapping[subject] = []
        self.subject_to_observers_mapping[subject].append(observer)

    def unregister(self, subject: Subject, observer: Observer) -> None:
        if observer in self.subject_to_observers_mapping[subject]:
            self.subject_to_observers_mapping[subject].remove(observer)

    # Notifies all observers
    def notify(self) -> None:
        for observers_list in self.subject_to_observers_mapping.values():
            for observer in observers_list:
                observer.update()


def main() -> None:
    change_manager = ConcreteChangeManager()
    subject = ConcreteSubject(change_manager)
    observers = [
        ConcreteObserver(subject),
        ConcreteObserver(subject),
        ConcreteObserver(subject)
    ]

    print("Subject notifying...")
    subject.notify()


if __name__ == "__main__":
    main()
