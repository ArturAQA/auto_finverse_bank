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
    """Создаем контекст с фиксированным разрешением экрана и записью видео"""
    ctx = browser.new_context(
        viewport={"width": 1280, "height": 720},
        record_video_dir="videos/",
    )
    yield ctx
    ctx.close()

@pytest.fixture()
def page(context, request):
    """Новая вкладка для каждого теста"""
    pg = context.new_page()
    yield pg
    pg.close()
    
    # Используем твою функцию из курса при падении теста
    rep_call = getattr(request.node, "rep_call", None)
    if rep_call and rep_call.failed:
        attach_video(pg)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Хук для создания скриншотов при падении теста"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page") or item.funcargs.get("logged_in_page")
        if page:
            allure.attach(
                page.screenshot(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )

@pytest.fixture()
def logged_in_page(page):
    """Фикстура для автоматической авторизации перед тестом"""
    login_page = LoginPage(page)
    login_page.open_login_page()
    login_page.login_with_env_credentials()
    expect(page.get_by_test_id(HeaderLocators.LOGOUT_BUTTON)).to_be_visible()
    return page
