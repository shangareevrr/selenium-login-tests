from pages.login_page import LoginPage

class TestLoginPage:
    def test_positive_login(self, browser):
        page = LoginPage(browser)
        page.open()
        page.login("admin", "password")
        message = page.get_message()
        assert message == "Успешно! Вход выполнен."

    def test_negative_wrong_username(self, browser):
        page = LoginPage(browser)
        page.open()
        page.login("wrong_user", "password")
        message = page.get_message()
        assert message == "Ошибка: Неверный логин или пароль."

    def test_negative_wrong_password(self, browser):
        page = LoginPage(browser)
        page.open()
        page.login("admin", "wrong_password")
        message = page.get_message()
        assert message == "Ошибка: Неверный логин или пароль."