import sys

import mongoengine
import os

mongoengine.connect('shopee-case-study-database',
                    host='127.0.0.1', port=27017)

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def allowed_options():
    return ['1', '2', '3']

def display_user_options():
    print("\nWelcome to the Sales Management App. What would you like to do?\n")
    print("1. Input Sale Item")
    print("2. Check Sales Ranking")
    print("3. Quit")


def register_sale_item():
    raise Exception(NotImplementedError)


def display_ranking():
    raise Exception(NotImplementedError)


def execute_option(option):
    if option not in allowed_options():
        print("'{}' is an invalid input option. "
              "Please, input one of the allowed option values.".format(option))
        return

    if option == '1':
        register_sale_item()
        display_ranking()
    elif option == '2':
        display_ranking()
    elif option == '3':
        sys.exit(os.EX_OK)


if __name__ == "__main__":
    while True:
        display_user_options()
        user_input = input("\nSelect your option: ")
        execute_option(user_input)
