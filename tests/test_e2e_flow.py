import allure
from playwright.sync_api import Page, expect
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from locators.dashboard_locators import DashboardLocators
from utils.data_generators import generate_user_fullname

@allure.title("Регистрация, логин, открытие счета, выпуск карты, логаут")
@allure.feature("Сквозные сценарии")
def test_e2e_user_onboarding_and_card_issue(page: Page):
    login_page = LoginPage(page)
    register_page = RegisterPage(page)
    dashboard_page = DashboardPage(page)
    
    with allure.step("Открываем страницу авторизации"):
        login_page.open_login_page()
        
    with allure.step("Переходим на страницу регистрации"):
        login_page.go_to_register_page()
        
    with allure.step("Проверяем успешный переход на страницу регистрации"):
        expected_register_url = f"{register_page.base_url}/register"
        expect(page).to_have_url(expected_register_url)
        
    with allure.step("Проверяем наличие заголовка Регистрация"):
        expect(page.get_by_role("heading", name="Регистрация")).to_be_visible()
        
    with allure.step("Регистрируем нового пользователя"):
        user = generate_user_fullname()
        register_page.register_new_user(
            fullname=user["fullname"],
            email=user["email"],
            password=user["password"]
        )
        
    with allure.step("Проверяем редирект на страницу логина"):
        expected_login_page = f"{login_page.base_url}/login"
        expect(page).to_have_url(expected_login_page)
        
    with allure.step("Авторизуемся созданным пользователем"):
        login_page.login_with_custom_credentials(
            email=user["email"],
            password=user["password"]
        )
        
    with allure.step("Проверяем успешный логин"):
        expected_dashboard_url = f"{login_page.base_url}/dashboard"
        expect(page).to_have_url(expected_dashboard_url)
        
    with allure.step("Проверяем, что у нового пользователя нет открытого счета"):
        expect(page.get_by_role("heading", name="Счёт не открыт")).to_be_visible()
        
    with allure.step("Проверяем наличие кнопки для открытия нового счета"):
        expect(page.get_by_role("button", name="Открыть счёт")).to_be_visible()
        
    with allure.step("Открываем новый счет"):
        dashboard_page.open_account()
        
    with allure.step("Проверяем отображение счета"):
        expect(page.get_by_test_id(DashboardLocators.ACCOUNT_CARD)).to_be_visible()
        
    with allure.step("Нажимаем на кнопку Выпустить карту"):
        dashboard_page.click_issue_card_button()
        
    with allure.step("Проверяем, что в поле держателя карты подставилось ФИО пользователя"):
        expect(page.get_by_role("textbox", name="Держатель карты (латиница)")).to_have_value(user["fullname"])
        
    with allure.step("Нажимаем на кнопку Выпустить карту возле поля держателя"):
        dashboard_page.confirm_issue_card()
        
    with allure.step("Проверяем открытие поповера для сохранения данных карты"):
        expect(page.get_by_role("heading", name="Карта выпущена — сохраните данные")).to_be_visible()
        
    with allure.step("Сохраняем данные карты"):
        dashboard_page.save_card()
        
    with allure.step("Проверяем отображение выпущенной карты"):
        expect(page.get_by_test_id(DashboardLocators.BANK_CARD)).to_be_visible()
        
    with allure.step("Выходим из аккаунта"):
        dashboard_page.click_logout_button()
        
    with allure.step("Проверяем переход на страницу логина и делаем финальный скриншот"):
        expect(page).to_have_url(expected_login_page)
        allure.attach(
            page.screenshot(),
            name="Финальное состояние после выхода",
            attachment_type=allure.attachment_type.PNG
        )