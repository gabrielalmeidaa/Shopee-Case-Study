import sys

import mongoengine
import os

from models.sale_item import SaleItem
from mongoengine import ValidationError

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


def readable_error_message(exception):
    if 'seller_name' in exception.errors.keys():
        return "Input seller is not one of the five allowed sellers. " \
               "Please, input a valid seller name."
    if 'item_value' in exception.errors.keys():
        return "Item value is invalid. Make sure to not input negative numbers " \
               "and to use '.' as the separator for decimal numbers."
    else:
        return str(exception.errors)


def register_sale_item():
    clear_terminal()
    print("Please input the requested Sale Item information:")
    sale_item_data = get_input_for_sale_item_data()
    sale_item = SaleItem(**sale_item_data)
    try:
        sale_item.save()
    except ValidationError as e:
        print(readable_error_message(e))


def get_input_for_sale_item_data():
    seller_name = input("Seller's Name: ")
    customer_name = input("Customer's Name: ")
    item_name = input("Item's Name: ")
    item_value = input("Item's Value (please input decimal values with '.'): ")
    return dict(seller_name=seller_name, customer_name=customer_name,
                item_name=item_name, item_value=item_value)


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
