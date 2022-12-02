from selene.support.shared import browser
from selene import be,have


def test_search_positive(open_browser):
    browser.element('[name=q]').should(be.blank).type('selene').press_enter()
    browser.element('#search').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_search_negative(open_browser):
    browser.element('[name=q]').should(be.blank).type('ifcniuewyr8743bcuuhdflabcer').press_enter()
    browser.element('#res').should(have.text('Your search - ifcniuewyr8743bcuuhdflabcer - did not match any documents.'))