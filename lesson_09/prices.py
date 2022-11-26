from dataclasses import dataclass

# class Price:
#     def convert(self, currency: str):
#         pass


# # price_a + price_b = price_c


@dataclass
class Price:
    amount: int
    currency: str


@dataclass
class ExchangeRates:
    _initialized = False
    def __new__(cls: type[Self]) -> Self:
        instance = ./..

    def __init__(self, filename: str) -> None:
        self._filename = filename

    def convert(self, price: Price, currency: str) -> Price:
        pass


price = Price(amount=12, currency="EUR")
er_file = "..."
er = ExchangeRates(er_file)

er2 = ExchangeRates(er_file)

er.convert(price, "usd")