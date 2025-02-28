import time
import undetected_chromedriver as uc
from selenium import webdriver
from config.config import Config


class DriverFactory:
    """Factory class for creating WebDriver instances"""

    @staticmethod
    def get_driver():
        """
        Create and return a WebDriver instance based on configuration

        Returns:
            WebDriver: Configured WebDriver instance
        """
        browser = Config.BROWSER.lower()
        headless = Config.HEADLESS

        if browser == "chrome":
            options = uc.ChromeOptions()
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_argument("--disable-notifications")

            # Deneysel seçeneklerle bildirim ve parola yönetimini kapatıyoruz
            prefs = {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,
                "profile.default_content_setting_values.notifications": 2
            }
            options.add_experimental_option("prefs", prefs)

            # Undetected ChromeDriver başlatma
            driver = uc.Chrome(options=options)

            # WebDriver tespitini zorlaştırmak için
            driver.execute_script(
                "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
            )

            time.sleep(2)

        elif browser == "firefox":
            from selenium.webdriver.firefox.service import Service as FirefoxService
            from webdriver_manager.firefox import GeckoDriverManager
            options = webdriver.FirefoxOptions()
            if headless:
                options.add_argument("--headless")
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

        elif browser == "edge":
            from selenium.webdriver.edge.service import Service as EdgeService
            from webdriver_manager.microsoft import EdgeChromiumDriverManager
            options = webdriver.EdgeOptions()
            if headless:
                options.add_argument("--headless")
            options.add_argument("--start-maximized")
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)

        else:
            raise ValueError(f"Browser '{browser}' is not supported")

        # Implicit wait ayarı
        driver.implicitly_wait(Config.IMPLICIT_WAIT)

        return driver