import pytest
from playwright.sync_api import Page


@pytest.fixture(scope="function", autouse=True)
def setup(page: Page, request):
    page.goto("https://parabank.parasoft.com/parabank/index.htm")
    yield page
    tcname = request.node.name
    page.screenshot(path=f"./screenshots/{tcname}.png", full_page=True)
    page.close()