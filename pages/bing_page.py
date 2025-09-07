"""
    File with class for Bing search page object models
"""

from playwright.sync_api import Page
from pages.base_page import BasePage


class BingPage(BasePage):
    def __init__(self, page: Page, site: str):
        super().__init__(page, site)

    def _validate_static_ui(self):
        ...

    def open(self):
        self.page.goto(self.url)

    def search(self, query: str):
        raise NotImplementedError('Feature not implemented')

    def apply_category_filter(self, category: str):
        raise NotImplementedError('Feature not implemented')

    def results_filtered_by_category(self, category: str, query: str) -> bool:
        raise NotImplementedError('Feature not implemented')

    def related_searches_available(self) -> bool:
        raise NotImplementedError('Feature not implemented')
