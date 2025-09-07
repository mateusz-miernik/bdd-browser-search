"""
    File with base class for page object models
"""

from abc import ABC, abstractmethod
from playwright.sync_api import Page


class BasePage(ABC):
    def __init__(self, session: Page, site: str):
        self.page = session
        self.url = f"https://{site}"

    @abstractmethod
    def _validate_static_ui(self):
        ...
