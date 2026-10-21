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
