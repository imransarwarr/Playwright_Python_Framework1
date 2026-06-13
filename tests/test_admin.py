import pytest

from pages.adminPage import AdminPage
from testData.excel_reader import get_excel_data


@pytest.mark.parametrize(
    "job_title,description,note",
    get_excel_data("JobTitles")
)
def test_add_job_title(logged_in_page, job_title, description, note):

    admin = AdminPage(logged_in_page)

    admin.navigate_to_job_titles()
    admin.click_add_job_title()

    admin.add_job_title(
        job_title,
        description,
        note
    )

    # Verify Job Title is visible in table
    locator = logged_in_page.locator(f"text='{job_title}'")

    locator.wait_for()
    assert locator.is_visible()