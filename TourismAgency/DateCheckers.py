from Offers import get_start, get_end
def is_valid_date(day, month, year):
    """
       Checks if day, month and year form a valid date.
       :param day: the day (str)
       :param month: the month (str)
       :param year: the year (str, must have 4 digits)
       :return: True if the date is valid, False otherwise
    """

    if not (day.isdigit() and month.isdigit() and year.isdigit()):
        return False

    if len(year) != 4:
        return False

    day = int(day)
    month = int(month)
    year = int(year)

    if month < 1 or month > 12:
        return False



    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0:
        days_in_month[1] = 29

    if day >= 1 and day <= days_in_month[month - 1]:
        return True
    else:
        return False

def date_checker(day, month, year, day1, month1, year1):
    """
        Checks if both dates are valid and the end date is not before the start date.
        Each date is turned into a number of the form yyyymmdd, so they can be compared
        (ex. 13/09/2026 -> 20260913, 02/10/2026 -> 20261002).
        :param day, month, year: the start date (strings)
        :param day1, month1, year1: the end date (strings)
        :return: True if both dates are valid and start date <= end date, False otherwise
    """
    if not is_valid_date(day, month, year) or not is_valid_date(day1, month1, year1):
        return False
    start = int(year) * 10000 + int(month) * 100 + int(day)
    end = int(year1) * 10000 + int(month1) * 100 + int(day1)
    return start <= end


def make_date(day, month, year):
    """
        Builds a date string in the format dd/mm/yyyy.
        Adds a 0 in front of the day or month if they have only one digit.
        :param day: the day (str)
        :param month: the month (str)
        :param year: the year (str)
        :return: the date as a string, ex. "08/03/2026"
    """
    if len(day) == 1:
        day = "0" + day
    if len(month) == 1:
        month = "0" + month
    return day + "/" + month + "/" + year


def duration(offer):
    """
    Returns the number of days between the start and end date of an offer.
    :param offer: the offer
    :return: the number of days between the start and end date of an offer
    :return: type int
    """
    before = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    d1, m1, y1 = get_start(offer).split("/")
    d2, m2, y2 = get_end(offer).split("/")
    start = int(y1) * 365 + before[int(m1) - 1] + int(d1)
    end = int(y2) * 365 + before[int(m2) - 1] + int(d2)
    return end - start

