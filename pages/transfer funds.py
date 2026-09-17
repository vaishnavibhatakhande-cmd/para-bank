import re
from playwright.sync_api import Page, expect

def test_example(page: Page) -> None:

    page.get_by_role("link", name="Transfer Funds")
    page.locator("#amount")
    page.locator("#amount").fill("10,000")
    page.get_by_role("button", name="Transfer")
    page.locator("#amount")
    page.locator("#amount").fill("10,0000")
    page.get_by_role("button", name="Transfer")
    page.get_by_role("link", name="Transfer Funds")