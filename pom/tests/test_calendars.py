"""
This module contains the test of the calendar page.
"""
from datetime import datetime
from playwright.sync_api import Page

from pages.calendars_page import CalendarPage
from utils.util import add_days, random_upper_date, random_under_month_date, screenshot_name_generator
from data.constants import FULL_SCREENSHOT


AUX_DATE = datetime.utcnow()


def test_tc001_start_date_as_today_and_end_date_as_today_plus_7(page: Page, calendar_page: CalendarPage) -> None:
    """
    Test case TC001.
    """
    test_case_code = "TC001"
    print("") # Empty print to better read of the console message
    print(f"Test {test_case_code} starting.")

    #calendar_page = CalendarPage(page)
    calendar_page.load()
    if FULL_SCREENSHOT:
        page.screenshot(path = screenshot_name_generator(test_case_code, "1", "default_calendars", AUX_DATE), full_page=True)

    # GIVEN "Today" as Start date.
    expected_start_date = datetime.utcnow()
    print("expected_start_date", expected_start_date)

    # AND "Today + 7" as End date.
    expected_end_date = add_days(expected_start_date, 7)
    print("expected_end_date", expected_end_date)

    # WHEN selecting these days in the calendars.
    calendar_page.click_day(expected_start_date)
    if FULL_SCREENSHOT:
        page.screenshot(path = screenshot_name_generator(test_case_code, "2", "clicked_first_date", AUX_DATE), full_page=True)

    calendar_page.click_day(expected_end_date)
    if FULL_SCREENSHOT:
        page.screenshot(path = screenshot_name_generator(test_case_code, "3", "clicked_second_date", AUX_DATE), full_page=True)

    # THEN Calendar input range dates match.
    calendar_page.compare_range_input_dates_with_clicked_dates(expected_start_date, expected_end_date)
    print(f"Test {test_case_code} completed.")

def test_tc002_start_date_as_random_day_in_the_future_and_end_date_as_start_date_plus_21(page: Page, calendar_page: CalendarPage) -> None:
    """
    Test case TC002.
    """
    test_case_code = "TC002"
    print("") # Empty print to better read of the console message
    print(f"Test {test_case_code} starting.")

    #calendar_page = CalendarPage(page)
    calendar_page.load()
    if FULL_SCREENSHOT:
        page.screenshot(path = screenshot_name_generator(test_case_code, "1", "default_calendars", AUX_DATE), full_page=True)

    # GIVEN "Random day in the future" as Start date.
    expected_start_date = random_upper_date()
    print("expected_start_date", expected_start_date)

    # AND "Start day + 21" as End date.
    expected_end_date = add_days(expected_start_date, 21)
    print("expected_end_date", expected_end_date)

    # WHEN selecting these days in the calendars.
    calendar_page.click_day(expected_start_date)
    if FULL_SCREENSHOT:
        page.screenshot(path = screenshot_name_generator(test_case_code,  "2", "clicked_first_date", AUX_DATE), full_page=True)

    calendar_page.click_day(expected_end_date)
    if FULL_SCREENSHOT:
        page.screenshot(path = screenshot_name_generator(test_case_code, "3", "clicked_second_date", AUX_DATE), full_page=True)

    # THEN Calendar input range dates match.
    calendar_page.compare_range_input_dates_with_clicked_dates(expected_start_date, expected_end_date)
    print(f"Test {test_case_code} completed.")


def test_tc003_start_date_as_random_day_in_the_previous_month_and_end_date_as_start_date_plus_5(page: Page, calendar_page: CalendarPage) -> None:
    """
    Test case TC003.
    """
    test_case_code = "TC003"
    print("") # Empty print to better read of the console message
    print(f"Test {test_case_code} starting.")

    #calendar_page = CalendarPage(page)
    calendar_page.load()
    if FULL_SCREENSHOT:
        page.screenshot(path = screenshot_name_generator(test_case_code, "1", "default_calendars", AUX_DATE), full_page=True)

    # GIVEN "Random day in the previous month" as Start date
    expected_start_date = random_under_month_date()
    print("expected_start_date", expected_start_date)

    # AND "Start day + 5" as End date.
    expected_end_date = add_days(expected_start_date, 5)
    print("expected_end_date", expected_end_date)

    # WHEN selecting these days in the calendars.
    calendar_page.click_day(expected_start_date)
    if FULL_SCREENSHOT:
        page.screenshot(path = screenshot_name_generator(test_case_code, "2", "clicked_first_date", AUX_DATE), full_page=True)

    calendar_page.click_day(expected_end_date)
    if FULL_SCREENSHOT:
        page.screenshot(path = screenshot_name_generator(test_case_code, "3", "clicked_second_date", AUX_DATE), full_page=True)

    # THEN Calendar input range dates match.
    calendar_page.compare_range_input_dates_with_clicked_dates(expected_start_date, expected_end_date)
    print(f"Test {test_case_code} completed.")
