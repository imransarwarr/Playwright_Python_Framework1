from pages.basePage import BasePage



class PIMPage(BasePage):

    # Locators
    pim_menu = "//span[text()='PIM']"
    add_emp_btn = "//button[normalize-space()='Add']"

    first_name = "input[name='firstName']"
    middle_name = "input[name='middleName']"
    last_name = "input[name='lastName']"

    save_btn = "//button[@type='submit']"

    def click_pim_menu(self):
        self.click_element(self.pim_menu)

    def click_add_employee(self):
        self.click_element(self.add_emp_btn)

    def add_employee(self, first, middle, last):
        self.enter_text(self.first_name, first)
        self.enter_text(self.middle_name, middle)
        self.enter_text(self.last_name, last)

        self.click_element(self.save_btn)