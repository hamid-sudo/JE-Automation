import re

from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from utils.config import BASE_URL


def test_login_rejects_invalid_credentials(page: Page):
    login_page = LoginPage(page)

    login_page.open(BASE_URL)
    login_page.login(
        email="invalid.user@example.com",
        password="WrongPassword123!",
    )

    expect(page).to_have_url(
        re.compile(r".*/login(?:[/?#].*)?$"),
        timeout=10_000,
    )

    error_message = page.get_by_text(
        re.compile(r"invalid|incorrect|failed|not match", re.IGNORECASE)
    ).first

    expect(error_message).to_be_visible(timeout=10_000)