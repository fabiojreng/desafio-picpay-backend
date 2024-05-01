class Amount:
    def __init__(self, amount: float) -> None:
        self.__amount = amount

    def create(self, amount):
        if amount < 0:
            raise ValueError("The balance cannot be negative")
        return Amount(amount)

    def get_value(self):
        return self.__amount
