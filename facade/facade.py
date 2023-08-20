class SubsystemClass1:
    def very_difficult_method(self) -> None:
        print("Low-level things")


class SubsystemClass2:
    def another_difficult_behavior(self) -> None:
        print("More low-level things")


class SubsystemClass3:
    def more_lowlevel_behavior(self) -> None:
        print("Low-level operations")


class Facade:
    def __init__(self) -> None:
        self._class1_inst = SubsystemClass1()
        self._class2_inst = SubsystemClass2()
        self._class3_inst = SubsystemClass3()

    def just_do_magic(self) -> None:
        self._class1_inst.very_difficult_method()
        self._class2_inst.another_difficult_behavior()
        self._class3_inst.more_lowlevel_behavior()


def main() -> None:
    facade = Facade()
    facade.just_do_magic()


if __name__ == "__main__":
    main()
