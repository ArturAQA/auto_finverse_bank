import pytest
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
        
        
@pytest.mark.parametrize("attempt", range(3),
                         ids=["попытка_1", "попытка_2", "попытка_3"])
@allure.title("Логин с рандомными данными Faker: {attempt}")
@allure.feature("Авторизация")
def test_login_with_faker(page: Page, attempt):
    login_page = LoginPage(page)
    login_page.open_login_page()
    
    invalid_email = fake.email()
    invalid_password = fake.password(10)
        
    with allure.step(f"Вводим сгенерированные данные для попытки №{attempt + 1}"):
        login_page.login_with_custom_credentials(email=invalid_email, password=invalid_password)
        allure.attach(invalid_email, name="Email", attachment_type=allure.attachment_type.TEXT)
        
    with allure.step("Проверяем появление ошибки входа"):
            expect(page.get_by_test_id(LoginLocators.ERROR_MESSAGE)).to_be_visible()