from lib.password_checker import *
import pytest

def test_check_password_length_true():
    password_length = PasswordChecker()
    assert password_length.check("12345678")

def test_check_password_length_false():
    password_length = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_length.check("2")
    assert str(e.value) == "Invalid password, must be 8+ characters."