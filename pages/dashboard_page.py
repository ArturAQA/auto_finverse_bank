import os
import allure
from playwright.sync_api import Page
from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from locators.header_locators import HeaderLocators
from locators.dashboard_locators import DashboardLocators

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
            
    def click_logout_button(self):
        """Кликнуть по кнопке выхода из аккаунта"""
        self.page.get_by_test_id(HeaderLocators.LOGOUT_BUTTON).click()
        return self
    
    def open_account(self):
        """Кликнуть по кнопке открытия нового счета"""
        self.page.get_by_role("button", name="Открыть счёт").click()
        return self
    
    def click_issue_card_button(self):
        """Кликнуть по кнопке Выпустить карту"""
        self.page.get_by_test_id(DashboardLocators.ISSUE_CARD_BUTTON).click()
        return self
    
    def confirm_issue_card(self):
        """Кликнуть на вторую кнопку 'Выпустить карту' для подтверждения"""
        self.page.get_by_role("button", name="Выпустить карту").last.click()
        return self
    
    def save_card(self):
        """Сохранить выпущенную карту"""
        self.page.get_by_role("button", name="Сохранено").click()
        return self