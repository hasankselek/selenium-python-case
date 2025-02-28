from selenium.webdriver.common.by import By

from base.base_page import BasePage


class LoginPage(BasePage):
    """Page object for login page"""

    #Locates
    EMAIL_BOX = (By.CSS_SELECTOR,"input[placeholder='E-mail']")
    PASSWORD_BOX = (By.CSS_SELECTOR,"input[placeholder='Password']")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR,".ant-btn.ant-btn-primary")

    def verify_login_page(self):
        current_url = self.get_current_url()
        expected_url = "https://app.forceget.com/system/account/login"
        assert current_url == expected_url, f"Expected URL is {expected_url}, current URL is {current_url}"
        return self

    def fill_email_password(self,email,password):
        self.element_helper.input_text(self.EMAIL_BOX,email)
        self.element_helper.input_text(self.PASSWORD_BOX,password)
        return self

    def click_sign_in(self):
        self.element_helper.click(self.SIGN_IN_BUTTON)
        return self