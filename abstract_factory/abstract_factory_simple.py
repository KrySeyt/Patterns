class ProductKit:
    def create_first_product(self) -> "FirstProduct":
        return FirstProduct()

    def create_second_product(self) -> "SecondProduct":
        return SecondProduct()

    def create_third_product(self) -> "ThirdProduct":
        return ThirdProduct()


class UpgradedProductKit(ProductKit):
    def create_first_product(self) -> "UpgradedFirstProduct":
        return UpgradedFirstProduct()

    def create_second_product(self) -> "UpgradedSecondProduct":
        return UpgradedSecondProduct()


class FirstProduct:
    def show_product(self) -> None:
        print("First product")


class UpgradedFirstProduct(FirstProduct):
    def show_product(self) -> None:
        print("Upgraded First product")


class SecondProduct:
    def show_product(self) -> None:
        print("Second product")


class UpgradedSecondProduct(SecondProduct):
    def show_product(self) -> None:
        print("Upgraded Second product")


class ThirdProduct:
    def show_product(self) -> None:
        print("Third product")


def products_user(product_factory: ProductKit) -> None:
    first_product: FirstProduct = product_factory.create_first_product()
    first_product.show_product()

    second_product: SecondProduct = product_factory.create_second_product()
    second_product.show_product()

    third_product: ThirdProduct = product_factory.create_third_product()
    third_product.show_product()


def main() -> None:
    product_factory = UpgradedProductKit()
    products_user(product_factory)


if __name__ == "__main__":
    main()
