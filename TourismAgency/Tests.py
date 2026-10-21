from DateCheckers import is_valid_date, date_checker, make_date, duration

from AddModify import add_offer, modify_price

from Removing import remove_from_destination, remove_greater_price, remove_less_days


def get_test_offers():
    """
    Returns a new list with the offers from the problem statement, used in tests.
    """
    return [
        ["Madrid", "11/08/2026", "20/08/2026", 4435.25],
        ["Buenos Aires", "06/03/2026", "21/03/2026", 10215.75],
        ["Athens", "13/09/2026", "19/09/2026", 3298.90],
        ["Cairo", "15/08/2026", "25/08/2026", 3925.30],
        ["Helsinki", "24/09/2026", "02/10/2026", 2010.75],
    ]


def test_is_valid_date():
    assert is_valid_date("11", "8", "2026")
    assert is_valid_date("29", "2", "2028")
    assert not is_valid_date("29", "2", "2026")
    assert not is_valid_date("31", "9", "2026")
    assert not is_valid_date("11", "13", "2026")
    assert not is_valid_date("abc", "8", "2026")
    assert not is_valid_date("11", "8", "26")


def test_date_checker():
    assert date_checker("11", "8", "2026", "20", "8", "2026")
    assert date_checker("24", "9", "2026", "2", "10", "2026")
    assert not date_checker("20", "8", "2026", "11", "8", "2026")
    assert not date_checker("31", "9", "2026", "5", "10", "2026")


def test_make_date():
    assert make_date("8", "3", "2026") == "08/03/2026"
    assert make_date("11", "08", "2026") == "11/08/2026"


def test_duration():
    assert duration(["Madrid", "11/08/2026", "20/08/2026", 4435.25]) == 9
    assert duration(["Helsinki", "24/09/2026", "02/10/2026", 2010.75]) == 8
    assert duration(["Vienna", "28/12/2026", "03/01/2027", 1500.0]) == 6


def test_add_offer():
    test_offers = []
    add_offer(test_offers, "Paris", "5", "6", "2026", "10", "6", "2026", "1500")
    assert len(test_offers) == 1
    assert test_offers[0] == ["Paris", "05/06/2026", "10/06/2026", 1500.0]


def test_modify_price():
    test_offers = get_test_offers()
    modify_price(test_offers, 0, 3000.0)
    assert test_offers[0][3] == 3000.0
    assert test_offers[1][3] == 10215.75


def test_remove_from_destination():
    test_offers = get_test_offers()
    test_offers.append(["Madrid", "01/09/2026", "05/09/2026", 2000.0])
    assert remove_from_destination(test_offers, "Madrid") == 2
    assert len(test_offers) == 4
    assert remove_from_destination(test_offers, "Paris") == 0
    assert len(test_offers) == 4


def test_remove_less_days():
    test_offers = get_test_offers()
    assert remove_less_days(test_offers, 9) == 2      # Athens (6) si Helsinki (8)
    assert len(test_offers) == 3
    assert remove_less_days(test_offers, 1) == 0


def test_remove_greater_price():
    test_offers = get_test_offers()
    assert remove_greater_price(test_offers, 4000.0) == 2   # Madrid si Buenos Aires
    assert test_offers == [
        ["Athens", "13/09/2026", "19/09/2026", 3298.90],
        ["Cairo", "15/08/2026", "25/08/2026", 3925.30],
        ["Helsinki", "24/09/2026", "02/10/2026", 2010.75],
    ]
    assert remove_greater_price(test_offers, 99999.0) == 0


def run_all_tests():
    test_is_valid_date()
    test_date_checker()
    test_make_date()
    test_duration()
    test_add_offer()
    test_modify_price()
    test_remove_from_destination()
    test_remove_less_days()
    test_remove_greater_price()
