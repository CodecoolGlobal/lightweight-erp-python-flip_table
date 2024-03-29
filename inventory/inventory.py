""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
"""

import ui
import data_manager
import common


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    table = data_manager.get_table_from_file("inventory/inventory.csv")

    options = [
        "Show table",
        "Add item",
        "Remove item",
        "Update item",
        "Available items",
        "Average durability by manufacturer"
    ]

    while True:
        ui.print_menu("Inventory manager", options, "Back to Main menu")
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
                data_manager.write_table_to_file("inventory/inventory.csv", table)
            
            elif option == "3":
                id_to_remove = ui.get_inputs(
                    ["Please enter the ID of the title you wish to remove: "],
                    ""
                )
                if common.check_id_in_table(table, id_to_remove):    
                    table = remove(table, id_to_remove)
                    data_manager.write_table_to_file("inventory/inventory.csv", table)

            elif option == "4":
                id_to_update = ui.get_inputs(
                    ["Please enter the Id of the item you wish to update: "],
                    ""
                )
                if common.check_id_in_table(table, id_to_update):
                    update(table, id_to_update)
                    data_manager.write_table_to_file("inventory/inventory.csv", table)

            elif option == "5":
                ui.print_result(get_available_items(table), "The available items are: ")
                common.go_back_in_menu()
            
            elif option == "6":
                ui.print_result(get_average_durability_by_manufacturers(table), ["MANUFACTURER", "AVG. DURABILITY"])
                common.go_back_in_menu()

            elif option == "0":
                break

            else:
                raise KeyError("Theres no such option")
            
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

    ui.print_table(table, ["ID", "NAME", "MANUFACTURER", "PURCHASE YEAR", "DURBILITY"])


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    input_for_new_row = ui.get_inputs(
    ["Name", "Manufacturer", "Year of purchase", "Durability"],
    "Please enter product details: "
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
        ["NAME", "MANUFACTURER", "YEAR OF PURCHASE", "DURABILITY"],
        "Please enter the new data to update: "
    )

    if common.confirm_option():

        ID = 0

        for item in table:
            if item[ID] == id_:
                for item_data_index in range(len(new_data)):
                    item[item_data_index + 1] = new_data[item_data_index]

    return table


def get_available_items(table):
    """
    Question: Which items have not exceeded their durability yet?

    Args:
        table (list): data table to work on

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """

    not_exceeded_items = []
    NAME = 1
    P_YEAR = 3
    DURABILITY = 4

    for item in table:
        if int(item[P_YEAR]) + int(item[DURABILITY]) >= 2019:
            not_exceeded_items.append(item)

    return not_exceeded_items



def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """

    MANUFACTURER = 2
    DURABILITY = 4
    count_by_manuf = {}
    sum_by_manuf = {}
    avg_durab_by_manuf = {}

    for item in table:
        if item[MANUFACTURER] not in count_by_manuf:
            count_by_manuf[item[MANUFACTURER]] = 1
            sum_by_manuf[item[MANUFACTURER]] = int(item[DURABILITY])

        else:
            count_by_manuf[item[MANUFACTURER]] += 1
            sum_by_manuf[item[MANUFACTURER]] += int(item[DURABILITY])

    for manufacturer in count_by_manuf:
        avg_durab_by_manuf[manufacturer] = (sum_by_manuf.get(manufacturer) / count_by_manuf.get(manufacturer))
        

    return avg_durab_by_manuf


