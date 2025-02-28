import time

from config.config import Config
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.dashboard_page import DashboardPage

class TestRegisterLogin:

    def test_successful_register_login(self, setup_driver):
        # Driver ve sayfa nesnelerini oluşturuyoruz
        driver = setup_driver
        register_page = RegisterPage(driver)
        login_page = LoginPage(driver)
        dashboard_page = DashboardPage(driver)
        config_page = Config()

        # Kayıt sayfasına yönleniyoruz
        register_page.navigate_to_register_page()

        # Cloudflare kontrolü için bekleme süresi
        time.sleep(5)

        # Kayıt formunu doldurup, gerekli adımları zincirleme yöntemiyle çağırıyoruz
        (
            register_page.fill_user_information(
                config_page.FIRST_NAME,
                config_page.LAST_NAME,
                config_page.COUNTRY,
                config_page.MOBILE_NUMBER,
                config_page.COMPANY,
                config_page.EMAIL,
                config_page.TITLE,
                config_page.PASSWORD,
                config_page.PASSWORD,
            )
            .click_privacy_policy_checkbox()
            .click_agree_signup_button()
            .fill_verification_code(config_page.VERIFICATION_CODE)
            .verify_account_created()
        )

        # Giriş sayfasında işlemleri gerçekleştiriyoruz
        (
            login_page.verify_login_page()
            .fill_email_password(config_page.EMAIL,
                                 config_page.PASSWORD)
            .click_sign_in()
        )

        #Başarılı bir şekilde giriş yaptığını doğruluyoruz
        (
            dashboard_page.click_avatar_icon()
            .confirm_login(config_page.FIRST_NAME,
                           config_page.LAST_NAME))
