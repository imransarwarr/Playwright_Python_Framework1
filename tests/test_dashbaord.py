import pytest

from pages.dashboardPage import DashboardPage

@pytest.mark.order(1)
def test_dashboard(logged_in_page):

    dashboard = DashboardPage(logged_in_page)

    dashboard.navigate_to_pim()