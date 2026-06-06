import pytest
from playwright.sync_api import sync_playwright

from pages.loginPage import LoginPage
from utilities.configReader import ConfigReader


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session", params=["chromium"])
#@pytest.fixture(scope="session", params=["chromium", "firefox"])
def browser(request, playwright_instance):

    browser_name = request.param

    browser = getattr(playwright_instance, browser_name).launch(
        headless=False,
        slow_mo=1000
    )

    yield browser

    browser.close()


@pytest.fixture()
def page(browser):

    page = browser.new_page()

    yield page

    page.close()


@pytest.fixture()
def logged_in_page(page):

    page.goto(ConfigReader.QA_URL)

    login = LoginPage(page)

    login.login(
        ConfigReader.USERNAME,
        ConfigReader.PASSWORD
    )

    return page