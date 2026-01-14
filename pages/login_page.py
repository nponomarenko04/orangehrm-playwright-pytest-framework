from pages.base_page import BasePage

class LoginPage(BasePage):
    # Локаторы для OrangeHRM
    USERNAME_INPUT = "input[name='username']"
    PASSWORD_INPUT = "input[name='password']"
    LOGIN_BUTTON = "button[type='submit']"
    ERROR_MESSAGE = ".oxd-alert-content-text"
    FORGOT_PASSWORD_LINK = ".oxd-text.oxd-text--p.orangehrm-login-forgot-header"
    
    def open_login_page(self):
        self.navigate("https://opensource-demo.orangehrmlive.com")
        return self
    
    def login(self, username: str = "Admin", password: str = "admin123"):
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        return self
    
    def get_error_text(self):
        if self.is_element_visible(self.ERROR_MESSAGE):
            return self.get_text(self.ERROR_MESSAGE)
        return ""
