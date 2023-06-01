"""
This module contains CalendarPage,
the page object for the sdet-challenge page.
"""
import re
from datetime import datetime
from playwright.sync_api import Page, expect

from data.constants import CALENDAR_SITE, MONTHS, get_month_by_abbr_name


class CalendarPage:
    """
    Page objet CalendarPage. This class represent the calendars page.
    """

    # pylint: disable=too-many-instance-attributes
    def __init__(self, page: Page) -> None:
        self.page = page
        self.url = CALENDAR_SITE
        self.first_date_input_display_locator = page.get_by_placeholder(
            'Early')
        self.second_date_input_display_locator = page.get_by_placeholder(
            'Continuous')
        self.previous_month_button_locator = page.locator(
            "css=button[class*='rdrPprevButton']")
        self.next_month_button_locator = page.locator(
            "css=button[class*='rdrNextButton']")
        self.month_picker_locator = page.locator("span").filter(has_text=re.compile(
            r"^JanuaryFebruaryMarchAprilMayJuneJulyAugustSeptemberOctoberNovemberDecember$")).get_by_role("combobox")
        self.year_picker_locator = page.get_by_role(
            'combobox').locator("nth=1")
        self.first_calendar_month_year_locator = page.locator(
            "xpath=(//div[contains(@class,'rdrMonthsHorizontal')]/div[@class='rdrMonth']/div[@class='rdrMonthName'])[1]")
        self.second_calendar_month_year_locator = page.locator(
            "xpath=(//div[contains(@class,'rdrMonthsHorizontal')]/div[@class='rdrMonth']/div[@class='rdrMonthName'])[2]")
        self.day_in_calendar_locator = None


    def load(self) -> None:
        """
        It is used to go to the calendar page.
        """
        self.page.goto(self.url)


    def get_day_in_calendar_locator(self, day: str, calendar: int):
        """
        It is used to get the locator of a day located in one of the calendars.
        :param str day: String of the number day to located in one of the calendars. 
        :param int calendar: Number of the calendar in which the day must be located. 
        :return: Locator of the day to click in one of the calendars.
        """
        day_in_calendar_locator = self.page.locator(f"xpath=(//button[not(contains(@class,'rdrDayPassive'))]//span[contains(@class, 'rdrDayNumber')] [span = {day}]) [{calendar}]")
        return day_in_calendar_locator
        #return self.page.locator(f"xpath=(//button[not(contains(@class,'rdrDayPassive'))]//span[contains(@class, 'rdrDayNumber')] [span = {day}]) [{calendar}]")


    def click_day(self, date: datetime) -> None:
        """
        It is used to click a day in one of the calendars using a date received.
        :param date date: Date wanted to click on one of the calendars.  
        """
        # Getting the year and month of the date received.
        year_received = date.year
        month_received = MONTHS[date.month - 1]['month']

        # Getting the months and years of the first and second calendars.
        # E.g value: "Jan 2023"
        first_calendar_month_year = self.first_calendar_month_year_locator.inner_text()
        current_month_first_calendar = get_month_by_abbr_name(
            first_calendar_month_year[0:3])
        # E.g value: "Feb 2023"
        second_calendar_month_year = self.second_calendar_month_year_locator.inner_text()
        current_month_second_calendar = get_month_by_abbr_name(
            second_calendar_month_year[0:3])
        month_year_selected = first_calendar_month_year
        year_selected = month_year_selected[4:9]

        if not self.is_year_in_valid_range(year_received):
            print('Failure - Year displayed in first calendar is out of valid range.')

        # The year received is not the same that the year displayed in the calendars?
        if year_received != int(year_selected):
            # Then change the year selected using the year picker.
            self.select_year(year_received)

            # Update the values because are neccesary for validations.
            first_calendar_month_year = self.first_calendar_month_year_locator.inner_text()
            second_calendar_month_year = self.second_calendar_month_year_locator.inner_text()
            month_year_selected = first_calendar_month_year
            year_selected = month_year_selected[4:9]

        # The month received is not one of the months displayed in the calendars?
        # The second part of the validation is for the case when in the first calendar
        # the month is December and the second calendar the month is January of the next year.
        if (month_received["abbr_name"] != current_month_first_calendar['month']["abbr_name"] and month_received["abbr_name"] != current_month_second_calendar['month']["abbr_name"]) or (month_received["abbr_name"] == current_month_second_calendar['month']["abbr_name"] and year_received != int(second_calendar_month_year[4:9])):
            # Then change the month selected using the month picker.
            self.select_month(month_received["full_name"])

            # Update the values because are neccesary for validations.
            first_calendar_month_year = self.first_calendar_month_year_locator.inner_text()
            current_month_first_calendar = get_month_by_abbr_name(
                first_calendar_month_year[0:3])
            second_calendar_month_year = self.second_calendar_month_year_locator.inner_text()
            current_month_second_calendar = get_month_by_abbr_name(
                second_calendar_month_year[0:3])
            month_year_selected = self.first_calendar_month_year_locator.inner_text()

        month_year_received = month_received["abbr_name"] + \
            " " + str(year_received)
        day_received = date.day

        # Evaluate in which calendar the day must be clicked and click the day
        if month_year_received == first_calendar_month_year:
            self.day_in_calendar_locator = self.get_day_in_calendar_locator(str(day_received), 1)
            self.day_in_calendar_locator.click()
        elif month_year_received == second_calendar_month_year:
            self.day_in_calendar_locator = self.get_day_in_calendar_locator(str(day_received), 2)
            self.day_in_calendar_locator.click()
        else:
            raise ValueError(
                f'(Failure - Day in the date {date} was not found in neither calendar.')


    @staticmethod
    def is_year_in_valid_range(year: int) -> bool:
        """
        It is used to check if a year is in the valid range of minus 100 years 
        and plus 20 years from the current date.
        :param int year: Year to check. 
        :return: Boolean of the year validity.
        """
        current_date = datetime.utcnow()
        min_valid_year = current_date.year - 100
        max_valid_year = current_date.year + 20
        #return year >= min_valid_year and year <= max_valid_year
        return min_valid_year <= year <= max_valid_year


    def select_month(self, full_name_month: str) -> None:
        """
        It is used to open the month dropdown and click a month.
        :param str full_name_month: Name of the month to click in the month dropdown. 
        """
        self.month_picker_locator.click()
        # Get the index of the a month in the Json array MONTHS
        index = next((i for i, month in enumerate(MONTHS) if month['month']['full_name'] == full_name_month), None)
        self.month_picker_locator.select_option(str(index))


    def select_year(self, year: int) -> None:
        """
        It is used to open the year dropdown and click a year.
        :param int year: Year to click in the year dropdown.
        :return:
        """
        is_year_valid = self.is_year_in_valid_range(year)

        if is_year_valid:
            self.year_picker_locator.click()
            self.year_picker_locator.select_option(str(year))
        else:
            print(
                f'(Failure - The year {year} received is out the valid range.)')
            raise ValueError(
                f'(Failure - The year {year} received is out the valid range.)')


    def compare_range_input_dates_with_clicked_dates(self, expected_start_date: datetime, expected_end_date: datetime) -> None:
        """
        It is used to check if the input dates displayed are 
        the correct ones after clicked two dates.
        :param date expected_start_date: First date clicked in one of the calendars.
        :param date expected_end_date: Second date clicked in one of the calendars.
        """
        if expected_start_date <= expected_end_date:
            expect(self.first_date_input_display_locator).to_have_value(self.__build_input_date(expected_start_date))
            expect(self.second_date_input_display_locator).to_have_value(self.__build_input_date(expected_end_date))
        else:
            expect(self.first_date_input_display_locator).to_have_value(self.__build_input_date(expected_end_date))
            expect(self.second_date_input_display_locator).to_have_value(self.__build_input_date(expected_start_date))


    @staticmethod
    def __build_input_date(date: datetime) -> str:
        """
        It is used to get a string of the date received to compare with the calendars Date input 
        displayed in the calendars.
        :param date date: Date to transform in the format used in the input date.
        :return: String of the date in a especif format. E.g "Feb 6, 2023".
        """
        year = date.year
        month_index = date.month - 1
        # Abbreviated month name
        abbr_month = MONTHS[month_index]['month']['abbr_name']
        day = date.day
        # E.g "Feb 6, 2023".
        return abbr_month + " " + str(day) + "," + " " + str(year)
