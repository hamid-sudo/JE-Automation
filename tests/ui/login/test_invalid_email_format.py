import re
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from utils.config import BASE_URL


def test_login_rejects_invalid_email_format(page: Page):
    login_page = LoginPage(page)

    login_page.open(BASE_URL)
    login_page.login("not-a-valid-email", "AnyPassword123!")

    expect(page).to_have_url(
        re.compile(r".*/login(?:[/?#].*)?$"),
        timeout=10_000,
    )