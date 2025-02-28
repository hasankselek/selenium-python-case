import pytest
import os
from utilities.driver_factory import DriverFactory
from utilities.logger import Logger

# Setup logger
logger = Logger.get_logger("conftest")


@pytest.fixture(scope="function")
def setup_driver():
    """
    Setup WebDriver before test and tear down after test

    Yields:
        WebDriver: WebDriver instance
    """
    logger.info("Setting up WebDriver")
    driver = DriverFactory.get_driver()

    # Yield driver to test
    yield driver

    # Teardown
    logger.info("Tearing down WebDriver")
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Capture screenshots on test failure
    """
    outcome = yield
    report = outcome.get_result()

    # Check if test failed and in call phase
    if report.when == "call" and report.failed:
        # Check if fixture has driver
        driver = None
        for fixture_name, fixture_value in item._fixtureinfo.name2fixturedefs.items():
            if fixture_name == "setup_driver":
                driver = item.funcargs["setup_driver"]
                break

        if driver:
            # Create screenshots directory if it doesn't exist
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")

            # Take screenshot
            test_name = item.nodeid.replace("/", "_").replace(":", "_").replace("::", "_")
            screenshot_path = f"screenshots/{test_name}.png"
            driver.save_screenshot(screenshot_path)
            logger.info(f"Screenshot saved to {screenshot_path}")
