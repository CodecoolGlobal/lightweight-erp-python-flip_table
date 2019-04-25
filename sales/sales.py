""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
    * customer_id (string): id from the crm
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    table = data_manager.get_table_from_file("sales/sales.csv")

    options = [
        "Show table",
        "Add item",
        "Remove item",
        "Update item",
        "Lowest price item ID",
        "Items ID sold between two given dates."]
    # your code


    while True:
        ui.print_menu("Sales manager", options, "Back to main menu")
        option = ui.get_inputs(
            ["Please enter a number: "],
            ""
        )

        try:
            if option == "1":
                show_table(table)
                common.go_back_in_menu()

            elif option == "2":
                table = add(table)
                data_manager.write_table_to_file("sales/sales.csv", table)

            elif option == "3":
                id_to_remove = ui.get_inputs(
                    ["Please enter the ID of the game you wish to remove: "],
                    ""
                    )
                if common.check_id_in_table(table, id_to_remove):
                    table = remove(table, id_to_remove)
                    data_manager.write_table_to_file("sales/sales.csv", table)

            elif option == "4":
                id_to_update = ui.get_inputs(
                    ["Please enter the ID of the game you wish to update: "],
                    ""
                )
                if common.check_id_in_table(table, id_to_update):
                    update(table, id_to_update)
                    data_manager.write_table_to_file("sales/sales.csv", table)

            elif option == "5":
                lowest_price = get_lowest_price_item_id(table)
                ui.print_result(lowest_price, "The lowest price games ID is: ")
                common.go_back_in_menu()

            elif option == "6":
                dates = ui.get_inputs(["Month from", "Day from", "Year from", "Month to", "Day to", "Year to"], "Please enter the dates: ")
                month_from = dates[0]
                day_from = dates[1]
                year_from = dates[2]
                month_to = dates[3]
                day_to = dates[4]
                year_to = dates[5]
                ui.print_result(get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to), ["ID", "TITLE", "PRICE", "MONTH", "DAY", "YEAR"])
                common.go_back_in_menu()
                
            elif option == "0":
                break
            
            else:
                raise KeyError("There is no such option")
        
        except KeyError as err:
            ui.print_error_message(str(err))


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    ui.print_table(
        table,
        ["ID", "TITLE", "PRICE", "MONTH", "DAY", "YEAR"])


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    input_for_new_row = ui.get_inputs(
        ["TITLE", "PRICE", "MONTH", "DAY", "YEAR"],
        "Please enter product details"
    )
    input_for_new_row.insert(0, common.generate_random(table))
    if common.confirm_option():
        table.append(input_for_new_row)

    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    if common.confirm_option():
        ID = 0

        for game in table:
            if game[ID] == id_:
                table.remove(game)

    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    new_data = ui.get_inputs(
        ["TITLE", "PRICE", "MONTH", "DAY", "YEAR"],
        "Please enter the new data to update"
    )

    if common.confirm_option():

        ID = 0

        for game in table:
            if game[ID] == id_:
                for game_data_index in range(len(new_data)):
                    game[game_data_index + 1] = new_data[game_data_index]

    return table



def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """

    lowest_price_items_data = []
    PRICE = 2
    ID = 0
    FIRST_ELEMENT = 0
    lowest_price = min([price[PRICE] for price in table])

    for game in table:
        if game[PRICE] == lowest_price:
            lowest_price_items_data.append(game)
        
    if len(lowest_price_items_data) == 1:
       return lowest_price_items_data[FIRST_ELEMENT][ID]

    else:
        return common.alph_sorted_names_reversed(lowest_price_items_data)[FIRST_ELEMENT][ID]
    



def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """

    MONTH = 3
    DAY = 4
    YEAR = 5

    list_of_games = []

    for game in table:
        if int(game[YEAR]) >= int(year_from) and int(game[YEAR]) <= int(year_to):
            list_of_games.append(game)

    for game in table:
        if int(game[MONTH]) < int(month_from) and int(game[YEAR]) == int(year_from):
            list_of_games.remove(game)

        elif int(game[MONTH]) > int(month_to) and int(game[YEAR]) == int(year_to):
            list_of_games.remove(game)

        elif int(game[DAY]) < int(day_from) and int(game[MONTH]) == int(month_from):
            list_of_games.remove(game)

        elif int(game[DAY]) > int(day_to) and int(game[MONTH]) == int(month_to):
            list_of_games.remove(game)
        else:
            pass

    return list_of_games

    

# functions supports data abalyser
# --------------------------------


def get_title_by_id(id):

    """
    Reads the table with the help of the data_manager module.
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        id (str): the id of the item

    Returns:
        str: the title of the item
    """

    # your code


def get_title_by_id_from_table(table, id):

    """
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the sales table
        id (str): the id of the item

    Returns:
        str: the title of the item
    """

    # your code


def get_item_id_sold_last():
    """
    Reads the table with the help of the data_manager module.
    Returns the _id_ of the item that was sold most recently.

    Returns:
        str: the _id_ of the item that was sold most recently.
    """

    # your code


def get_item_id_sold_last_from_table(table):
    """
    Returns the _id_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        str: the _id_ of the item that was sold most recently.
    """

    # your code


def get_item_title_sold_last_from_table(table):
    """
    Returns the _title_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        str: the _title_ of the item that was sold most recently.
    """

    # your code


def get_the_sum_of_prices(item_ids):
    """
    Reads the table of sales with the help of the data_manager module.
    Returns the sum of the prices of the items in the item_ids.

    Args:
        item_ids (list of str): the ids

    Returns:
        number: the sum of the items' prices
    """

    # your code


def get_the_sum_of_prices_from_table(table, item_ids):
    """
    Returns the sum of the prices of the items in the item_ids.

    Args:
        table (list of lists): the sales table
        item_ids (list of str): the ids

    Returns:
        number: the sum of the items' prices
    """

    # your code


def get_customer_id_by_sale_id(sale_id):
    """
    Reads the sales table with the help of the data_manager module.
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.

    Args:
         sale_id (str): sale id to search for
    Returns:
         str: customer_id that belongs to the given sale id
    """

    # your code


def get_customer_id_by_sale_id_from_table(table, sale_id):
    """
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.

    Args:
        table: table to remove a record from
        sale_id (str): sale id to search for
    Returns:
        str: customer_id that belongs to the given sale id
    """

    # your code


def get_all_customer_ids():
    """
    Reads the sales table with the help of the data_manager module.

    Returns:
         set of str: set of customer_ids that are present in the table
    """

    # your code


def get_all_customer_ids_from_table(table):
    """
    Returns a set of customer_ids that are present in the table.

    Args:
        table (list of list): the sales table
    Returns:
         set of str: set of customer_ids that are present in the table
    """

    # your code


def get_all_sales_ids_for_customer_ids():
    """
    Reads the customer-sales association table with the help of the data_manager module.
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)

    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
            all the sales id belong to the given customer_id
    """

    # your code


def get_all_sales_ids_for_customer_ids_form_table(table):
    """
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)
    Args:
        table (list of list): the sales table
    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
         all the sales id belong to the given customer_id
    """

    # your code


def get_num_of_sales_per_customer_ids():
    """
     Reads the customer-sales association table with the help of the data_manager module.
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """

    # your code


def get_num_of_sales_per_customer_ids_from_table(table):
    """
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Args:
        table (list of list): the sales table
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """

    # your code
