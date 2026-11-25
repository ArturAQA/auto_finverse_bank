import allure
from playwright.sync_api import Page, expect
from pages.dashboard_page import DashboardPage
from locators.dashboard_locators import DashboardLocators

@allure.title("Успешная блокировка карты")
@allure.feature("Действия с картой")
def test_block_card(logged_in_page: Page):
    dashboard_page = DashboardPage(logged_in_page)
    
    if logged_in_page.locator(DashboardLocators.BLOCKED_CARD_BADGE).first.is_visible():
        dashboard_page.unblock_card()
    
    with allure.step("Нажимаем на кнопку Блокировать"):
        dashboard_page.block_card()
        
    with allure.step("Проверяем отображение что карта заблокирована"):
        expect(logged_in_page.locator(DashboardLocators.BLOCKED_CARD_BADGE).first).to_be_visible()