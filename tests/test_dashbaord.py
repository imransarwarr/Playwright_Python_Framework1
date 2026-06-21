import pytest
import allure

from pages.dashboardPage import DashboardPage


@allure.title("Verify Dashboard Page Functionality")
@allure.description("Validating the Dashboard Page")
@pytest.mark.order(1)
def test_dashboard(logged_in_page):

    dashboard = DashboardPage(logged_in_page)

    with allure.step("Redirect to dashboard page"):
        dashboard.navigate_to_pim()