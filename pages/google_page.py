"""
    File with class for Google search page object models
"""

from playwright.sync_api import Page
from pages.base_page import BasePage

class GooglePage(BasePage):
    def __init__(self, page: Page, site: str):
        super().__init__(page, site)

    def _validate_static_ui(self):
        ...

    def open(self):
        self.page.goto(self.url)

    def search(self, query: str):
        raise NotImplementedError('Feature not implemented')

    def apply_date_filter(self, filter_name: str):
        raise NotImplementedError('Feature not implemented')

    def results_within_last_week(self, query: str) -> bool:
        raise NotImplementedError('Feature not implemented')
