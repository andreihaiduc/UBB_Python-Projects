from DateCheckers import make_date

def add_offer(offers, destination, day, month, year, day1, month1, year1, price):
    """
        Creates an offer from the given data and adds it to the list of offers.
        :param offers: the list of offers
        :param destination: the destination of the offer (str)
        :param day, month, year: the start date (strings)
        :param day1, month1, year1: the end date (strings)
        :param price: the price of the offer (str, converted to float)
        :return: -
    """

    offer = [destination, make_date(day, month, year), make_date(day1, month1, year1), float(price)]
    offers.append(offer)

def modify_price(offers, index, new_price):
    """
        Changes the price of the offer at the given position.
        :param offers: the list of offers
        :param index: the position of the offer in the list (int, starting from 0)
        :param new_price: the new price of the offer (float)
        :return: -
    """

    offers[index][3] = new_price
