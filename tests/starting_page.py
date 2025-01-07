from playwright.sync_api import Page


class StartingPage:
    def __init__(self, page: Page):
        self.page = page
        self.full_name_input = page.locator("#userName")
        self.email_input = page.locator("#userEmail")
        self.current_address_input = page.locator("#currentAddress")
        self.permanent_address_input = page.locator("#permanentAddress")
        self.submit_button = page.locator("#submit")
        self.output_name = page.locator("#name")
        self.output_email = page.locator("#email")
        self.output_current_address = page.locator("#output #currentAddress")
        self.output_permanent_address = page.locator("#output #permanentAddress")

    def navigate(self, url: str):
        self.page.goto(url)

    def fill_form(self, full_name: str, email: str, current_address: str, permanent_address: str) -> object:
        self.full_name_input.fill(full_name)
        self.email_input.fill(email)
        self.current_address_input.fill(current_address)
        self.permanent_address_input.fill(permanent_address)
        self.submit_button.click()

    def get_output_text(self):
        return {
            "name": self.output_name.inner_text().replace("Name:", "").strip(),
            "email": self.output_email.inner_text().replace("Email:", "").strip(),
            "current_address": self.output_current_address.inner_text().replace("Current Address :", "").strip(),
            "permanent_address": self.output_permanent_address.inner_text().replace("Permananet Address :",
                                                                                    "").strip(),
        }
