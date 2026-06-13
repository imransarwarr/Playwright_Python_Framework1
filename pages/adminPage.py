from pages.basePage import BasePage


class AdminPage(BasePage):

    # Locators
    admin_menu = "role=link[name='Admin']"
    job_dropdown = "text=Job"
    job_titles_menu = "//a[text()='Job Titles']"
    add_button = "//button[normalize-space()='Add']"

    job_title_input = "(//input[contains(@class,'oxd-input')])[2]"
    description_input = "//textarea[@placeholder='Type description here']"
    note_input = "//textarea[@placeholder='Add note']"
    save_button = "//button[@type='submit']"

    # Actions
    def navigate_to_job_titles(self):
        self.page.get_by_role("link", name="Admin").click()
        self.page.get_by_text("Job", exact=True).click()
        self.page.get_by_role("menuitem", name="Job Titles").click()

    def click_add_job_title(self):
        self.click_element(self.add_button)

    def add_job_title(self, title, description, note):
        self.enter_text(self.job_title_input, title)
        self.enter_text(self.description_input, description)
        self.enter_text(self.note_input, note)
        self.click_element(self.save_button)

    def verify_job_title_exists(self, title):
        return self.page.get_by_text(title).is_visible()