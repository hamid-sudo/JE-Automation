import re
from playwright.sync_api import Page, expect

from utils.config import BASE_URL


def test_forgot_password_opens_reset_page(page: Page):
    page.goto(BASE_URL)

    forgot_password_link = page.get_by_role(
        "link",
        name=re.compile(r"forgot.*password", re.IGNORECASE),
    )
    forgot_password_link.click()

    expect(page).to_have_url(
        re.compile(r".*(forgot|reset).*", re.IGNORECASE),
        timeout=10_000,
    )