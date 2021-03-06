import os


class OutputManager:

    @staticmethod
    def display_user_options():
        print("\nWelcome to the Sales Management App. What would you like to do?\n")
        print("1. Input Sale Item")
        print("2. Check Sales Ranking")
        print("3. Quit")

    @staticmethod
    def print_readable_error_message(exception):
        if 'seller_name' in exception.errors.keys():
            print("\nInput seller is not one of the five allowed sellers. " \
                  "Please, input a valid seller name.")
        if 'value' in exception.errors.keys():
            print("\nItem value is invalid. Make sure to not input negative numbers " \
                  "and to use '.' as the separator for decimal numbers.")
        else:
            print(exception.errors)

    @staticmethod
    def clear_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def print_input_error_messythage(option):
        print("'{}' is an invalid input option. "
              "Please, input one of the allowed option values.".format(option))

    @staticmethod
    def print_sale_register_success_message():
        print("Sale Item registered successfully!")

    @staticmethod
    def display_ranking(ranking):
        print("\nRanking sales amount for every registered item: \n")
        for index, item in enumerate(ranking.keys()):
            print("\n===== Item #{} - {} =====\n".format(index + 1, item.title()))
            for placement, record in enumerate(ranking.get(item)):
                print("#{}: {}, with the total of ${}".format(
                    placement + 1, record.get("_id").title(),
                    record.get("salesTotal")))
        input("\nPress any key to continue.")

    @staticmethod
    def print_input_error_message(option):
        print("'{}' is an invalid input option. "
              "Please, input one of the allowed option values.".format(option))
