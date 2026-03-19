from appium.webdriver.common.appiumby import AppiumBy

class AppLocators:
    # Generic clickable elements
    FIRST_BUTTON = (AppiumBy.XPATH, "(//android.widget.Button)[1]")
    SECOND_BUTTON = (AppiumBy.XPATH, "(//android.widget.Button)[2]")

    # Generic text / input
    TEXT_FIELD = (AppiumBy.CLASS_NAME, "android.widget.EditText")

    # Generic screen validation
    ANY_TEXT = (AppiumBy.CLASS_NAME, "android.widget.TextView")
