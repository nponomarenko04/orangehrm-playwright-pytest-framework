from playwright.sync_api import Page, expect
import time

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.timeout = 10000
    
    def navigate(self, url: str):
        self.page.goto(url, wait_until="networkidle")
        return self
    
    def click(self, selector: str):
        self.page.locator(selector).click()
        return self
    
    def fill(self, selector: str, text: str):
        self.page.locator(selector).fill(text)
        return self
    
    def get_text(self, selector: str) -> str:
        return self.page.locator(selector).text_content() or ""
    
    def wait_for_element(self, selector: str, timeout: int = None):
        timeout = timeout or self.timeout
        self.page.locator(selector).wait_for(state="visible", timeout=timeout)
        return self
    
    def is_element_visible(self, selector: str) -> bool:
        return self.page.locator(selector).is_visible()
