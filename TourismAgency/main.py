from printers import print_offers, print_numbered_offers, offers_in_interval, destination_lower_price, offers_end_date,print_averagep_destination,count_offers_per_destination,print_from_substring,print_two_best_offers

from DateCheckers import is_valid_date, date_checker, make_date, duration

from AddModify import add_offer, modify_price

from Removing import remove_from_destination, remove_greater_price, remove_less_days

from Tests import test_add_offer, test_remove_greater_price, test_remove_less_days, test_date_checker, test_duration, \
    test_is_valid_date, test_make_date, test_modify_price, test_remove_from_destination, get_test_offers, run_all_tests
from menus import options_menu, main_menu

run_all_tests()

offers = []
add_offer(offers, "Madrid", "11", "8", "2026", "20", "8", "2026", "4435.25")
add_offer(offers, "Buenos Aires", "6", "3", "2026", "21", "3", "2026", "10215.75")
add_offer(offers, "Athens", "13", "9", "2026", "19", "9", "2026", "3298.90")
add_offer(offers, "Cairo", "15", "8", "2026", "25", "8", "2026", "3925.30")
add_offer(offers, "Helsinki", "24", "9", "2026", "2", "10", "2026", "2010.75")

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

    elif option in ("1", "2", "3", "4"):
        options_menu(option)
        print()
        selection = input("Please enter your selection: ").strip()

        if selection == "e":
            continue
        elif option == "1" and selection == "a":

            destination = input("Please enter the destination: ").strip()
            day = (input("Please enter the start day: "))
            month = (input("Please enter the start month: "))
            year = (input("Please enter the start year: "))

            day1 = input("Please enter the end day: ")
            month1 = input("Please enter the end month: ")
            year1 = input("Please enter the end year: ")
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

        elif option == "3" and selection == "a":
            day = input("Please enter the start day: ").strip()
            month = input("Please enter the start month: ").strip()
            year = input("Please enter the start year: ").strip()
            day1 = input("Please enter the end day: ").strip()
            month1 = input("Please enter the end month: ").strip()
            year1 = input("Please enter the end year: ").strip()

            if date_checker(day, month, year, day1, month1, year1):
                result = offers_in_interval(offers, day, month, year, day1, month1, year1)
                if len(result) == 0:
                    print("No offers in this interval.")
                else:
                    print_offers(result)
            else:
                print("Invalid dates.")

        elif option == "3" and selection == "b":
            destination = input("Please enter the destination: ").strip()
            price = input("Please enter the price: ").strip()
            try:
                result = destination_lower_price(offers, destination, float(price))
                if len(result) == 0:
                    print("No offers found for " + destination + " with a lower price than " + price + ".")
                else:
                    print_offers(result)
            except ValueError:
                print("Invalid price.")

        elif option == "3" and selection == "c":
            day1 = input("Please enter the end day: ").strip()
            month1 = input("Please enter the end month: ").strip()
            year1 = input("Please enter the end year: ").strip()
            if is_valid_date(day1, month1, year1):
                result = offers_end_date(offers, day1, month1, year1)
                if len(result) == 0:
                    print("No offers ending on " + make_date(day1, month1, year1) + ".")
                else:
                    print_offers(result)
            else:
                print("Invalid date.")
        elif option == "4" and selection == "a":
            destination = input("Please enter the destination: ").strip()
            price=print_averagep_destination(offers, destination)
            print("Average price: " + str(price))

        elif option == "4" and selection == "b":
            result = count_offers_per_destination(offers)
            if len(result) == 0:
                print("There are no offers.")
            else:
                for pair in result:
                    print(pair[0] + ": " + str(pair[1]) + " offer(s)")

        elif option == "4" and selection == "c":
            substring = input("Please enter the substring: ").strip()
            result=print_from_substring(offers,substring)
            if len(result) == 0:
                print("There are no offers containing the " + substring + " substring.")
            else:
                print_offers(result)

        elif option == "4" and selection == "d":
            day = input("Please enter the start day: ").strip()
            month = input("Please enter the start month: ").strip()
            year = input("Please enter the start year: ").strip()

            day1 = input("Please enter the end day: ").strip()
            month1 = input("Please enter the end month: ").strip()
            year1 = input("Please enter the end year: ").strip()

            result=print_two_best_offers(offers, day, month, year1, day1, month1, year1)
            if len(result)<2:
                print("There are not at least 2 offers.")
            else:
                print_offers(result)
    elif option == "5":
        print("Filtering is not implemented yet.")

    elif option == "6":
        print("Undo is not implemented yet.")

    else:
        print("Invalid option.")
