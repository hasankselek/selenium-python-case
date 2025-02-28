import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from base.base_page import BasePage

class RegisterPage(BasePage):
    """Page object for register page"""

    # Locates
    FIRSTNAME_INPUT = (By.ID, "firstName")
    LASTNAME_INPUT = (By.ID, "lastName")
    COUNTRY_DROPDOWN = (By.XPATH,"(//nz-select[@class='ant-select w-full ng-tns-c364634890-11 ant-select-in-form-item ant-select-show-arrow ant-select-show-search ant-select-single ng-untouched ng-pristine ng-valid ng-star-inserted'])[1]")
    COUNTRY_INPUT = (By.CSS_SELECTOR, "input.ant-select-selection-search-input")
    MOBILENUMBER_INPUT = (By.ID, "phoneNumber")
    COMPANY_INPUT = (By.ID, "companyName")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[placeholder='E-mail']")
    TITLE_DROPDOWN = (By.XPATH, "(//div[@class='ant-form-item-control-input-content ng-tns-c2837444922-6'])[1]")
    TITLE_INPUT = (By.XPATH,"//div[@class='ant-select-item-option-content']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[placeholder='Password']")
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[placeholder='Confirm password']")
    CHECKBOX = (By.CSS_SELECTOR, ".checkbox-box")
    ACCEPT_BUTTON = (By.CSS_SELECTOR, "button[class='ant-btn ant-btn-primary']")
    AGREE_SIGNUP_BUTTON = (By.CSS_SELECTOR, ".ant-btn.w-full.ant-btn-primary")
    VERIFICATION_CODE_BOX = (By.XPATH,"//div[@class='cdk-overlay-container']//input[1]")
    LOGIN_BUTTON = (By.XPATH,"//div[@class='cdk-overlay-container']")


    def __init__(self, driver):
        """
        Initialize RegisterPage

        Args:
            driver: WebDriver instance
        """
        super().__init__(driver)
        # Page URL - append to base URL
        self.page_url = "/register"

    def navigate_to_register_page(self):
        """Navigate to register page"""
        self.navigate_to(self.page_url)

    def fill_firstname(self, firstname):
        self.element_helper.input_text(self.FIRSTNAME_INPUT, firstname)
        time.sleep(1)
        return self

    def fill_lastname(self, lastname):
        self.element_helper.input_text(self.LASTNAME_INPUT, lastname)
        time.sleep(1)
        return self

    def select_country(self, country):
        self.element_helper.click(self.COUNTRY_DROPDOWN)
        time.sleep(2)
        self.element_helper.input_text(self.COUNTRY_INPUT, country)
        time.sleep(2)
        self.element_helper.input_text(self.COUNTRY_INPUT, Keys.ENTER)
        return self

    def fill_mobile_number(self, mobile_number):
        self.element_helper.input_text(self.MOBILENUMBER_INPUT, mobile_number)
        time.sleep(1)
        return self

    def fill_company(self, company):
        self.element_helper.input_text(self.COMPANY_INPUT, company)
        time.sleep(1)
        return self

    def fill_email(self, email):
        self.element_helper.input_text(self.EMAIL_INPUT, email)
        time.sleep(1)
        return self

    def select_title(self, title):
        """Dropdown aç ve belirli bir title seç"""
        self.element_helper.click(self.TITLE_DROPDOWN)
        time.sleep(2)

        # **Tüm title seçeneklerini bul**
        options = self.driver.find_elements(*self.TITLE_INPUT)

        for option in options:
            if option.text.strip() == title:  # WebElement'ten metni al
                option.click()
                break
        return self

    def fill_password(self, password):
        self.element_helper.input_text(self.PASSWORD_INPUT, password)
        time.sleep(1)
        return self

    def fill_confirm_password(self, confirm_password):
        self.element_helper.input_text(self.CONFIRM_PASSWORD_INPUT, confirm_password)
        return self

    def fill_user_information(self, firstname, lastname, country, mobile_number, company, email, title, password,
                              confirm_password):

        (self.fill_firstname(firstname)
             .fill_lastname(lastname)
             .select_country(country)
             .fill_mobile_number(mobile_number)
             .fill_company(company)
             .fill_email(email)
             .select_title(title)
             .fill_password(password)
             .fill_confirm_password(confirm_password))
        return self


    def click_privacy_policy_checkbox(self):
        self.element_helper.click(self.CHECKBOX)
        self.element_helper.click(self.ACCEPT_BUTTON)
        time.sleep(3)
        return self

    def click_agree_signup_button(self):
        self.element_helper.click(self.AGREE_SIGNUP_BUTTON)
        time.sleep(2)
        return self

    def fill_verification_code(self,code):
        self.element_helper.input_text(self.VERIFICATION_CODE_BOX,code)
        self.element_helper.wait_for_element_visible(self.LOGIN_BUTTON)
        time.sleep(3)
        return self

    def verify_account_created(self):
        assert self.element_helper.find(self.LOGIN_BUTTON).is_displayed()
        self.element_helper.click(self.LOGIN_BUTTON)
        time.sleep(5)
        return self



