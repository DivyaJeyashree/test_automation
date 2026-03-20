import os
import allure
from core.driver import get_driver
from pages.mobile.app_page import AppPage


@allure.epic("APK Automation")
@allure.feature("Login Testing")


def test_login():
    driver = get_driver()
    page = AppPage(driver)

    password = os.getenv("APP_PASSWORD", "Test@123")

    page.login(password)

    assert page.is_screen_loaded()

    driver.quit()
