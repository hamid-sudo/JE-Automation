from playwright.sync_api import Page

from pages.login_page import LoginPage
from utils.config import BASE_URL


def test_password_is_masked(page: Page):
    login_page = LoginPage(page)

    login_page.open(BASE_URL)

    assert login_page.password_input.get_attribute("type") == "password"