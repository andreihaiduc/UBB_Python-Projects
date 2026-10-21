from menus import main_menu, options_menu

offers = [
    ["Madrid", "11/08/2026", "20/08/2026", 4435.25],
    ["Buenos Aires", "06/03/2026", "21/03/2026", 10215.75],
    ["Athens", "13/09/2026", "19/09/2026", 3298.90],
    ["Cairo", "15/08/2026", "25/08/2026", 3925.30],
    ["Helsinki", "24/09/2026", "02/10/2026", 2010.75],
]

from printers import print_offers, print_numbered_offers

from DateCheckers import is_valid_date, date_checker, make_date, duration

from AddModify import add_offer, modify_price

from Removing import remove_from_destination, remove_greater_price, remove_less_days

from Tests import test_add_offer, test_remove_greater_price, test_remove_less_days,test_date_checker,test_duration,test_is_valid_date,test_make_date,test_modify_price,test_remove_from_destination,get_test_offers,run_all_tests

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
