import os
from appium import webdriver
from appium.options.android import UiAutomator2Options

def get_driver():
    options = UiAutomator2Options()

    # ✅ Path to Downloads folder APK
    apk_path = os.path.expanduser("~/Downloads/app-release-4-3-26.apk")
    options.app = apk_path

    options.set_capability("platformName", "Android")
    options.set_capability("automationName", "UiAutomator2")
    options.set_capability("deviceName", "emulator-5554")
    options.set_capability("autoGrantPermissions", True)

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    return driver
