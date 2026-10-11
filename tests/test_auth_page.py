import allure
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

@allure.title("Успешная авторизация в Finverse Bank под тестовым пользователем")
@allure.feature("Авторизация")
@allure.story("Вход по валидным данным")
def test_successful_login(page: Page):
    login_page = LoginPage(page)
    
    login_page.open_login_page()
    login_page.login_with_env_credentials()
    
    with allure.step("Проверяем успешный переход на страницу Дашборда"):
        expect(page).to_have_url("https://finverse-bank.ru")