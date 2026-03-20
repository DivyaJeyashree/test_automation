from appium import webdriver
from appium.options.android import UiAutomator2Options

def get_driver():
    options = UiAutomator2Options()

    options.platform_name = "Android"
    options.device_name = "emulator-5554"

    # 🔥 IMPORTANT
    options.app = "/home/runner/work/test_automation/test_automation/app.apk"

    # 🔥 Your app details
    options.app_package = "com.almuzaini.almuzaini"
    options.app_activity = "com.almuzaini.almuzaini.MainActivity"

    options.automation_name = "UiAutomator2"

    # ✅ FIXES
    options.no_reset = True
    options.new_command_timeout = 300
    options.adb_exec_timeout = 120000   # 🔥 VERY IMPORTANT (increase timeout)
    options.app_wait_duration = 120000  # 🔥 wait for app launch

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    return driver
