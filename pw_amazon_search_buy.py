"""
Playwright Automation

1. Navigate to https://www.amazon.in/
2. Search for “Tiffin box”
3. Sort by lowest price
4. Verify the price is really in ascending order
5. Apply the filter Color “Purple”
6. Select second tiffin box
7. Now Try to buy the second product from the “Tiffin box”
8. Verify the price is correct from product details page and in Checkout page
"""

from hamcrest import *
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright_context:

    # Launch the browser
    browser = playwright_context.chromium.launch(headless=False, slow_mo=1000)
    browser_context = browser.new_context()

    # Start tracing
    browser_context.tracing.start(name="trace", screenshots=True, snapshots=True, sources=True)

    page = browser_context.new_page()
    # 1. Navigate to https://www.amazon.in/
    page.goto("https://www.amazon.in/")

    # 2. Search for “Tiffin box”
    page.fill(selector="//input[@id='twotabsearchtextbox']", value="Tiffin box")
    page.click(selector="//input[@id='nav-search-submit-button']")

    # 3. Sort by lowest price
    # Element - Drop-down -> Featured
    page.click(selector="//span[contains(text(), 'Featured')]")
    # Element - Drop-down Value -> Price: Low to High
    page.click(selector="//a[contains(text(), 'Price: Low to High')]")


    # 4. Verify the price is really in ascending order
    # TODO

    # 5. Apply the filter color - “Purple”
    purple_locator = page.locator(selector="//a[@title='Purple']/span/div")
    purple_locator.scroll_into_view_if_needed()
    purple_locator.click()

    # 6. Select second tiffin box
    page.click(selector="//div[@data-index='5']")

    print(browser_context.pages)
    print(browser_context.pages[1].url)

    # Fetch handle of new tab/window
    page2 = browser_context.pages[1]

    # 7. Now Try to buy the second product from the “Tiffin box”

    # Fetch product price
    product_price_element = page2.locator(selector="//div[@id='corePriceDisplay_desktop_feature_div']//span[@class='a-price-whole']")
    product_price = product_price_element.text_content().strip()
    print("Price on product page is: ", product_price)

    # Click on "Add to cart" button
    page2.click(selector="//input[@id='add-to-cart-button']")
    # page2.click(selector="[id='add-to-cart-button']")

    # 8. Verify the price is correct from product details page and in Checkout page
    cart_price_element = page2.locator(selector="//div[@id='sw-subtotal']//span[@class='a-price-whole']")
    cart_price = cart_price_element.text_content().strip()[:-1] # Ignore last element by removing decimal from the price value.
    print("Price on cart/checkout page is: ", cart_price)

    # expect(cart_price).to_have_text(product_price)
    assert_that(cart_price, equal_to(product_price), "Assert failed!!!!")


    # locator_assertions.to_have_text()

    # Take screenshot
    page2.screenshot(path="test-results/amazon.png")

    # Stop tracing and export to ZIP file
    browser_context.tracing.stop(path="test-results/trace.zip")


    browser_context.close()
    browser.close()
