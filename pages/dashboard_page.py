from pages.base_page import BasePage


class DashboardPage(BasePage):
    dashboard_logo= "//div[@class='oxd-brand-banner']"

    
    def is_dashboard_loaded(self):
        return self.is_element_visible(self.dashboard_logo)
    


