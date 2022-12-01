import pytest

@pytest.fixture()
def open_browser():
    assert True, "Эта проверка упала в фикстуре"
    b = "browser"
    print("Браузер открыт")
    yield b
    b=""
    print("Браузер закрыт")