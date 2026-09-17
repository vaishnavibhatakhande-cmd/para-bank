import re
from playwright.sync_api import Page, expect

def test_example(page: Page) -> None:
        page.get_by_role("link", name="Request Loan").click()
        page.locator("#amount").click()
        page.locator("#amount").fill("200000")
        page.locator("#downPayment").click()
        page.locator("#downPayment").fill("10000")
        page.get_by_role("button", name="Apply Now").click()
        page.get_by_text("Loan Request Processed Loan").click()