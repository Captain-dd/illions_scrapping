from selenium.webdriver.common.by import By

doctor_name = (By.XPATH, '//div[@id="provider_search_item"]//sub')
doctor_address = (By.XPATH, '//div[@id="provider_search_item"]//table/tbody/tr/td')
search_number = (By.CSS_SELECTOR, '.dynamic-text b')
