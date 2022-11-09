from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import pytest

option = Options()
option.headless =False
driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)

@pytest.fixture()
def initiate_driver():

    driver.get('https://enrollhfs.illinois.gov/en/provider-search')
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver

    driver.quit()


