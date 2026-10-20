def main_menu():
    """
        Prints the main menu of the application.
        :return: -
    """

    print("0. Show all vacation offers.")
    print("1. Add and modify an offer.")
    print("2. Remove an offers.")
    print("3. Display offers with specific properties.")
    print("4. Reports.")
    print("5. Filtering.")
    print("6. Undo.")
    print("7. Exit.")


def options_menu(option):
    """
       Prints the sub-menu for the chosen option from the main menu.
       :param option: the option chosen by the user in the main menu (str, "1" - "5")
       :return: -
    """
    if option == "1":
        print("a). Add a vacation offer.")
        print("b). Modify a vacation offer(price).")
        print("e). Exit.")
    elif option == "2":
        print("a). Delete all available offers for a given destination.")
        print("b). Remove all available offers that have a shorter duration than a given number of days.")
        print("c). Remove all available offers for which the price is greater than a given price. ")
        print("e). Exit.")
    elif option == "3":
        print("a). Print all offers which take place in a given interval of time.")
        print("b). Print all offers with a given destination having a price smaller than a given price.")
        print("c). Print all offers with a given end date.")
        print("e). Exit.")
    elif option == "4":
        print("a). Print the average price of offers for a given destination.")
        print("b). Print the number of offers available for each destination.")
        print("c). Print the offers for which the destination string contains a given substring.")
        print("d). Print the two best offers for a given interval in terms of price.")
        print("e). Exit.")
    elif option == "5":
        print("a). Eliminate offers that have as destination a given place.")
        print("b). Eliminate offers for which the price is greater than a given price, and the number of days the offer spans is smaller than a given number of days.")
        print("e). Exit.")
    elif option == "6":
        pass
    elif option == "7":
        main_menu()

offers = [
    ["Madrid", "11/08/2026", "20/08/2026", 4435.25],
    ["Buenos Aires", "06/03/2026", "21/03/2026", 10215.75],
    ["Athens", "13/09/2026", "19/09/2026", 3298.90],
    ["Cairo", "15/08/2026", "25/08/2026", 3925.30],
    ["Helsinki", "24/09/2026", "02/10/2026", 2010.75],
]

###   Printing function
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


###

### Date checking/forming functions

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
    """
    before = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    d1, m1, y1 = offer[1].split("/")
    d2, m2, y2 = offer[2].split("/")
    start = int(y1) * 365 + before[int(m1) - 1] + int(d1)
    end = int(y2) * 365 + before[int(m2) - 1] + int(d2)
    return end - start

###


### Adding/Modifying functions


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

###


### Removing functions

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

###




### Tests

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


run_all_tests()







while True:
    print()
    main_menu()
    print()
    option = input("Please enter your option: ").strip()
    print()

    if option == "7":
        print("Bye!")
        break
    elif option == "0":
        print_offers(offers)

    elif option in ("1", "2"):
        options_menu(option)
        print()
        selection = input("Please enter your selection: ").strip()

        if selection == "e":
            continue
        elif option == "1" and selection == "a":

            destination = input("Please enter the destination: ").strip()
            day=(input("Please enter the start day: "))
            month=(input("Please enter the start month: "))
            year=(input("Please enter the start year: "))

            day1=input("Please enter the end day: ")
            month1=input("Please enter the end month: ")
            year1=input("Please enter the end year: ")
            price = input("Please enter the price: ").strip()

            if date_checker(day, month, year, day1, month1, year1):
                add_offer(offers, destination, day, month, year, day1, month1, year1, price)
                print("Offer added successfully.")
            else:
                print("Invalid dates.")

        elif option == "1" and selection == "b":
            print_numbered_offers(offers)
            number = input("Choose the offer number: ").strip()
            price = input("Please enter the new price: ").strip()

            if number.isdigit() and 1 <= int(number) <= len(offers):
                modify_price(offers, int(number) - 1, float(price))
                print("Price modified successfully.")
            else:
                print("Invalid offer number.")


        elif option == "2" and selection == "a":
            destination = input("Please enter the destination: ").strip()
            removed = remove_from_destination(offers, destination)
            if removed == 0:
                print("No offers found for " + destination + ".")
            else:
                print(str(removed) + " offer(s) removed.")


        elif option == "2" and selection == "b":
            days = input("Please enter the number of days: ").strip()
            if days.isdigit():
                removed = remove_less_days(offers, int(days))
                if removed == 0:
                    print("No offers shorter than " + days + " days.")
                else:
                    print(str(removed) + " offer(s) removed.")
            else:
                print("Invalid number of days.")


        elif option == "2" and selection == "c":
            price = input("Please enter the price: ").strip()
            try:
                removed = remove_greater_price(offers, float(price))
                if removed == 0:
                    print("No offers with a price greater than " + price + ".")
                else:
                    print(str(removed) + " offer(s) removed.")
            except ValueError:
                 print("Invalid price.")
    elif option == "3":
        print("Displaying is not implemented yet.")
    elif option == "4":
        print("Reports are not implemented yet.")
    elif option == "5":
        print("Filtering is not implemented yet.")

    elif option == "6":
        print("Undo is not implemented yet.")

    else:
        print("Invalid option.")
