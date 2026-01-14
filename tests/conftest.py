import pytest
from playwright.sync_api import Playwright, Page
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()
    yield page
    context.close()
    browser.close()


@pytest.fixture(scope='session')
def initialize_auth_state(playwright: Playwright) -> str:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    page.locator("input[name='username']").fill("Admin")
    page.locator("input[name='password']").fill("admin123")
    page.locator("button[type='submit']").click()
    page.wait_for_selector("//div[@class='oxd-brand-banner']", timeout=10000)

    storage_path = "orangehrm-state.json"
    context.storage_state(path=storage_path)

    page.close()
    context.close()
    browser.close()

    return storage_path


@pytest.fixture
def auth_page(initialize_auth_state: str, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        storage_state=initialize_auth_state
    )
    page = context.new_page()
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index')
    yield page
    page.close()
    context.close()
    browser.close()


@pytest.fixture
def login_page(chromium_page: Page) -> LoginPage:
    return LoginPage(page=chromium_page)


@pytest.fixture
def auth_dashboard_page(auth_page: Page) -> DashboardPage:
    return DashboardPage(page=auth_page)


def pytest_collection_modifyitems(config, items):
    for item in items:
        if not any(item.iter_markers()):
            item.add_marker(pytest.mark.smoke)