
Простой проект на Python с автотестами входа на сайт.  
Тесты проверяют логин с правильными и неправильными данными.  
Сделано с помощью Selenium + pytest.


1. Перед запуском надо установить несколько библиотек.  
Открой командную строку и введи:

pip install -r requirements.txt


В папке  test:
test_positive_login.py                 Тест с правильными данными
test_negative_wrong_username.py        Тест: неправильный логин
test_negative_wrong_password.py        Тест: неправильный пароль



2. Запускаем тесты, предварительно CD до папки:


pytest -v -s

- `-v` — вывод в подробном виде (verbose)
- `-s` — чтобы видно было `print()` в консоли

3. После запуска в терминале:


tests/test_positive_login.py::test_positive_login 
Сообщение: Успешно! Вход выполнен.
PASSED


