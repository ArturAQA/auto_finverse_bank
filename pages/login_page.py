import os
import allure
from playwright.sync_api import Page
from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from dotenv import load_dotenv, find_dotenv

# Подгружаем переменные из файла .env
load_dotenv(find_dotenv())

class LoginPage(BasePage):
    URL = "https://dev.finverse-bank.ru"

    def __init__(self, page: Page):
        super().__init__(page)

    def open_login_page(self):
        """Открывает страницу авторизации банка"""
        with allure.step(f"Открываем страницу логина: {self.URL}"):
            self.open(self.URL)
        return self

    def login_with_env_credentials(self):
        """Выполняет авторизацию, используя безопасные переменные окружения"""
        # Вытаскиваем секреты из системы
        email = os.getenv("FINVERSE_USER")
        password = os.getenv("FINVERSE_PASSWORD")
        
        if not email or not password:
            raise ValueError("Ошибка: Переменные окружения FINVERSE_USER или FINVERSE_PASSWORD не настроены!")

        with allure.step("Вводим безопасные учетные данные из env-переменных"):
            self.page.get_by_test_id(LoginLocators.EMAIL_INPUT).fill(email)
            self.page.get_by_test_id(LoginLocators.PASSWORD_INPUT).fill(password)
            self.page.get_by_test_id(LoginLocators.SUBMIT_BUTTON).click()