import os
import sys

from models.sale_register import SaleRegister
from models.sales_ranking import SalesRanking
from mongoengine import ValidationError
from output_manager import OutputManager

from settings import setup_mongodb_connection


setup_mongodb_connection()


def allowed_options():
    return ['1', '2', '3']


def register_sale_item():
    OutputManager.clear_terminal()
    print("Please input the requested Sale Item information:")
    sale_item_data = get_input_for_sale_item_data()
    try:
        sale_item = SaleRegister.register_sale(**sale_item_data)
        sale_item.save()
        OutputManager.print_sale_register_success_message()
    except ValidationError as e:
        OutputManager.print_readable_error_message(e)


def get_input_for_sale_item_data():
    seller_name = input("Seller's Name: ")
    customer_name = input("Customer's Name: ")
    item_name = input("Item's Name: ")
    item_value = input("Item's Value (please input decimal values with '.'): ")
    return dict(seller_name=seller_name, customer_name=customer_name,
                item_name=item_name, item_value=item_value)


def display_ranking():
    ranking = SalesRanking.build_ranking()
    OutputManager.display_ranking(ranking)


def execute_option(option):
    if option not in allowed_options():
        OutputManager.print_input_error_message(option)
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
        OutputManager.display_user_options()
        user_input = input("\nSelect your option: ")
        execute_option(user_input)
