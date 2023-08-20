from abc import ABC, abstractmethod


class Subject(ABC):
    @abstractmethod
    def operation(self) -> None:
        raise NotImplementedError


class RealSubject(Subject):
    def operation(self) -> None:
        print("Real subject operation")


class SubjectProxy(Subject):
    def __init__(self, real_subject: RealSubject) -> None:
        self.real_subject = real_subject

    def operation(self) -> None:
        return self.real_subject.operation()


def main() -> None:
    proxy = SubjectProxy(RealSubject())
    proxy.operation()


if __name__ == "__main__":
    main()
