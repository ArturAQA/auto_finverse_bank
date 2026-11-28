import re
import allure
from playwright.sync_api import Page, expect
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from locators.dashboard_locators import DashboardLocators, CardRevealLocators
from utils.data_generators import generate_user_fullname

@allure.title("При нажатии на карту открывается модальное окно карты")
@allure.feature("Действия с модальным окном карты")
def test_open_card_modal(logged_in_page: Page):
    dashboard_page = DashboardPage(logged_in_page)
    
    with allure.step("Кликаем по карте"):
        dashboard_page.click_card()
        
    with allure.step("Проверяем, что открылось модальное окно карты"):
        expect(logged_in_page.get_by_test_id(CardRevealLocators.MODAL)).to_be_visible()
        
@allure.title("Модальное окно закрывается кликом на крестик")
@allure.feature("Действия с модальным окном карты")
def test_close_card_modal_by_button(logged_in_page: Page):
    dashboard_page = DashboardPage(logged_in_page)
    
    with allure.step("Кликаем по карте"):
        dashboard_page.click_card()
        
    with allure.step("Кликаем на крестик"):
        dashboard_page.click_modal_close_button()
        
    with allure.step("Проверяем, что окно не отображается"):
        expect(logged_in_page.get_by_test_id(CardRevealLocators.MODAL)).not_to_be_visible()
        
@allure.title("Модальное окно закрывается клавишей Ecsape")
@allure.feature("Действия с модальным окном карты")
def test_close_card_modal_by_esc(logged_in_page: Page):
    dashboard_page = DashboardPage(logged_in_page)
    
    with allure.step("Кликаем по карте"):
        dashboard_page.click_card()
        
    with allure.step("Нажимаем на клавишу Esc"):
        logged_in_page.keyboard.press("Escape")
        
    with allure.step("Проверяем, что окно не отображается"):
        expect(logged_in_page.get_by_test_id(CardRevealLocators.MODAL)).not_to_be_visible()
        
@allure.title("Модальное окно закрывается кликом в молоко")
@allure.feature("Действия с модальным окном карты")
def test_close_card_modal_by_click_outside(logged_in_page: Page):
    dashboard_page = DashboardPage(logged_in_page)
    
    with allure.step("Кликаем по карте"):
        dashboard_page.click_card()
        
    with allure.step("Кликаем мимо окна"):
        dashboard_page.click_outside_modal()
        
    with allure.step("Проверяем, что окно не отображается"):
        expect(logged_in_page.get_by_test_id(CardRevealLocators.MODAL)).not_to_be_visible()
        
@allure.title("Успешное раскрытие данных карты")
@allure.feature("Действия с модальным окном карты")
def test_reveal_card_data(page: Page):
    login_page = LoginPage(page)
    register_page = RegisterPage(page)
    dashboard_page = DashboardPage(page)

    with allure.step("Создаем нового пользователя и выпускаем свежую карту"):
        user = generate_user_fullname()
        register_page.open_register_page().register_new_user(
            fullname=user["fullname"],
            email=user["email"],
            password=user["password"]
        )
        login_page.login_with_custom_credentials(
            email=user["email"],
            password=user["password"]
        )
        dashboard_page.open_account().click_issue_card_button().confirm_issue_card().save_card()

    with allure.step("Кликаем по выпущенной карте"):
        dashboard_page.click_card()

    with allure.step("Кликаем на кнопку Показать данные"):
        dashboard_page.click_card_reveal_button()

    with allure.step("Проверяем, что отобразился CVV номер"):
        expect(page.get_by_test_id(CardRevealLocators.CVV_VALUE)).to_be_visible()

    with allure.step("Проверяем, что номер карты отображается в виде 16 цифр"):
        expect(page.get_by_test_id(CardRevealLocators.NUMBER_VALUE)).to_have_text(
            re.compile(r"\d{4}\s\d{4}\s\d{4}\s\d{4}")
        )
