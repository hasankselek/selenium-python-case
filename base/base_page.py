from selenium.webdriver.common.by import By
from utilities.element_helper import ElementHelper
from utilities.logger import Logger
from config.config import Config


class BasePage:
    """Base class for all page objects"""

    def __init__(self, driver):
        """
        Initialize BasePage

        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        self.element_helper = ElementHelper(driver)
        self.logger = Logger.get_logger(self.__class__.__name__)
        self.base_url = Config.BASE_URL

    def navigate_to(self, url=""):
        """
        Navigate to URL

        Args:
            url (str): URL suffix to append to base URL
        """
        full_url = f"{self.base_url}{url}"
        self.logger.info(f"Navigating to URL: {full_url}")
        self.driver.get(full_url)

    def get_title(self):
        """
        Get page title

        Returns:
            str: Page title
        """
        title = self.driver.title
        self.logger.info(f"Page title: {title}")
        return title

    def get_current_url(self):
        """
        Get current URL

        Returns:
            str: Current URL
        """
        url = self.driver.current_url
        self.logger.info(f"Current URL: {url}")
        return url

    def refresh_page(self):
        """Refresh the current page"""
        self.logger.info("Refreshing page")
        self.driver.refresh()

    def go_back(self):
        """Navigate back in browser history"""
        self.logger.info("Navigating back")
        self.driver.back()

    def go_forward(self):
        """Navigate forward in browser history"""
        self.logger.info("Navigating forward")
        self.driver.forward()
