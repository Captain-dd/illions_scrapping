from conftest import driver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.control import explicit_wait_time


class CommonUtilites:

    @staticmethod
    def click_element(element_locator):
        WebDriverWait(driver=driver, timeout=explicit_wait_time) \
            .until(EC.visibility_of_element_located(locator=element_locator)).click()

    @staticmethod
    def send_text(element_locator, text):
        WebDriverWait(driver=driver, timeout=explicit_wait_time) \
            .until(EC.visibility_of_element_located(locator=element_locator)).send_keys(text)

    @staticmethod
    def get_text(element_locator) -> str:
        WebDriverWait(driver=driver, timeout=explicit_wait_time) \
            .until(EC.visibility_of_element_located(locator=element_locator))

        return driver.find_element(by=element_locator[0], value=element_locator[1]).text

    @staticmethod
    def get_multiple_button(element_locator):
        WebDriverWait(driver=driver, timeout=explicit_wait_time).until(
            EC.visibility_of_element_located(locator=element_locator))

        return driver.find_elements(by=element_locator[0], value=element_locator[1])

    @staticmethod
    def scroll_down():
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @staticmethod
    def clear_input(element_locator):
        tag = WebDriverWait(driver=driver, timeout=explicit_wait_time).until(
            EC.visibility_of_element_located(locator=element_locator))
        tag.click()
        tag.clear()

    # @staticmethod
    # def is_displayed(element_locator):
    #     return driver.find_elements(by=element_locator[0], value=element_locator[1])
    #
