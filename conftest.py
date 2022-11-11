from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import pytest

option = Options()

# if True then browser UI will not be visible
# if False then browser UI will be visible
option.headless = False
driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)

@pytest.fixture()
def initiate_driver():

    driver.get('https://enrollhfs.illinois.gov/en/provider-search')
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver

    driver.quit()


