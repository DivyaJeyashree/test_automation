import os
from appium import webdriver
from appium.options.android import UiAutomator2Options

def get_driver():
    options = UiAutomator2Options()
    
    options.app = os.path.abspath("app.apk")
    options.set_capability("platformName", "Android")
    options.set_capability("automationName", "UiAutomator2")
    options.set_capability("deviceName", "emulator-5554")
    options.set_capability("appPackage", "com.whatsapp")
    options.set_capability("appActivity", "com.whatsapp.Main")
    options.set_capability("noReset", True)
    options.set_capability("autoGrantPermissions", True)
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    return driver

