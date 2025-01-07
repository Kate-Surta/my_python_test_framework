import pytest

from playwright.sync_api import sync_playwright

from tests.starting_page import StartingPage


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    return page


def test_correct_data(page):
    login_page = StartingPage(page)
    login_page.navigate("https://demoqa.com/text-box")
    login_page.fill_form(
        full_name="Donald Duck",
        email="donald.duck@example.com",
        current_address="56 Main St",
        permanent_address="379 Apple Rd"
    )
    output_text = login_page.get_output_text()
    assert output_text["name"] == "Donald Duck"
    assert output_text["email"] == "donald.duck@example.com"
    assert output_text["current_address"] == "56 Main St"
    assert output_text["permanent_address"] == "379 Apple Rd"
