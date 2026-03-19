from locators.mobile.app_locators import AppLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AppPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click_first_button(self):
        element = self.wait.until(
            EC.element_to_be_clickable(AppLocators.FIRST_BUTTON)
        )
        element.click()

    def click_second_button(self):
        element = self.wait.until(
            EC.element_to_be_clickable(AppLocators.SECOND_BUTTON)
        )
        element.click()

    def is_screen_loaded(self):
        elements = self.driver.find_elements(*AppLocators.ANY_TEXT)
        return len(elements) > 0
