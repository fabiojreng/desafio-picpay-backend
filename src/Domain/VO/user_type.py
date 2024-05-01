class UserType:
    def __init__(self, user_type: str) -> None:
        valid_types = ["Common", "Shopkeepers"]
        if user_type not in valid_types:
            raise ValueError("Invalid user type. Use 'Common' or 'Shopkeepers'")
        self.__value = user_type

    def get_value(self):
        return self.__value
