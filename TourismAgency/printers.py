def print_offers(offers):
    """
        Prints all offers, one per line, in the format:
        destination, start date, end date, price
        :param offers: the list of offers
        :return: -
    """

    for offer in offers:
        print(offer[0] + ", " + offer[1] + ", " + offer[2] + ", " + str(offer[3]))



def print_numbered_offers(offers):
    """
        Prints all offers, one per line, numbered starting from 1.
        Used when the user has to choose an offer from the list.
        :param offers: the list of offers
        :return: -
    """

    for i in range(len(offers)):
        offer = offers[i]
        print(str(i + 1) + ". " + offer[0] + ", " + offer[1] + ", " + offer[2] + ", " + str(offer[3]))
