"""
Fixture module.
"""
import pytest
from playwright.sync_api import Page

from pages.calendars_page import CalendarPage

@pytest.fixture
def calendar_page(page: Page) -> CalendarPage:
    """
    Construct the page object CalendarPage.
    """
    return CalendarPage(page)
