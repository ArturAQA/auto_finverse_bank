import pytest
import allure
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from locators.header_locators import HeaderLocators
from locators.login_locators import LoginLocators

@allure.title("Успешный выход из аккаунта Finverse Bank")
@allure.feature("Выход из аккаунта")
def test_logout(logged_in_page: Page):
    dashboard_page = DashboardPage(logged_in_page)
    
    with allure.step("Нажимаем на кнопку выхода из аккаунта"):
        dashboard_page.click_logout_button()
        
    with allure.step("Проверяем переход на страницу логина"):
        expect(logged_in_page).to_have_url(f"{dashboard_page.base_url}/login")
        
    with allure.step("Проверяем отображение кнопки Войти"):
        expect(logged_in_page.get_by_test_id(LoginLocators.SUBMIT_BUTTON)).to_be_visible()