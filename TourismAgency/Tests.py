from DateCheckers import is_valid_date, date_checker, make_date, duration

from AddModify import add_offer, modify_price

from Removing import remove_from_destination, remove_greater_price, remove_less_days

from Offers import *
from printers import *


def GetSet_offer():
    o = create_offer("Lyon", "11/10/2026", "23/10/2026", 5689.76)

    assert get_destination(o) == "Lyon"
    assert not get_destination(o) == "Madrid"

    assert get_start(o) == "11/10/2026"
    assert not get_start(o) == "23/10/2026"

    assert get_end(o) == "23/10/2026"
    assert not get_end(o) == "11/10/2026"

    assert get_price(o) == 5689.76
    assert not get_price(o) == 9999.0

    o2 = create_offer("Rome", "01/07/2026", "05/07/2026", 900.0)
    assert get_id(o2) == get_id(o) + 1
    assert not get_id(o2) == get_id(o)

    set_destination(o, "Madrid")
    assert get_destination(o) == "Madrid"
    assert not get_destination(o) == "Lyon"

    set_start(o, "11/09/2026")
    assert get_start(o) == "11/09/2026"
    assert not get_start(o) == "11/10/2026"

    set_end(o, "20/09/2026")
    assert get_end(o) == "20/09/2026"
    assert not get_end(o) == "23/10/2026"

    set_price(o, 6001.10)
    assert get_price(o) == 6001.10
    assert not get_price(o) == 5689.76


def get_test_offers():
    """
    Builds a new list of offers using add_offer, used in tests.
    """
    test_offers = []

    add_offer(test_offers, "Madrid", "11", "8", "2026", "20", "8", "2026", "4435.25")
    add_offer(test_offers, "Buenos Aires", "6", "3", "2026", "21", "3", "2026", "10215.75")
    add_offer(test_offers, "Athens", "13", "9", "2026", "19", "9", "2026", "3298.90")
    add_offer(test_offers, "Cairo", "15", "8", "2026", "25", "8", "2026", "3925.30")
    add_offer(test_offers, "Helsinki", "24", "9", "2026", "2", "10", "2026", "2010.75")
    return test_offers


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
    assert duration(create_offer("Madrid", "11/08/2026", "20/08/2026", 4435.25)) == 9
    assert duration(create_offer("Helsinki", "24/09/2026", "02/10/2026", 2010.75)) == 8
    assert duration(create_offer("Vienna", "28/12/2026", "03/01/2027", 1500.0)) == 6


def test_add_offer():
    test_offers = []

    add_offer(test_offers, "Paris", "5", "6", "2026", "10", "6", "2026", "1500")
    assert len(test_offers) == 1
    assert get_destination(test_offers[0]) == "Paris"
    assert get_start(test_offers[0]) == "05/06/2026"
    assert get_end(test_offers[0]) == "10/06/2026"
    assert get_price(test_offers[0]) == 1500.0


def test_modify_price():
    test_offers = get_test_offers()
    modify_price(test_offers, 0, 3000.0)
    assert get_price(test_offers[0]) == 3000.0
    assert get_price(test_offers[1]) == 10215.75


def test_remove_from_destination():
    test_offers = get_test_offers()
    add_offer(test_offers, "Madrid", "1", "9", "2026", "5", "9", "2026", "2000")
    assert remove_from_destination(test_offers, "Madrid") == 2
    assert len(test_offers) == 4
    assert remove_from_destination(test_offers, "Paris") == 0
    assert len(test_offers) == 4


def test_remove_less_days():
    test_offers = get_test_offers()
    assert remove_less_days(test_offers, 9) == 2
    assert len(test_offers) == 3
    assert remove_less_days(test_offers, 1) == 0


def test_remove_greater_price():
    test_offers = get_test_offers()
    assert remove_greater_price(test_offers, 4000.0) == 2
    assert [get_destination(o) for o in test_offers] == ["Athens", "Cairo", "Helsinki"]
    assert remove_greater_price(test_offers, 99999.0) == 0





def test_offers_in_interval():
    test_offers = get_test_offers()
    result = offers_in_interval(test_offers, "1", "8", "2026", "31", "8", "2026")
    assert [get_destination(o) for o in result] == ["Madrid", "Cairo"]
    assert not len(result) == 5
    assert offers_in_interval(test_offers, "1", "1", "2025", "31", "1", "2025") == []


def test_destination_lower_price():
    test_offers = get_test_offers()
    add_offer(test_offers, "Madrid", "1", "9", "2026", "5", "9", "2026", "2000")
    result = destination_lower_price(test_offers, "Madrid", 3000.0)
    assert len(result) == 1
    assert get_price(result[0]) == 2000.0
    assert not len(result) == 2
    assert destination_lower_price(test_offers, "Madrid", 1000.0) == []
    assert destination_lower_price(test_offers, "Paris", 99999.0) == []


def test_offers_end_date():
    test_offers = get_test_offers()
    result = offers_end_date(test_offers, "25", "8", "2026")
    assert [get_destination(o) for o in result] == ["Cairo"]
    assert not len(result) == 3
    assert offers_end_date(test_offers, "1", "1", "2026") == []


def test_count_offers_per_destination():
    test_offers = get_test_offers()
    add_offer(test_offers, "Madrid", "1", "9", "2026", "5", "9", "2026", "2000")
    result = count_offers_per_destination(test_offers)
    assert result == [["Madrid", 2], ["Buenos Aires", 1], ["Athens", 1], ["Cairo", 1], ["Helsinki", 1]]
    assert not result[0] == ["Madrid", 1]
    assert count_offers_per_destination([]) == []


def test_offers_with_substring():
    test_offers = get_test_offers()
    result = print_from_substring(test_offers, "a")
    assert [get_destination(o) for o in result] == ["Cairo", "Madrid"]
    assert not [get_destination(o) for o in result] == ["Madrid", "Cairo"]
    assert print_from_substring(test_offers, "xyz") == []


def test_two_best_offers():
    test_offers = get_test_offers()
    result = print_two_best_offers(test_offers, "1", "8", "2026", "31", "10", "2026")
    assert [get_destination(o) for o in result] == ["Helsinki", "Athens"]
    assert not len(result) == 4
    assert print_two_best_offers(test_offers, "1", "1", "2025", "31", "1", "2025") == []


def run_all_tests():
    GetSet_offer()
    test_is_valid_date()
    test_date_checker()
    test_make_date()
    test_duration()
    test_add_offer()
    test_modify_price()
    test_remove_from_destination()
    test_remove_less_days()
    test_remove_greater_price()
    test_offers_in_interval()
    test_destination_lower_price()
    test_offers_end_date()
    test_count_offers_per_destination()
    test_offers_with_substring()
    test_two_best_offers()
