import time

from pages.dashboardPage import DashboardPage


def test_dashboard(logged_in_page):

    dashboard = DashboardPage(logged_in_page)

    dashboard.navigate_to_pim()
    time.sleep(2)