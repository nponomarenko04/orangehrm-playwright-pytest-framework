import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_successful_login(page):
    """Тест успешного логина"""
    login_page = LoginPage(page)
    login_page.open_login_page().login()
    
    dashboard_page = DashboardPage(page)
    assert dashboard_page.is_dashboard_loaded()
    assert "dashboard" in page.url.lower()

def test_login_with_wrong_credentials(page):
    """Тест с неверными данными"""
    login_page = LoginPage(page)
    login_page.open_login_page().login("wrong", "wrong")
    
    error_text = login_page.get_error_text()
    assert error_text != ""
    assert "invalid" in error_text.lower() or "error" in error_text.lower()

def test_empty_login(page):
    """Тест с пустыми полями"""
    login_page = LoginPage(page)
    login_page.open_login_page().login("", "")
    
    # В OrangeHRM при пустых полях появляются красные рамки
    assert login_page.is_element_visible(".oxd-input-field-error-message")
