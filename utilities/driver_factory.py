import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from config.config import Config
import undetected_chromedriver as uc


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

            # Undetected ChromeDriver başlatma
            driver = uc.Chrome(options=options)

            # WebDriver'in tespit edilmemesi için stealth benzeri özellikler ekleme
            driver.execute_script(
                "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
            )

            time.sleep(2)


        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            if headless:
                options.add_argument("--headless")
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

        elif browser == "edge":
            options = webdriver.EdgeOptions()
            if headless:
                options.add_argument("--headless")
            options.add_argument("--start-maximized")
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)

        else:
            raise ValueError(f"Browser '{browser}' is not supported")

        # Set implicit wait
        driver.implicitly_wait(Config.IMPLICIT_WAIT)

        return driver