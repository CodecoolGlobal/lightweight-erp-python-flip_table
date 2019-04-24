""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
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

    # you code
    table = data_manager.get_table_from_file("accounting/items.csv")

    options = [
        "Show table",
        "Add item",
        "Remove item",
        "Update item",
        "Place Holder 1",
        "Place Holder 2"]

    while True:
        ui.print_menu("- Accounting -", options, "Back to Main menu")
        option = ui.get_inputs(["Please enter a number: "], "")

        try:
            if option == "1":
                show_table(table)
                common.go_back_in_menu()

            elif option == "2":
                table = add(table) 
                data_manager.write_table_to_file("accounting/items.csv", table)

            elif option == "3":
                id_to_remove = ui.get_inputs(
                    ["Please enter the ID of the title you wish to remove: "], ""
                )
                table = remove(table, id_to_remove)
                data_manager.write_table_to_file("accounting/items.csv", table)

            elif option == "4":
                which_id = ui.get_inputs(
                    ["Please enter the ID of the title you wish to update: "],
                    ""
                )
                update(table, which_id)
                data_manager.write_table_to_file("accounting/items.csv", table)

            elif option == "5":
                which_year_max(table)
                common.go_back_in_menu()

            elif option == "6":
                which_year = ui.get_inputs(
                    ["Please enter a year"],
                    ""
                )
                ui.print_result(avg_amount(table, which_year), "The average amount by given year is: ")
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

    ui.print_table(table, ["ID", "DAY", "MONTH", "YEAR", "IN-STOCK","AMOUNT"])

def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    input_for_new_row = ui.get_inputs(
        ["DAY", "MONTH", "YEAR", "In-stock","AMOUNT"],
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

    for item in table:
        if item[ID] == id_:
            table.remove(item)

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
        ["DAY", "MONTH", "YEAR", "In-stock","AMOUNT"],
        "Please enter the new data to update"
    )
    DAY = 0
    MONTH = 1
    YEAR = 2
    IN_STOCK = 3
    AMOUNT = 4

    ID = 0

    for item in table:
        if item[ID] == id_:
            for label in range(len(new_data)):
                item[label + 1] = new_data[label]

    return table


# special functions:
# ------------------

def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number
    """
    YEAR = 3
    IN_OR_OUT = 4
    AMOUNT = 5

    years = set([year[YEAR] for year in table])

    profit_by_year = {}

    for year in years:
        in_amount = 0
        out_amount = 0
        for items in table:
            if items[IN_OR_OUT] == "in" and items[YEAR] == year:
                in_amount += int(items[AMOUNT])
            if items[IN_OR_OUT] == "out" and items[YEAR] == year:
                out_amount += int(items[AMOUNT])
        profit_by_year[(in_amount - out_amount)] = year
        
    return profit_by_year.get(max(profit_by_year))

def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """

    YEAR = 3
    IN_OR_OUT = 4
    AMOUNT = 5

    in_amount = 0
    out_amount = 0

    items_by_year = 0

    for items in table:
        if items[IN_OR_OUT] == "in" and items[YEAR] == year:
            in_amount += int(items[AMOUNT])
        if items[IN_OR_OUT] == "out" and items[YEAR] == year:
            out_amount += int(items[AMOUNT])
        if items[YEAR] == year:
            items_by_year += 1
    
    return (in_amount - out_amount) / items_by_year
    
