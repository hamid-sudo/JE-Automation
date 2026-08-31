import pytest
from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError

from pages.login_page import LoginPage
from pages.pos_page import PosPage
from utils.config import (
    BASE_URL,
    JE_PASSWORD,
    JE_USERNAME,
    POS_COUNTER_NAME,
    POS_PRODUCT_NAME,
    RUN_POS_TRANSACTION_TESTS,
)


def close_dashboard_tour_if_visible(page: Page, timeout: int = 5000) -> None:
    """Dismiss the dashboard onboarding tour, mirroring PosPage.close_tour_if_visible."""
    end_tour_btn = page.get_by_role("button", name="End tour")

    if end_tour_btn.count() > 0 and end_tour_btn.first.is_visible():
        end_tour_btn.first.click()

    overlay = page.locator(".driver-overlay")
    if overlay.count() == 0:
        return

    try:
        overlay.first.wait_for(state="hidden", timeout=timeout)
    except PlaywrightTimeoutError:
        # Last resort: remove it directly from the DOM.
        page.evaluate(
            """
            () => {
                document.querySelectorAll('.driver-overlay, .driver-popover')
                    .forEach(el => el.remove());
            }
            """
        )
        page.wait_for_timeout(200)


@pytest.mark.pos_transaction
def test_pos_sale_with_order_discount(page: Page):
    if RUN_POS_TRANSACTION_TESTS.lower() != "true":
        pytest.skip("POS transaction tests are disabled.")

    login_page = LoginPage(page)
    login_page.open(BASE_URL)
    login_page.login(JE_USERNAME, JE_PASSWORD)

    close_dashboard_tour_if_visible(page)

    launch_pos_btn = page.get_by_role("button", name="Launch POS")
    launch_pos_btn.wait_for(state="visible", timeout=10000)
    launch_pos_btn.scroll_into_view_if_needed()

    try:
        with page.expect_popup(timeout=15000) as popup_info:
            launch_pos_btn.click(timeout=8000)
    except PlaywrightTimeoutError:
        close_dashboard_tour_if_visible(page)
        page.screenshot(path="screenshots/launch_pos_before_force_click.png")
        with page.expect_popup(timeout=15000) as popup_info:
            launch_pos_btn.click(force=True)

    pos_browser_page = popup_info.value
    pos_browser_page.wait_for_load_state()

    pos_page = PosPage(pos_browser_page)
    pos_page.close_tour_if_visible()
    pos_page.select_counter(POS_COUNTER_NAME)
    pos_page.add_product(POS_PRODUCT_NAME)
    pos_page.apply_order_discount()
    pos_page.charge_and_print_receipt()