import pytest
from playwright.sync_api import sync_playwright
from tests.starting_page import StartingPage
from tests.links_page import LinksPage
from tests.radio_button_page import RadioButtonPage
from utils.logger import setup_logger

logger = setup_logger('ui_test_logger', 'reports/ui_test.log')

@pytest.fixture(scope="session")
def browser():
    logger.info("Set up browser")
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    logger.info("Set up the page")
    context = browser.new_context()
    page = context.new_page()
    return page


def test_correct_data(page):
    logger.info("Start test_correct_data")
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


def test_bad_request_link(page):
    logger.info("Start test_bad_request_link")
    links_page = LinksPage(page)
    links_page.navigate()

    status, status_text = links_page.click_bad_request_link()

    assert status == 400, f"Expected status 400, but got {status}"
    assert status_text == "Bad Request", f"Expected text 'Bad Request', but got {status_text}"


def test_select_impressive_radio_button(page):
    logger.info("Start test_select_impressive_radio_button")
    radio_button_page = RadioButtonPage(page)
    radio_button_page.navigate()

    message = radio_button_page.select_impressive()

    assert message == "You have selected Impressive", f"Expected message 'You have selected Impressive', but got '{message}'"
