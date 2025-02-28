from selenium.webdriver.common.by import By

from base.base_page import BasePage


class DashboardPage(BasePage):
    """Page object for dashboard page"""

    #Locates
    USER_FIRST_LASTNAME = (By.CSS_SELECTOR,".m-b-0.text-dark.font-weight-semibold")
    AVATAR_ICON = (By.CSS_SELECTOR,"nz-avatar[class='ant-avatar ant-avatar-circle ant-avatar-icon']")

    def click_avatar_icon(self):
        self.element_helper.click(self.AVATAR_ICON)
        return self

    def confirm_login(self,first_name,last_name):

        """ Full Name Check """
        current_full_name = self.element_helper.get_text(self.USER_FIRST_LASTNAME)
        expected_full_name = first_name + ' ' + last_name
        assert current_full_name == expected_full_name
        return self