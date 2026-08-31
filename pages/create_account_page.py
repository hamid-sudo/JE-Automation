from playwright.sync_api import Page


class CreateAccountPage:
    def __init__(self, page: Page):
        self.page = page
        self.create_account_link = page.get_by_role("link", name="Create account")
        self.owner_name_input = page.get_by_role(
            "textbox",
            name="Business Owner Name",
        )
        self.business_email_input = page.get_by_role(
            "textbox",
            name="Business Email",
        )
        self.password_input = page.get_by_role(
            "textbox",
            name="Password",
            exact=True,
        )
        self.confirm_password_input = page.get_by_role(
            "textbox",
            name="Confirm Password",
        )
        self.continue_button = page.get_by_role("button", name="Continue")

    def open(self, login_url: str):
        self.page.goto(login_url)
        self.create_account_link.click()

    def create_account(self, owner_name: str, email: str, password: str):
        self.owner_name_input.fill(owner_name)
        self.business_email_input.fill(email)
        self.password_input.fill(password)
        self.confirm_password_input.fill(password)
        self.continue_button.click()