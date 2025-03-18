import pytest_playwright as playwright
# from hamcrest import *

from playwright.sync_api import sync_playwright, expect, Page

def get_pw_driver(playwright):

    # with sync_playwright() as playwright_context:
    #     # Launch the browser
    #     browser = playwright_context.chromium.launch(headless=False, slow_mo=1000)
    #     context = browser.new_context()
    #
    #     # Start tracing
    #     context.tracing.start(name="trace", screenshots=True, snapshots=True, sources=True)
    #
    #     page = context.new_page()
    #     return page

    play_context = sync_playwright().start()
    # Launch the browser
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()

    # Start tracing
    context.tracing.start(name="trace", screenshots=True, snapshots=True, sources=True)

    page = context.new_page()

    return page
