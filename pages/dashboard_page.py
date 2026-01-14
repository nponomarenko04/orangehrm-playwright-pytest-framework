from pages.base_page import BasePage

class DashboardPage(BasePage):
    # Локаторы dashboard
    DASHBOARD_HEADER = ".oxd-topbar-header-breadcrumb-module"
    USER_MENU = ".oxd-userdropdown-tab"
    LOGOUT_BUTTON = "a[href='/web/index.php/auth/logout']"
    
    def is_dashboard_loaded(self):
        return self.is_element_visible(self.DASHBOARD_HEADER)
    
    def logout(self):
        self.click(self.USER_MENU)
        self.click(self.LOGOUT_BUTTON)
        return LoginPage(self.page)
