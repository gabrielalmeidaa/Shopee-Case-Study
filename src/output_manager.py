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
            print("Input seller is not one of the five allowed sellers. " \
                  "Please, input a valid seller name.")
        if 'item_value' in exception.errors.keys():
            print("Item value is invalid. Make sure to not input negative numbers " \
                  "and to use '.' as the separator for decimal numbers.")
        else:
            print(exception.errors)

    @staticmethod
    def clear_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def print_input_error_message(option):
        print("'{}' is an invalid input option. "
              "Please, input one of the allowed option values.".format(option))