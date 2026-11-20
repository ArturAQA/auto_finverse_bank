import allure
import pytest
from dotenv import load_dotenv
from playwright.sync_api import expect
from locators.header_locators import HeaderLocators
from pages.login_page import LoginPage
from utils.video_recording import attach_video

load_dotenv()

@pytest.fixture()
def context(browser):
    """Создаем контекст с фиксированным разрешением экрана"""
    ctx = browser.new_context(
        viewport={"width": 1280, "height": 720},
    )
    yield ctx
    ctx.close()

@pytest.fixture()
def page(context):
    """Новая вкладка для каждого теста"""
    pg = context.new_page()
    yield pg
    pg.close()

# Хук для создания скриншотов при падении теста
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        if "page" in item.fixturenames:
            page = item.funcargs["page"]
            screenshot = page.screenshot()
            allure.attach(
                screenshot,
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )
            attach_video(page)

@pytest.fixture()
def logged_in_page(page):
    """Фикстура для автоматической авторизации перед тестом"""
    login_page = LoginPage(page)
    login_page.open_login_page()
    login_page.login_with_env_credentials()
    expect(page.get_by_test_id(HeaderLocators.LOGOUT_BUTTON)).to_be_visible()
    return page
                