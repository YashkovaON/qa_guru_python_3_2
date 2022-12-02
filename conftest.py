import pytest
from selene.support.shared import browser


@pytest.fixture(scope="function", autouse=True)
def open_browser():
    browser.config.window_height = 1920
    browser.config.window_width = 1080
    b = browser.open('https://google.com/ncr')
    yield b
    browser.close()
