import pytest
from pages.login_page import LoginPage

def test_negative_wrong_username(browser):
    page = LoginPage(browser)
    page.open()
    page.login("wrong_user", "password")
    message = page.get_message()
    print("Сообщение:", message)
    assert message == "Ошибка: Неверный логин или пароль."