class ConcreteProduct:
    def show_name(self) -> None:
        print(f"This is {type(self).__name__}")


class ConcreteCreator:
    def create_product(self) -> ConcreteProduct:
        return ConcreteProduct()


def main() -> None:
    creator = ConcreteCreator()
    product = creator.create_product()
    product.show_name()


if __name__ == "__main__":
    main()
