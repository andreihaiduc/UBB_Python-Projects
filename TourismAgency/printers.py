from DateCheckers import date_checker,make_date
from Offers import get_destination, get_start, get_end, get_price


def print_offers(offers):
    """
    Prints all offers, one per line, in the format:
    destination, start date, end date, price
    :param offers: the list of offers
    :return: -
    """
    for offer in offers:
        print(get_destination(offer) + ", " + get_start(offer) + ", " + get_end(offer) + ", " + str(get_price(offer)))


def print_numbered_offers(offers):
    """
    Prints all offers, one per line, numbered starting from 1.
    Used when the user has to choose an offer from the list.
    :param offers: the list of offers
    :return: -
    """
    for i in range(len(offers)):
        offer = offers[i]
        print(str(i + 1) + ". " + get_destination(offer) + ", " + get_start(offer) + ", " + get_end(offer) + ", " + str(
            get_price(offer)))


def offers_in_interval(offers, day, month, year, day1, month1, year1):
    """
    Returns the offers which take place entirely in the given interval.
    :param offers: the list of offers
    :param day, month, year: the start of the interval (strings)
    :param day1, month1, year1: the end of the interval (strings)
    :return: a new list with the offers in the interval
    """
    result = []
    for offer in offers:
        sd, sm, sy = get_start(offer).split("/")
        ed, em, ey = get_end(offer).split("/")
        if date_checker(day, month, year, sd, sm, sy) and date_checker(ed, em, ey, day1, month1, year1):
            result.append(offer)
    return result


def destination_lower_price(offers, destination, price):
    """
    Returns the offers which take place in a given destination with the condition that the price is smaller than the given price.
    :param offers: the list of offers
    :param destination: the destination
    :param price: the price
    :return: a new list with the available offers
    """
    result = []
    for offer in offers:
        dest = get_destination(offer)
        pr = get_price(offer)
        if destination == dest and pr < price:
            result.append(offer)

    return result


def offers_end_date(offers, day1, month1, year1):
    """
    Returns the offers which end on the given date.
    :param offers: the list of offers
    :param day1: the end day (str)
    :param month1: the end month (str)
    :param year1: the end year (str)
    :return: a new list with the offers ending on the given date
    """
    end_date = make_date(day1, month1, year1)
    result = []
    for offer in offers:
        if get_end(offer) == end_date:
            result.append(offer)
    return result

def print_averagep_destination(offers, destination):
    """
    Returns the average price of the vacations for a given destination.
    :param offers: the list of offers
    :param destination: the destination
    :return: an average price of the vacations
    """
    avg_price = 0
    sum_price = 0
    count=0
    for offer in offers:
        if destination == get_destination(offer):
            count = count + 1
            sum_price = sum_price + get_price(offer)
    avg_price = sum_price / count
    return avg_price
def count_offers_per_destination(offers):
    """
    Counts the number of offers for each destination.
    :param offers: the list of offers
    :return: a list of pairs [destination, number of offers]
    """
    destinations = []
    result = []
    for offer in offers:
        dest = get_destination(offer)
        if dest in destinations:
            i = destinations.index(dest)
            result[i][1] = result[i][1] + 1
        else:
            destinations.append(dest)
            result.append([dest, 1])
    return result

def print_from_substring(offers,substring):
    """
    Returns the list of offers that contain in their destination's name a given substring.
    :param offers: the list of offers
    :param substring: the substring
    :return: an ordered list of offers that contain in their destination's name the given substring
    """

    result = []
    for offer in offers:
        if substring in get_destination(offer):
            result.append(offer)
    for i in range(len(result) - 1):
        for j in range(i + 1, len(result)):
            if get_destination(result[i]) > get_destination(result[j]):
                result[i], result[j] = result[j], result[i]
    return result

def print_two_best_offers(offers, day, month, year, day1, month1, year1):
    """
        Returns the two cheapest offers which take place in the given interval.
        :param offers: the list of offers
        :param day, month, year: the start of the interval (strings)
        :param day1, month1, year1: the end of the interval (strings)
        :return: a new list with at most two offers, the cheapest first
        """
    result = offers_in_interval(offers, day, month, year, day1, month1, year1)
    for i in range(len(result) - 1):
        for j in range(i + 1, len(result)):
            if get_price(result[i]) > get_price(result[j]):
                result[i], result[j] = result[j], result[i]
    return result[:2]


