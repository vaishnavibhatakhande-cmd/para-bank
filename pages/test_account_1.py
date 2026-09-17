import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://parabank.parasoft.com/parabank/overview.htm")
    page.locator("input[name=\"username\"]").fill("john")
    page.locator("input[name=\"password\"]")
    page.get_by_role("button", name="Log In")
    page.get_by_role("button", name="Open New Account")
    page.get_by_role("link", name="13566")
    page.get_by_role("button", name="Go")

   