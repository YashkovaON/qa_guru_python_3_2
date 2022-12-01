import pytest



@pytest.fixture()
def create_user(open_browser):
    assert True, "Эта проверка упала в фикстуре подготовки пользователя"
    return 35

def test_body(open_browser, create_user):
    assert open_browser == "browser"
    assert create_user == 35