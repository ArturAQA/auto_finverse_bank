import allure
from playwright.sync_api import Page, expect
from pages.dashboard_page import DashboardPage
from locators.dashboard_locators import DashboardLocators

@allure.title("Успешная разблокировка карты")
@allure.feature("Действия с картой")
def test_unblock_card(logged_in_page: Page):
    dashboard_page = DashboardPage(logged_in_page)
    
    if logged_in_page.locator(DashboardLocators.ACTIVE_CARD_BADGE).first.is_visible():
        dashboard_page.block_card()
    
    with allure.step("Нажимаем на кнопку Разблокировать"):
        dashboard_page.unblock_card()
        
    with allure.step("Проверяем отображение что карта активна"):
        expect(logged_in_page.locator(DashboardLocators.ACTIVE_CARD_BADGE).first).to_be_visible()