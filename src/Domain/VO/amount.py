class Amount:
    def __init__(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("The balance cannot be negative")
        self.__amount = amount

    def get_value(self):
        return self.__amount
