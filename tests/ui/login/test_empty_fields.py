import re
import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from utils.config import BASE_URL

LOGIN_URL = re.compile(r".*/login(?:[/?#].*)?$")
ERROR_TEXT = re.compile(r"required|enter.*email|enter.*password", re.IGNORECASE)


@pytest.mark.parametrize(
    "email,password",
    [
        ("", ""),
        ("", "AnyPassword123!"),
        ("invalid.user@example.com", ""),
    ],
)
def test_login_requires_email_and_password(page: Page, email: str, password: str):
    login_page = LoginPage(page)

    login_page.open(BASE_URL)
    login_page.login(email, password)

    expect(page).to_have_url(LOGIN_URL, timeout=10_000)
    expect(page.get_by_text(ERROR_TEXT).first).to_be_visible(timeout=10_000)