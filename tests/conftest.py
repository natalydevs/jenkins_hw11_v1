import pytest
from selene import browser
from selenium.webdriver import ChromeOptions

@pytest.fixture(scope='function', autouse=True)
def set_browser():
    options = ChromeOptions()
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920,1080')

    browser.config.driver_name = 'chrome'
    browser.config.driver_options = options
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 10
    yield
    browser.quit()
