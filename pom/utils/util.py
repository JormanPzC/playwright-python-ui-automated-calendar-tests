"""
	Module of general functions.
"""
import datetime
import random
from calendar import monthrange
from dateutil.relativedelta import relativedelta


def add_days(date_received, days_to_add):
    """
    It is used to add days to a date.
    :param date date_received: Base date to add days.
    :param int days_to_add: Number of days to add to the date, it can be a negative number.
    :return: Date with the added days.
    """
    added_days_date = date_received + datetime.timedelta(days=days_to_add)
    return added_days_date


def random_int_from_interval(min_number: int,  max_number: int) -> int:
    """
    It is used  to get a random number between two numbers.
    :param int min: Lowest number.
    :param int max: Highest number.
    :return: A random number between the min and max numbers.
    """
    random_number = random.randint(min_number, max_number)
    return random_number


def random_upper_date():
    """
    It is used to get a random date greater than the current date, with a limit of up to 20 years.
    :return: Random date greater that current date.
    """
    max_days = 20 * 365  # approximately the number of days in 20 years
    random_days = random_int_from_interval(1, max_days)
    return add_days(datetime.datetime.utcnow(), random_days)


def random_under_month_date():
    """
    It is used to get a random date from the current date previous month.
    :return: Random date from the current date previous month.
    """
    date_now = datetime.datetime.utcnow()
    previous_month_date = date_now - relativedelta(months=1)
    num_days_in_previous_month = monthrange(
        date_now.year, previous_month_date.month)[1]
    random_days = random_int_from_interval(1, num_days_in_previous_month)

    # Setting the date to the first day of the previous month
    previous_month_date = add_days(
        previous_month_date, - previous_month_date.day + 1)
    return add_days(previous_month_date, random_days)


def screenshot_name_generator(test_case_code: str, part_number: str, test_case_part: str, date: datetime) -> str:
    """
    It is used to generate a name and route for a screenshot using 
    the current time and test case number.
    :param str test_case_code: identifier code of the test case.
    :param str part_number: number to specific the order of the screenshots.
    :param str test_case_part: part name of the test case.
    :param datetime date: full date of the moment the tests begin.
    :return: screenshot name and route.
    """
    str_aux_date = date.strftime("%m-%d-%Y_%H-%M-%S")
    screenshot_route = f"screenshots/{str_aux_date}/{test_case_code}_{part_number}_{test_case_part}_{str_aux_date}.png"
    return screenshot_route
