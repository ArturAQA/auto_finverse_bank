import os
import allure
import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

# Импортируем твой кастомный модуль (теперь с маленькой буквы!)
from utils.video_recording import attach_video

# Вызываем подгрузку .env после того, как все импорты завершены
load_dotenv()


@pytest.fixture()
def context(browser):
    ctx = browser.new_context(
        viewport={"width": 1280, "height": 720},
    )
    yield ctx
    ctx.close()

@pytest.fixture()
def page(context):
    pg = context.new_page()
    yield pg
    pg.close()
    
    
@pytest.fixture(scope="session")
def browser():
    """Один браузер на весь прогон — это быстро."""
    with sync_playwright() as p:
        b = p.chromium.launch(headless=True)
        yield b
        b.close()

@pytest.fixture()
def page(browser):
    """Новая страница для каждого теста — изоляция."""
    context = browser.new_context()
    pg = context.new_page()
    yield pg
    context.close()
    
    
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