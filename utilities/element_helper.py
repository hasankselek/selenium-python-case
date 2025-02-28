from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from config.config import Config
from utilities.logger import Logger


class ElementHelper:
    """Helper class for element interactions"""

    def __init__(self, driver):
        """
        Initialize ElementHelper

        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        self.logger = Logger.get_logger(self.__class__.__name__)
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)

    def find(self, locator):
        """
        Find element using provided locator

        Args:
            locator (tuple): Locator tuple (By.*, "value")

        Returns:
            WebElement: Found element

        Raises:
            NoSuchElementException: If element not found
        """
        try:
            self.logger.info(f"Finding element with locator: {locator}")
            return self.driver.find_element(*locator)
        except NoSuchElementException as e:
            self.logger.error(f"Element not found with locator: {locator}")
            raise e

    def find_all(self, locator):
        """
        Find all elements using provided locator

        Args:
            locator (tuple): Locator tuple (By.*, "value")

        Returns:
            list: List of WebElements
        """
        self.logger.info(f"Finding all elements with locator: {locator}")
        return self.driver.find_elements(*locator)

    def click(self, locator):
        """
        Click on element

        Args:
            locator (tuple): Locator tuple (By.*, "value")
        """
        element = self.wait_for_element_clickable(locator)
        self.logger.info(f"Clicking on element with locator: {locator}")
        element.click()

    def input_text(self, locator, text):
        """
        Input text into element

        Args:
            locator (tuple): Locator tuple (By.*, "value")
            text (str): Text to input
        """
        element = self.wait_for_element_visible(locator)
        element.clear()
        self.logger.info(f"Entering text '{text}' into element with locator: {locator}")
        element.send_keys(text)

    def get_text(self, locator):
        """
        Get text from element

        Args:
            locator (tuple): Locator tuple (By.*, "value")

        Returns:
            str: Element text
        """
        element = self.wait_for_element_visible(locator)
        text = element.text
        self.logger.info(f"Got text '{text}' from element with locator: {locator}")
        return text

    def wait_for_element_visible(self, locator):
        """
        Wait for element to be visible

        Args:
            locator (tuple): Locator tuple (By.*, "value")

        Returns:
            WebElement: Visible element

        Raises:
            TimeoutException: If element not visible within timeout
        """
        try:
            self.logger.info(f"Waiting for element to be visible with locator: {locator}")
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException as e:
            self.logger.error(f"Element not visible within timeout with locator: {locator}")
            raise e

    def wait_for_element_clickable(self, locator):
        """
        Wait for element to be clickable

        Args:
            locator (tuple): Locator tuple (By.*, "value")

        Returns:
            WebElement: Clickable element

        Raises:
            TimeoutException: If element not clickable within timeout
        """
        try:
            self.logger.info(f"Waiting for element to be clickable with locator: {locator}")
            return self.wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException as e:
            self.logger.error(f"Element not clickable within timeout with locator: {locator}")
            raise e

    def is_element_present(self, locator):
        """
        Check if element is present

        Args:
            locator (tuple): Locator tuple (By.*, "value")

        Returns:
            bool: True if element is present, False otherwise
        """
        try:
            self.find(locator)
            self.logger.info(f"Element is present with locator: {locator}")
            return True
        except NoSuchElementException:
            self.logger.info(f"Element is not present with locator: {locator}")
            return False



