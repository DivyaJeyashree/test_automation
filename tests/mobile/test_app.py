import os
import allure
from core.driver import get_driver
from pages.mobile.app_page import AppPage


@allure.epic("APK Automation")
@allure.feature("Login Testing")


def test_login():
    driver = get_driver()
    page = AppPage(driver)

    password = os.getenv("APP_PASSWORD", "Test@123")  # fallback for local

    page.enter_text(password)
    page.click_first_button()

    assert page.is_screen_loaded()

    driver.quit()
