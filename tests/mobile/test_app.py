import allure
from core.driver import get_driver
from pages.mobile.app_page import AppPage


@allure.epic("APK Automation")
@allure.feature("Basic Testing")


# ✅ Test 1
def test_click_first_button():
    driver = get_driver()
    page = AppPage(driver)

    page.click_first_button()

    assert page.is_screen_loaded()

    driver.quit()


# ✅ Test 2
def test_click_second_button_with_text():
    driver = get_driver()
    page = AppPage(driver)

    page.enter_text("Hello Automation")
    page.click_second_button()

    assert page.is_screen_loaded()

    driver.quit()
