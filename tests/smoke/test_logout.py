import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.components.navigation_component import Navigation

def test_logout(auth_dashboard_page:DashboardPage,login_page:LoginPage):
    auth_dashboard_page.is_dashboard_loaded()
    nav_logout=Navigation(page=auth_dashboard_page.page)
    nav_logout.click_user_menu()
    nav_logout.click_logout_button()
    login_page.expect_logo()
