from selenium.webdriver.common.by import By

provider_city_radioButton = (By.XPATH, "//div[@id='provider_search_form']//span[contains(text(), 'Provider city')]")
city_field = (By.XPATH, '//input[@name="city"]')
search_button = (By.XPATH, '//div[@id="provider_search_form"]//button[@class = "button loading-button"]')
