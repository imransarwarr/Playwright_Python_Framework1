import pytest
from pages.loginPage import LoginPage
from utilities.logger import setup_logger

from pages.loginPage import LoginPage
from utilities.configReader import ConfigReader

logger = setup_logger()

@pytest.fixture()
def login_page(page):
    page.goto(ConfigReader.QA_URL)
    return LoginPage(page)
logger.info("Login Successful")