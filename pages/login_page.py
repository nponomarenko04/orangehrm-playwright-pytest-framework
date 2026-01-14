from pages.base_page import BasePage
from playwright.sync_api import Page

class LoginPage(BasePage):
    password_input="input[name='password']"
    username_input = "input[name='username']"
    login_button = "//button[@type='submit']"

    def __init__(self,page: Page):
        super().__init__(page)
        self.url = "https://opensource-demo.orangehrmlive.com"

    def open_login_page(self):
        self.navigate("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        return self

    def fill_login_form(self, username: str = "", password: str = ""):
            self.fill(self.username_input, username)
            self.fill(self.password_input, password)


    def click_login_button(self):
        self.click(self.login_button)
        return self
    

