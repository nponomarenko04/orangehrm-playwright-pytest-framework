from pages.base_page import BasePage


class DashboardPage(BasePage):
    dashboard_logo= "//div[@class='oxd-brand-banner']"

    
    def is_dashboard_loaded(self):
        self.is_element_visible(self.dashboard_logo)
    
    def logout(self):
        self.click(self.USER_MENU)
        self.click(self.LOGOUT_BUTTON)

