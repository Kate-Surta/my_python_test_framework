from playwright.sync_api import Page

class RadioButtonPage:
    def __init__(self, page: Page):
        self.page = page
        self.impressive_radio_button = page.locator("label[for='impressiveRadio']")
        self.selected_message = page.locator("p.mt-3")

    def navigate(self):
        self.page.goto("https://demoqa.com/radio-button")

    def select_impressive(self):
        self.impressive_radio_button.click()
        return self.selected_message.inner_text()