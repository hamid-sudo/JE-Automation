import re
from playwright.sync_api import Page, expect

from utils.config import BASE_URL


def test_dashboard_requires_login(page: Page):
    dashboard_url = BASE_URL.replace("/login", "/dashboard")

    page.goto(dashboard_url)

    expect(page).to_have_url(
        re.compile(r".*/login(?:[/?#].*)?$"),
        timeout=10_000,
    )