import os, sys

sys.path.insert(0, os.path.abspath(os.curdir))
import pytest
from src.Domain.Entities.user import User


def test_create_user():
    name = "John Doe"
    email = "john.doe@example.com"
    registration_number = "12345678900"
    password = "password"
    amount = 1000.0
    user_type = "Common"

    user = User.create(name, email, registration_number, password, amount, user_type)

    assert user.get_name().get_value() == name
    assert user.get_email().get_value() == email
    assert user.get_registration_number().get_value() == "123.456.789-00"
    assert user.get_amount().get_value() == amount
    assert user.get_user_type().get_value() == user_type
