import re
from playwright.sync_api import Page, expect

def test_example(page: Page) -> None:
     page.get_by_role("link", name="Accounts Overview")
     page.get_by_text("Accounts Overview Account")
     