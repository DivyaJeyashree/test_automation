import os
from appium import webdriver
from appium.options.android import UiAutomator2Options

def get_driver():
    options = UiAutomator2Options()

    # ✅ Try local Downloads first
    local_apk = os.path.expanduser("~/Downloads/app-release-4-3-26.apk")
    repo_apk = os.path.abspath("app.apk")

    if os.path.exists(local_apk):
        options.app = local_apk
    else:
        options.app = repo_apk   # for GitHub Actions

    options.set_capability("platformName", "Android")
    options.set_capability("automationName", "UiAutomator2")
    options.set_capability("deviceName", "emulator-5554")
    options.set_capability("autoGrantPermissions", True)
    options.set_capability("noReset", False)

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    return driver
