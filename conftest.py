import pytest

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
