from pages.base_page import BasePage


class Navigation(BasePage):
    user_menu="//span[@class='oxd-userdropdown-tab']"
    logout_button="//a[@href='/web/index.php/auth/logout']"
    def click_user_menu(self):
        self.click(self.user_menu)
        return self

    def click_logout_button(self):
        self.click(self.logout_button)
        return self

    def logout(self):
        self.click(self.user_menu)
        self.click(self.logout_button)
        return self