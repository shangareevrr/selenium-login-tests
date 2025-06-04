from pages.login_page import LoginPage

def test_positive_login(browser):
    page = LoginPage(browser)
    page.open()
    page.login("admin", "password")
    message = page.get_message()
    print("Сообщение:", message)
    assert message == "Успешно! Вход выполнен."
