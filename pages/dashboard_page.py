import os
import allure
from playwright.sync_api import Page
from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from locators.header_locators import HeaderLocators
from locators.dashboard_locators import DashboardLocators
from locators.dashboard_locators import CardRevealLocators

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
        self.page.locator(DashboardLocators.OPEN_ACCOUNT_BUTTON).click()
        return self
    
    def click_issue_card_button(self):
        """Кликнуть по кнопке Выпустить карту"""
        self.page.get_by_test_id(DashboardLocators.ISSUE_CARD_BUTTON).click()
        return self
    
    def confirm_issue_card(self):
        """Кликнуть на вторую кнопку 'Выпустить карту' для подтверждения"""
        self.page.locator(DashboardLocators.CONFIRM_ISSUE_CARD_BUTTON).click()
        return self
    
    def save_card(self):
        """Сохранить выпущенную карту"""
        self.page.locator(DashboardLocators.SAVE_CARD_BUTTON).click()
        return self
    
    def block_card(self):
        """Заблокировать карту"""
        self.page.locator(DashboardLocators.CARD_BLOCK_BUTTON).first.click()
        return self
    
    def unblock_card(self):
        """Разблокировать карту"""
        self.page.locator(DashboardLocators.CARD_UNBLOCK_BUTTON).first.click()
        return self
    
    def click_card(self):
        """Кликнуть по карте"""
        self.page.get_by_test_id(DashboardLocators.BANK_CARD).first.click()
        return self
    
    def click_modal_close_button(self):
        """Кликнуть на крестик в модальном окне карты"""
        self.page.get_by_test_id(CardRevealLocators.MODAL_CLOSE).click()
        return self
    
    def click_outside_modal(self):
        """Кликнуть мимо модального окна"""
        self.page.mouse.click(10, 10)
        return self
    
    def click_card_reveal_button(self):
        """Кликнуть на кнопку Показать данные"""
        self.page.get_by_test_id(CardRevealLocators.REVEAL_BUTTON).click()
        return self
    
    def click_card_hide_button(self):
        """Кликнуть на кнопку Скрыть номер"""
        self.page.get_by_test_id(CardRevealLocators.HIDE_BUTTON).click()
        return self
    
    def click_copy_number_button(self):
        """Кликнуть на кнопку Копировать номер"""
        self.page.get_by_test_id(CardRevealLocators.COPY_NUMBER_BUTTON).click()
        return self
