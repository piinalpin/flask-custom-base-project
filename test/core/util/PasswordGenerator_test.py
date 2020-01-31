from src.core.util.PasswordGenerator import *


def test_password_positive():
    password = hash_password("test1")
    assert verify_password(password, "test1")


def test_password_negative():
    password = hash_password("test2")
    assert not verify_password(password, "test1")
