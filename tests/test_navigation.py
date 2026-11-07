import pytest
import allure
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from locators.login_locators import LoginLocators
from locators.header_locators import HeaderLocators
from locators.dashboard_locators import DashboardLocators
from locators.history_locators import HistoryLocators
from locators.security_locators import SecurityLocators
from locators.transfer_locators import TransferLocators

@allure.title("Личный кабинет открывается и содержит плашку с личным счётом")
@allure.feature("Навигация по разделам Finverse Bank")
def test_go_to_dashboard_page(logged_in_page: Page):
    dashboard_page = DashboardPage(logged_in_page)
    
    with allure.step("Проверяем успешный переход в раздел Кабинет"):
        expected_dashboard_url = f"{dashboard_page.base_url}/dashboard"
        expect(logged_in_page).to_have_url(expected_dashboard_url)
        
    with allure.step("Проверяем наличие плашки с личным Счётом"):
        expect(logged_in_page.get_by_test_id(DashboardLocators.ACCOUNT_CARD)).to_be_visible()

@allure.title("Успешный переход из личного кабинета в раздел Перевод")
@allure.feature("Навигация по разделам Finverse Bank")
def test_go_to_transfer_page(logged_in_page: Page):
    dashboard_page = DashboardPage(logged_in_page)
    
    with allure.step("Нажимаем на кнопку Перевод в хедере приложения"):
        dashboard_page.click_nav_transfer()
        
    with allure.step("Проверяем успешный переход в раздел Перевод"):
        expect(logged_in_page).to_have_url(f"{dashboard_page.base_url}/transfer")
        
    with allure.step("Проверяем наличие формы для перевода"):
        expect(logged_in_page.locator(TransferLocators.TRANSFER_FORM)).to_be_visible()

@allure.title("Успешный переход из личного кабинета в раздел История")
@allure.feature("Навигация по разделам Finverse Bank")
def test_go_to_history_page(logged_in_page: Page):
    dashboard_page = DashboardPage(logged_in_page)
    
    with allure.step("Нажимаем на кнопку История в хедере приложения"):
        dashboard_page.click_nav_history()
        
    with allure.step("Проверяем успешный переход в раздел История"):
        expect(logged_in_page).to_have_url(f"{dashboard_page.base_url}/history")
        
    with allure.step("Проверяем наличие заголовка раздела История"):
        expect(logged_in_page.get_by_role("heading", name="История")).to_be_visible()

@allure.title("Успешный переход из личного кабинета в раздел Безопасность")
@allure.feature("Навигация по разделам Finverse Bank")
def test_go_to_security_page(logged_in_page: Page):
    dashboard_page = DashboardPage(logged_in_page)
    
    with allure.step("Нажимаем на кнопку Безопасность в хедере приложения"):
        dashboard_page.click_nav_security()
        
    with allure.step("Проверяем успешный переход в раздел Безопасность"):
        expect(logged_in_page).to_have_url(f"{dashboard_page.base_url}/security")
        
    with allure.step("Проверяем наличие списка активных сессий"):
        expect(logged_in_page.get_by_test_id(SecurityLocators.SESSIONS_LIST)).to_be_visible()
        
@pytest.mark.parametrize("path, expected_title", [
    ("dashboard", "Дашборд | Finverse Bank"),
    ("transfer", "Переводы | Finverse Bank"),
    ("history", "История операций | Finverse Bank"),
    ("security", "Безопасность | Finverse Bank"),
], ids=["дашборд", "переводы", "история", "безопасность"])
@allure.title("Страница {path} открывается с правильным заголовком вкладки")
@allure.feature("Навигация")
def test_bank_pages_titles(logged_in_page: Page, path, expected_title):
    dashboard_page = DashboardPage(logged_in_page)
    
    with allure.step(f"Переходим на страницу: {path}"):
        target_url = f"{dashboard_page.base_url}/{path}"
        logged_in_page.goto(target_url)
        
    with allure.step(f"Проверяем заголовок вкладки: {expected_title}"):
        expect(logged_in_page).to_have_title(expected_title)
        
@pytest.mark.parametrize("path", [
    "dashboard",
    "transfer",
    "history",
    "security"
], ids=["на дашборде", "в переводах", "в истории", "в безопасности"])
@allure.title("Кнопка выхода в шапке отображается на странице {path}")
@allure.feature("Навигация")
def test_header_logout_button_visible(logged_in_page: Page, path):
    dashboard_page = DashboardPage(logged_in_page)
    
    with allure.step(f"Переходим на страницу: {path}"):
        target_url = f"{dashboard_page.base_url}/{path}"
        logged_in_page.goto(target_url)
        
    with allure.step("Проверяем наличие кнопки выхода в хедере"):
        expect(logged_in_page.get_by_test_id(HeaderLocators.LOGOUT_BUTTON)).to_be_visible()