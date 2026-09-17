import re
from playwright.sync_api import Page, expect

def test_example(page: Page) -> None:
        page.get_by_role("link", name="Bill Pay")
        page.locator("input[name=\"payee.name\"]")
        page.locator("input[name=\"payee.name\"]").fill("xyz")
        page.locator("input[name=\"payee.address.street\"]").click()
        page.locator("input[name=\"payee.address.street\"]").fill("hubbali")
        page.locator("input[name=\"payee.address.city\"]").click()
        page.locator("input[name=\"payee.address.street\"]").fill("SDM hubbali")
        page.locator("input[name=\"payee.address.city\"]").click()
        page.locator("input[name=\"payee.address.city\"]").fill("hubbali")
        page.locator("input[name=\"payee.address.state\"]").click()
        page.locator("input[name=\"payee.address.state\"]").fill("karnataka")
        page.locator("input[name=\"payee.address.zipCode\"]").click()
        page.locator("input[name=\"payee.address.zipCode\"]").fill("586101")
        page.locator("input[name=\"payee.phoneNumber\"]").click()
        page.locator("input[name=\"payee.phoneNumber\"]").fill("9342315679")
        page.locator("input[name=\"payee.accountNumber\"]").click()
        page.locator("input[name=\"payee.accountNumber\"]").fill("134467")
        page.locator("input[name=\"verifyAccount\"]").click()
        page.locator("input[name=\"verifyAccount\"]").fill("134467")
        page.locator("input[name=\"amount\"]").click()
        page.locator("input[name=\"amount\"]").fill("10000")
        page.get_by_role("button", name="Send Payment").click()
        