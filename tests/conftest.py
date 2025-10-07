import os
import pytest
from selene import browser
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture(scope='function', autouse=True)
def set_browser():
    options = ChromeOptions()
    # устойчивый набор флагов для контейнеров/Alpine
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-software-rasterizer')
    options.add_argument('--disable-extensions')
    options.add_argument('--no-zygote')
    options.add_argument('--window-size=1920,1080')
    # на всякий пожарный для новых версий хрома/драйвера
    options.add_argument('--remote-allow-origins=*')

    # Явно укажем бинарь chromium, который мы ставим в Execute shell
    chrome_bin = os.getenv('CHROME_BIN')
    if chrome_bin:
        options.binary_location = chrome_bin

    # Явно укажем путь до chromedriver и включим лог
    driver_path = os.getenv('CHROMEDRIVER')
    service = ChromeService(executable_path=driver_path, log_output="chromedriver.log") if driver_path else None

    browser.config.driver_name = 'chrome'
    browser.config.driver_options = options
    if service:
        browser.config.driver_service = service

    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 10

    yield

    browser.quit()
