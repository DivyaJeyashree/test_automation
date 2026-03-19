import os
from appium import webdriver
from appium.options.android import UiAutomator2Options

def get_driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "emulator-5554"
    options.app = os.path.abspath("app.apk")
    options.automation_name = "UiAutomator2"
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    return driver
