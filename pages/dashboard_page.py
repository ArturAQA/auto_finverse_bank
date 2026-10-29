import os
import allure
from playwright.sync_api import Page
from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from locators.header_locators import HeaderLocators

class DashboardPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.base_url = os.getenv("FINVERSE_BASE_URL", "https://finverse-bank.ru")
        self.url = f"{self.base_url}/dashboard"
        
    def click_nav_transfer(self):
        """Кликнуть по кнопке перехода в раздел Перевод"""
        self.page.get_by_test_id(HeaderLocators.NAV_TRANSFER).click()
        return self
    
    def click_nav_history(self):
            """Кликнуть по кнопке перехода в раздел История"""
            self.page.get_by_test_id(HeaderLocators.NAV_HISTORY).click()
            return self
        
    def click_nav_security(self):
                """Кликнуть по кнопке перехода в раздел Безопасность"""
                self.page.get_by_test_id(HeaderLocators.NAV_SECURITY).click()
                return self    