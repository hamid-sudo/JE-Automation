from playwright.sync_api import Page


class PosPage:
    def __init__(self, page: Page):
        self.page = page

    def close_tour_if_visible(self):
        end_tour = self.page.get_by_role("button", name="End tour")
        if end_tour.is_visible():
            end_tour.click()

    def select_counter(self, counter_name: str):
        self.page.get_by_role("button", name=counter_name).click()

    def add_product(self, product_name: str):
        self.page.get_by_role("button", name=product_name).click()

    def apply_order_discount(self):
        self.page.get_by_role("button", name="+ Apply %").click()
        self.page.get_by_role("combobox").click()
        self.page.get_by_label("Order-level").get_by_text("Order-level").click()
        self.page.get_by_role("button", name="Apply discount").click()

    def charge_and_print_receipt(self):
        self.page.get_by_role("button", name="Exact · $").click()
        self.page.get_by_role("button", name="Charge $").click()

        # Neutralize the native print dialog before it can open —
        # Playwright can't interact with OS-level dialogs, and they
        # block the tab, causing every subsequent action to hang.
        self.page.evaluate("window.print = () => {}")

        self.page.get_by_role("button", name="Print Receipt").click()
        self.page.get_by_role("button", name="Close", exact=True).click()