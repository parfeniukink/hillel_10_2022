from abc import ABC, abstractmethod
from uuid import UUID
from providers import StripeAPI, PayPalAPI


class User:
    def __init__(self, name: str) -> None:
        self.name = name


class Product:
    def __init__(self, name: str, price: int) -> None:
        self.name = name
        self.price = price


class PaymentSystem(ABC):
    @abstractmethod
    def authorize(self, user: User) -> UUID:
        """The concrete payment system authentication."""

    @abstractmethod
    def checkout(self, product: Product, token: UUID) -> UUID:
        """Concrete buying realization."""

    @abstractmethod
    def __str__(self) -> str:
        """Mandatory for customer representation."""


class Stripe(PaymentSystem):
    def authorize(self, user: User) -> UUID:
        return StripeAPI.get_token()

    def checkout(self, product: Product, token: UUID) -> UUID:
        order_num: UUID = StripeAPI.checkout(
            product_name=product.name, price=float(product.price), token=token
        )
        return order_num

    def __str__(self) -> str:
        return "Stripe"


class PayPal(PaymentSystem):
    def authorize(self, user: User) -> UUID:
        return PayPalAPI.get_token()

    def checkout(self, product: Product, token: UUID) -> UUID:
        order_num: UUID = PayPalAPI.buy(product_name=product.name, token=token)
        return order_num

    def __str__(self) -> str:
        return "PayPal"


class PaymentProcessor:
    def __init__(
        self, user: User, product: Product, payment_system: PaymentSystem
    ) -> None:
        self.user: User = user
        self.product: Product = product
        self.payment_system: PaymentSystem = payment_system

    def _authorize(self) -> UUID:
        token = self.payment_system.authorize(self.user)
        print(f"🔓 User {self.user.name} is authorized with {self.payment_system}")
        return token

    def buy(self):
        token: UUID = self._authorize()
        order: UUID = self.payment_system.checkout(self.product, token)
        print(
            f"🛍️ Buying {self.product.name} for {self.product.price} with {self.payment_system}. User: {self.user.name}"
        )
        print(f"\tOrder number: {order}")


def main():
    john: User = User(name="John")
    micro: Product = Product(name="Razor", price=1000)

    # Create payment systems from providers SDK
    # stripe = Stripe()
    paypal = PayPal()

    # Make payment
    payment_processor = PaymentProcessor(john, micro, paypal)
    payment_processor.buy()


if __name__ == "__main__":
    # User - just a customer representation
    # Product - shop's product representation
    # Payment system - the class that incapsulates the logic to communicate with provider
    # Payment process - the class that aggregates payment system, user and product
    main()
