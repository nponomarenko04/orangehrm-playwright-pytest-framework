import time

import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage

@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.authorization
def test_successful_login(page:Page):
    login_page=LoginPage(page=page)
    login_page.open_login_page()
    login_page.fill_login_form(username="Admin",password="admin123")
    login_page.click_login_button()
    time.sleep(300)