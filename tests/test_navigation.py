import pytest
import allure
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from locators.login_locators import LoginLocators
from locators.dashboard_locators import DashboardLocators
from locators.history_locators import HistoryLocators
from locators.security_locators import SecurityLocators
from locators.transfer_locators import TransferLocators

@allure.title("Личный кабинет открывается и содержит плашку с личным счётом")
@allure.feature("Навигация по разделам Finverse Bank")
def test_go_to_dashboard_page(page: Page):
    login_page = LoginPage(page)
        
    login_page.open_login_page()
    login_page.login_with_env_credentials()
    
    with allure.step("Проверяем успешный переход в раздел Кабинет"):
        expected_dashboard_url = f"{login_page.base_url}/dashboard"
        expect(page).to_have_url(expected_dashboard_url)
        
    with allure.step("Проверяем наличие плашки с личным Счётом"):
        expect(page.get_by_test_id(DashboardLocators.ACCOUNT_CARD)).to_be_visible()
        

@allure.title("Успешный переход из личного кабинета в раздел Перевод")
@allure.feature("Навигация по разделам Finverse Bank")        
def test_go_to_transfer_page(page: Page):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    
    login_page.open_login_page()
    login_page.login_with_env_credentials()
    
    with allure.step("Нажимаем на кнопку Перевод в хедере приложения"):
        dashboard_page.click_nav_transfer()
        
    with allure.step("Проверяем успешный переход в раздел Перевод"):
        expected_transfer_url = f"{login_page.base_url}/transfer"
        expect(page).to_have_url(expected_transfer_url)
        
    with allure.step("Проверяем наличие формы для перевода"):
        expect(page.locator(TransferLocators.TRANSFER_FORM)).to_be_visible()
        
        
@allure.title("Успешный переход из личного кабинета в раздел История")
@allure.feature("Навигация по разделам Finverse Bank")        
def test_go_to_history_page(page: Page):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    
    login_page.open_login_page()
    login_page.login_with_env_credentials()
    
    with allure.step("Нажимаем на кнопку История в хедере приложения"):
        dashboard_page.click_nav_history()
        
    with allure.step("Проверяем успешный переход в раздел История"):
        expected_history_url = f"{login_page.base_url}/history"
        expect(page).to_have_url(expected_history_url)
        
    with allure.step("Проверяем наличие заголовка раздела История"):
        expect(page.locator(HistoryLocators.HISTORY_HEADING)).to_be_visible()
        
        
@allure.title("Успешный переход из личного кабинета в раздел Безопасность")
@allure.feature("Навигация по разделам Finverse Bank")        
def test_go_to_security_page(page: Page):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    
    login_page.open_login_page()
    login_page.login_with_env_credentials()
    
    with allure.step("Нажимаем на кнопку Безопасность в хедере приложения"):
        dashboard_page.click_nav_security()
        
    with allure.step("Проверяем успешный переход в раздел Безопасность"):
        expected_secur_url = f"{login_page.base_url}/security"
        expect(page).to_have_url(expected_secur_url)
        
    with allure.step("Проверяем наличие списка активных сессий"):
        expect(page.get_by_test_id(SecurityLocators.SESSIONS_LIST)).to_be_visible()            