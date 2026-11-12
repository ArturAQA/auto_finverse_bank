import os
import allure
from playwright.sync_api import Page
from pages.base_page import BasePage
from locators.register_locators import RegisterLocators

class RegisterPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.base_url = os.getenv("FINVERSE_BASE_URL", "https://finverse-bank.ru")
        self.url = f"{self.base_url}/register"
        
    def open_register_page(self):
        """Открывает страницу регистрации нового юзера"""
        with allure.step(f"Открываем страницу регистрации: {self.url}"):
            self.open(self.url)
        return self
    
    def register_new_user(self, fullname: str, email: str, password: str):
        """Регистрирует нового пользователя"""
        if not fullname or not email or not password:
            raise ValueError("Ошибка: Учетные данные не введены")
        
        with allure.step("Вводим данные нового юзера"):
            self.page.get_by_test_id(RegisterLocators.FULLNAME_INPUT).fill(fullname)
            self.page.get_by_test_id(RegisterLocators.EMAIL_INPUT).fill(email)
            self.page.get_by_test_id(RegisterLocators.PASSWORD_INPUT).fill(password)
            self.page.get_by_test_id(RegisterLocators.SUBMIT_BUTTON).click()
        return self