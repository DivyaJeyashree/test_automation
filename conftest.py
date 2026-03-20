import pytest
from playwright.sync_api import sync_playwright
from core.driver import get_driver


# ✅ Mobile Fixture
@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


# ✅ Web Fixture
@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-dev-shm-usage"
            ]
        )
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080}
        )
        page = context.new_page()
        page.goto("https://example.com")

        yield page

        context.close()
        browser.close()
