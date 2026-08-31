import re
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from utils.config import BASE_URL, JE_USERNAME, JE_PASSWORD


def test_user_can_logout(page: Page):
    login_page = LoginPage(page)

    login_page.open(BASE_URL)
    login_page.login(JE_USERNAME, JE_PASSWORD)

    # Replace these two locators with the generated dashboard locators.
    page.get_by_role("button", name=re.compile(r"profile|account|user", re.I)).click()
    page.get_by_role("menuitem", name=re.compile(r"log ?out|sign out", re.I)).click()

    expect(page).to_have_url(
        re.compile(r".*/login(?:[/?#].*)?$"),
        timeout=10_000,
    )