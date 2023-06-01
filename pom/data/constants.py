"""
Module of constants variables
"""
CALENDAR_SITE = "https://sdet-challenge.vercel.app/"
"""
This variable is an array that contains the json of 12 months. 
Each month has their full and abbreviated names. 
"""

FULL_SCREENSHOT = False
"""
This variable is to activate or not the manual screenshot in key parts of the test.
In fact this variable should be in a .env file.
"""

MONTHS = [
    {
        'month': {
            'full_name': 'January',
            'abbr_name': 'Jan',
        },
    },
    {
        'month': {
            'full_name': 'February',
            'abbr_name': 'Feb',
        },
    },
    {
        'month': {
            'full_name': 'March',
            'abbr_name': 'Mar',
        },
    },
    {
        'month': {
            'full_name': 'April',
            'abbr_name': 'Apr',
        },
    },
    {
        'month': {
            'full_name': 'May',
            'abbr_name': 'May',
        },
    },
    {
        'month': {
            'full_name': 'June',
            'abbr_name': 'Jun',
        },
    },
    {
        'month': {
            'full_name': 'July',
            'abbr_name': 'Jul',
        },
    },
    {
        'month': {
            'full_name': 'August',
            'abbr_name': 'Aug',
        },
    },
    {
        'month': {
            'full_name': 'September',
            'abbr_name': 'Sep',
        },
    },
    {
        'month': {
            'full_name': 'October',
            'abbr_name': 'Oct',
        },
    },
    {
        'month': {
            'full_name': 'November',
            'abbr_name': 'Nov',
        },
    },
    {
        'month': {
            'full_name': 'December',
            'abbr_name': 'Dec',
        },
    },
]


def get_month_by_abbr_name(month: str):
    """
    It is used search the json month object using an abbreviate month name.
    :param str month: Month abbreviated name, E.g 'Jan'.
    :return: Json object of the month.
    """
    return next(filter(lambda x: x['month']['abbr_name'] == month, MONTHS), None)


def get_month_by_full_name(month: str):
    """
    It is used search the json month object using an full name month name.
:param str month: Month abbreviated name, E.g 'January'. 
:return: Json object of the month.
"""
    return next(filter(lambda x: x['month']['full_name'] == month, MONTHS), None)
