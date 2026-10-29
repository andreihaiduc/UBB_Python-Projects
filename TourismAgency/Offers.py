id_offer = 0


def create_offer(destination, start, end, price):
    """
     Creates the offer entity.

    :param destination: the location of the vacation
    :destination type: string
    :param start: the start date of the vacation
    :start type: string
    :param end: the end date of the vacation
    :end type: string
    :param price: the price of the offer
    :price type: float
    :return: offer entity
    """

    global id_offer
    id_offer = id_offer + 1
    offer = [id_offer, destination, start, end, price]

    return offer


def get_id(offer):
    """
    Returns the id of the offer.

    :param offer: offer entity
    :return: id of the offer
    :return type: int
    """
    return offer[0]


def get_destination(offer):
    """
    Returns the destination of the offer.

    :param offer: offer entity
    :return: the destination of the offer
    :return type: string
    """
    return offer[1]


def get_start(offer):
    """
    Returns the start date of the offer.

    :param offer: the offer entity
    :return: the start date of the offer
    :return type: string
    """
    return offer[2]


def get_end(offer):
    """
    Returns the end date of the offer.

    :param offer: the offer entity
    :return: the end date of the offer
    :return type: string
    """
    return offer[3]


def get_price(offer):
    """
    Returns the price of the offer.

    :param offer: the offer entity
    :return: the price of the offer
    :return type: float
    """
    return offer[4]


def set_destination(offer, new_destination):
    """
    Changes the destination to the new_destination.

    :param offer:offer entity
    :param new_destination: new destination entity
    :type new_destination: string
    :return:
    """
    offer[1] = new_destination


def set_start(offer, new_start):
    """
    Changes the start date of the offer to the new_start.

    :param offer: offer entity
    :param new_start: new start date of the offer
    :type new_start: string
    :return:
    """
    offer[2] = new_start


def set_end(offer, new_end):
    """
    Changes the end date of the offer to the new_end.

    :param offer: offer entity
    :param new_end: new end date of the offer
    :type new_end: string
    :return:
    """
    offer[3] = new_end


def set_price(offer, new_price):
    """
    Changes the price of the offer to the new_price.

    :param offer: offer entity
    :param new_price: the new price of the offer
    :type new_price: float
    :return:
    """
    offer[4] = new_price
