import pytest
from playwright.sync_api import BrowserContext

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, request):
    """Переопределяем параметры браузера"""
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
        "ignore_https_errors": True,
    }

# Добавляем фикстуру для запуска с видимым браузером
@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args, request):
    """Параметры запуска браузера"""
    return {
        **browser_type_launch_args,
        "headless": False,   # ВИДИМЫЙ браузер
        "slow_mo": 1000,     # Замедление 1 сек
    }

@pytest.fixture
def page(context: BrowserContext):
    """Простая фикстура страницы"""
    page = context.new_page()
    yield page
    page.close()
