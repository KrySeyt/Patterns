import datetime
from abc import ABC, abstractmethod


class AbstractClass(ABC):
    def template_method(self) -> None:
        obj_name = self.get_name()
        current_time = self.get_current_time()
        print(f"{obj_name} object in {current_time}")

    @abstractmethod
    def get_name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_current_time(self) -> str:
        raise NotImplementedError


class ConcreteClass(AbstractClass):
    def get_name(self) -> str:
        return "ConcreteClassObject"
    
    def get_current_time(self) -> str:
        return str(datetime.datetime.now())


def main() -> None:
    obj = ConcreteClass()
    obj.template_method()


if __name__ == "__main__":
    main()
