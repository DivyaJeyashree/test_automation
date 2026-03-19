from appium import webdriver
from appium.options.android import UiAutomator2Options

def get_driver():
    options = UiAutomator2Options()

    options.platform_name = "Android"
    options.device_name = "emulator-5554"

    # 🔥 IMPORTANT: USE APK DIRECTLY
    options.app = "app.apk"

    options.automation_name = "UiAutomator2"
    options.no_reset = True
    options.auto_grant_permissions = True

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    return driver
