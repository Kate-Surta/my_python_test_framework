from playwright.sync_api import Page

class LinksPage:
    def __init__(self, page: Page):
        self.page = page
        self.bad_request_link = page.locator("a#bad-request")

    def navigate(self):
        self.page.goto("https://demoqa.com/links")

    def click_bad_request_link(self):
        with self.page.expect_response("**/bad-request") as response_info:
            self.bad_request_link.click()
        response = response_info.value
        return response.status, response.status_text