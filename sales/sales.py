""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
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
            if option == "1":           #Print the table
                show_table(table)

            elif option == "2":
                table = add(table)
                data_manager.write_table_to_file("sales/sales.csv", table)

            elif option == "3":
                id_to_remove = ui.get_inputs(
                    ["Please enter the ID of the game you wish to remove: "],
                    ""
                    )
                table = remove(table, id_to_remove)
                data_manager.write_table_to_file("sales/sales.csv", table)

            elif option == "4":
                which_id = ui.get_inputs(
                    ["Please enter the ID of the game you wish to update: "],
                    ""
                )
                update(table, which_id)
                data_manager.write_table_to_file("sales/sales.csv", table)

            elif option == "5":
                lowest_price = get_lowest_price_item_id(table)
                ui.print_result(lowest_price, "The lowest price game ID's are: ")

            elif option == "6":
                #dates = ui.get_inputs(["Month from", "Day from", "Year from", "Month to", ])
            
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

    # your code


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
    TITLE = 0
    PRICE = 1
    MONTH = 2
    DAY = 3
    YEAR = 4


    ID = 0

    for game in table:
        if game[ID] == id_:
            for label in range(len(new_data)):
                game[label + 1] = new_data[label]

    return table


# special functions:
# ------------------

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """

    lowest_price_id = []
    PRICE = 2
    ID = 0
    lowest_id_price = min([price[PRICE] for price in table])

    for game in table:
        if game[PRICE] == lowest_id_price:
            lowest_price_id.append(game[ID])

    return lowest_price_id[0]


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


    

    # your code