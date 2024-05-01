class Amount:
    def __init__(self, amount: float) -> None:
        self.__amount = amount

    def create(self, amount):
        if amount < 0:
            raise ValueError("The balance cannot be negative")
        return Amount(amount)

    def deposit(self, value: float):
        if value < 0:
            raise ValueError("The value cannot be negative")
        self.__amount += value

    def transfer(self, value: float):
        if value < 0:
            raise ValueError("The value cannot be negative")
        self.__amount -= value

    def get_value(self):
        return self.__amount
