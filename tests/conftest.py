import os
import pytest
from selene import browser
from selenium.webdriver import ChromeOptions, ChromeService

@pytest.fixture(scope='function', autouse=True)
def set_browser():
    options = ChromeOptions()
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920,1080')

    chrome_bin = os.getenv('CHROME_BIN')
    if chrome_bin:
        options.binary_location = chrome_bin

    driver_path = os.path.join(os.getenv('WORKSPACE', os.getcwd()), 'chromedriver-linux64', 'chromedriver')

    service = ChromeService(executable_path=driver_path)

    browser.config.driver_name = 'chrome'
    browser.config.driver_options = options
    browser.config.driver_service = service

    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 10
    yield
    browser.quit()
