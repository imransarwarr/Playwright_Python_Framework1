import allure
import pytest

from pages.dashboardPage import DashboardPage
from pages.pimPage import PIMPage
from testData.test_data import TestData
from utilities.logger import setup_logger

logger = setup_logger()

@allure.title("Verify PIM Page Functionality")
@allure.description("Validating PIM Page")

@pytest.mark.order(2)
def test_add_employee(logged_in_page):

    dashboard = DashboardPage(logged_in_page)
    pim = PIMPage(logged_in_page)

    dashboard.navigate_to_pim()

    with allure.step("Click Add Employee"):

        pim.click_add_employee()

    with allure.step("Adding Employee Details"):
        pim.add_employee(
            TestData.FIRST_NAME,
            TestData.MIDDLE_NAME,
            TestData.LAST_NAME
        )

    with allure.step("Verify Personal Details page"):
        logged_in_page.locator("h6:has-text('Personal Details')").wait_for()

        logger.info("User landed on PIM Page Successfully")
