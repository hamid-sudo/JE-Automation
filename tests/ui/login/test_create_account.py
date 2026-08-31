import re
import uuid

from playwright.sync_api import Page, expect

from pages.create_account_page import CreateAccountPage
from utils.config import (
    BASE_URL,
    TEST_ACCOUNT_PASSWORD,
    TEST_EMAIL_DOMAIN,
    TEST_EMAIL_PREFIX,
    TEST_OWNER_NAME,
)


def test_create_new_account(page: Page):
    create_account_page = CreateAccountPage(page)

    unique_email = (
        f"{TEST_EMAIL_PREFIX}+{uuid.uuid4().hex[:8]}@{TEST_EMAIL_DOMAIN}"
    )

    create_account_page.open(BASE_URL)
    registration_url = page.url

    create_account_page.create_account(
        owner_name=TEST_OWNER_NAME,
        email=unique_email,
        password=TEST_ACCOUNT_PASSWORD,
    )

    expect(page).not_to_have_url(
        re.compile(re.escape(registration_url)),
        timeout=15_000,
    )
