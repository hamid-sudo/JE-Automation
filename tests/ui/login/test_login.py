import re

from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from utils.config import BASE_URL, JE_USERNAME, JE_PASSWORD


def test_valid_login_opens_dashboard(page: Page):
    login_page = LoginPage(page)

    login_page.open(BASE_URL)
    login_page.login(JE_USERNAME, JE_PASSWORD)

    expect(page).not_to_have_url(
        re.compile(r".*/login(?:[/?#].*)?$"),
        timeout=15_000,
    )