from pages.dashboardPage import DashboardPage
from pages.pimPage import PIMPage
from testData.test_data import TestData


def test_add_employee(logged_in_page):

    dashboard = DashboardPage(logged_in_page)
    pim = PIMPage(logged_in_page)

    dashboard.navigate_to_pim()

    pim.click_add_employee()

    pim.add_employee(
        TestData.FIRST_NAME,
        TestData.MIDDLE_NAME,
        TestData.LAST_NAME
    )

    logged_in_page.locator("h6:has-text('Personal Details')").wait_for()