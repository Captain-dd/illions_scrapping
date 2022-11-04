from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

import pytest

driver = webdriver.Chrome(ChromeDriverManager().install())

@pytest.fixture()
def initiate_driver():
    driver.get('https://enrollhfs.illinois.gov/en/provider-search')
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver

    driver.quit()


