from DateCheckers import duration

def remove_from_destination(offers,destination):
    """
        Removes all offers with the given destination.
        :param offers: the list of offers
        :param destination: the destination to remove (str)
        :return: the number of removed offers (int)
        """
    count = 0
    for i in range(len(offers)-1 ,-1,-1):
        if offers[i][0] == destination:
            offers.pop(i)
            count=count+1

    return count
def remove_less_days(offers,days):
    """
        Removes all offers that have a shorter duration than the given number of days.
        :param offers: the list of offers
        :param days: the number of days (int)
        :return: the number of removed offers (int)
    """

    count = 0
    for i in range(len(offers)-1,-1,-1):
        if duration(offers[i]) < days:
            offers.pop(i)
            count=count+1
    return count

def remove_greater_price(offers,price):
    """
        Removes all offers for which the price is greater than the given price.
        :param offers: the list of offers
        :param price: the given price (float)
        :return: the number of removed offers (int)
    """
    count = 0
    for i in range(len(offers)-1,-1,-1):
        if offers[i][3] > price:
            offers.pop(i)
            count=count+1

    return count
