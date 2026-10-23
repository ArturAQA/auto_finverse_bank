import os
import allure
from playwright.sync_api import Page
from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from dotenv import load_dotenv, find_dotenv

# Подгружаем переменные из файла .env
load_dotenv(find_dotenv())

class LoginPage(BasePage):
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.base_url = os.getenv("FINVERSE_BASE_URL", "https://finverse-bank.ru")
        self.url = f"{self.base_url}/login"

    def open_login_page(self):
        """Открывает страницу авторизации банка"""
        with allure.step(f"Открываем страницу логина: {self.url}"):
            self.open(self.url)
        return self

    def login_with_env_credentials(self):
        """Выполняет авторизацию, используя безопасные переменные окружения"""
        user_email = os.getenv("FINVERSE_USER")
        user_password = os.getenv("FINVERSE_PASSWORD")
        
        if not user_email or not user_password:
            raise ValueError("Ошибка: Учетные данные не предоставлены и не найдены в env!")

        with allure.step("Вводим безопасные учетные данные из env-переменных"):
            self.page.get_by_test_id(LoginLocators.EMAIL_INPUT).fill(user_email)
            self.page.get_by_test_id(LoginLocators.PASSWORD_INPUT).fill(user_password)
            self.page.get_by_test_id(LoginLocators.SUBMIT_BUTTON).click()
            
    def login_with_custom_credentials(self, email: str, password: str):
        """Выполняет авторизацию, используя введенные данные"""
        if not email or not password:
                    raise ValueError("Ошибка: Учетные данные не введены")
                
        with allure.step("Вводим учетные данные"):
                    self.page.get_by_test_id(LoginLocators.EMAIL_INPUT).fill(email)
                    self.page.get_by_test_id(LoginLocators.PASSWORD_INPUT).fill(password)
                    self.page.get_by_test_id(LoginLocators.SUBMIT_BUTTON).click()
        return self            