import pytest
from pages.login_page import LoginPage

def test_negative_wrong_password(browser):
    page = LoginPage(browser)
    page.open()
    page.login("admin", "wrong_password")
    message = page.get_message()
    print("Сообщение:", message)
    assert message == "Ошибка: Неверный логин или пароль."