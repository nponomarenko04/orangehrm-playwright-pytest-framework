import time

import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage

@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.authorization
def test_invalid_login(page:Page):
    login_page=LoginPage(page=page)
    login_page.open_login_page()
    login_page.fill_login_form(username="None",password="None")
    login_page.click_login_button()
    login_page.expect_alert()

