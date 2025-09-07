"""
    Environment file for playwright setup/teardown
"""

from playwright.sync_api import sync_playwright


# setup
def before_all(context):
    context.playwright = sync_playwright().start()
    browser = context.playwright.firefox.launch(headless=True)
    context.browser = browser
    context.page = browser.new_page()

# teardown
def after_all(context):
    context.browser.close()
    context.playwright.stop()
