import allure
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from locators.header_locators import HeaderLocators
from locators.login_locators import LoginLocators
from faker import Faker

fake = Faker()

@allure.title("Успешная авторизация в Finverse Bank под тестовым пользователем")
@allure.feature("Авторизация")
@allure.story("Вход по валидным данным")
def test_successful_login(page: Page):
    login_page = LoginPage(page)
    
    login_page.open_login_page()
    login_page.login_with_env_credentials()
    
    with allure.step("Проверяем успешный переход на страницу Дашборда"):
        expected_dashboard_url = f"{login_page.base_url}/dashboard"
        expect(page).to_have_url(expected_dashboard_url)
        
    with allure.step("Проверяем отображение интерфейса Дашборда"):
        expect(page.get_by_test_id(HeaderLocators.LOGOUT_BUTTON)).to_be_visible()
        
        
@allure.title("Ошибка при авторизации с невалидными данными")
@allure.feature("Авторизация")
@allure.story("Попытка входа по случайным невалидным данным")
def test_invalid_login(page: Page):
    login_page = LoginPage(page)
    login_page.open_login_page()
    
    invalid_email = fake.email()
    invalid_password = fake.password(10)
    
    login_page.login_with_custom_credentials(email = invalid_email, password = invalid_password)
    
    with allure.step("Проверяем появление ошибки входа"):
        expect(page.get_by_test_id(LoginLocators.ERROR_MESSAGE)).to_be_visible()
            
            