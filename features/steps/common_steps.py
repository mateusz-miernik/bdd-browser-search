"""
    File with common behave steps
"""

from behave import given
from pages.google_page import GooglePage
from pages.bing_page import BingPage


@given('I am on "{site}"')
def step_impl(context, site):
    if "google" in site:
        context.page_obj = GooglePage(context.page, site)
        context.page_obj.open()
    elif "bing" in site:
         context.page_obj = BingPage(context.page, site)
         context.page_obj.open()
    else:
        raise ValueError(f"Unsupported site: {site}")
