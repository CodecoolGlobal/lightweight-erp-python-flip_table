""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
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
    table = data_manager.get_table_from_file("store/games.csv")

    options = [
        "Show table",
        "Add item",
        "Remove item",
        "Update item",
        "Games per manufacturer",
        "Average stock by manufacturer"]

    while True:
        ui.print_menu("- Store manager -", options, "Back to Main menu")
        option = ui.get_inputs(["Please enter a number: "], "")

        try:
            if option == "1":
                show_table(table) 
                common.go_back_in_menu()

            elif option == "2":
                table = add(table) 
                data_manager.write_table_to_file("store/games.csv", table)

            elif option == "3":
                id_to_remove = ui.get_inputs(
                    ["Please enter the ID of the title you wish to remove: "], ""
                )
                if common.check_id_in_table(table, id_to_remove):
                    table = remove(table, id_to_remove)
                    data_manager.write_table_to_file("store/games.csv", table)

            elif option == "4":
                id_to_update = ui.get_inputs(
                    ["Please enter the ID of the title you wish to update: "],
                    ""
                )
                if common.check_id_in_table(table, id_to_update): 
                    update(table, id_to_update)
                    data_manager.write_table_to_file("store/games.csv", table)

            elif option == "5":
                count_by_manufacturer = get_counts_by_manufacturers(table)
                ui.print_result(count_by_manufacturer, ["MANUFACTURER", "GAMES"])
                common.go_back_in_menu()
                
            elif option == "6":
                which_manuf = ui.get_inputs(
                    ["Please enter which manufacturer: "],
                    ""
                )
                try:
                    average_stock_by_manufacturer = get_average_by_manufacturer(table, which_manuf)
                except ZeroDivisionError:
                    continue

                ui.print_result(average_stock_by_manufacturer,"The avarege stock by the manufacturer is ")
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
    ui.print_table(table, ["ID", "TITLE", "MANUFACTURER", "PRICE", "IN-STOCK"])


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    input_for_new_row = ui.get_inputs(
        ["Title", "Manufacturer", "Price", "In-stock"],
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
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    new_data = ui.get_inputs(
        ["Title", "Manufacturer", "Price", "In-stock"],
        "Please enter the new data to update"
    )

    if common.confirm_option():
        ID = 0

        for game in table:
            if game[ID] == id_:
                for data_index in range(len(new_data)):
                    game[data_index + 1] = new_data[data_index]




    return table



def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """

    count_by_manufacturer = {}
    MANUFACTURER = 2
    for game in table:
        if game[MANUFACTURER] not in count_by_manufacturer.keys():
            count_by_manufacturer[game[MANUFACTURER]] = 1
        else:
            count_by_manufacturer[game[MANUFACTURER]] += 1

    return count_by_manufacturer



def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """
    MANUFACTURER = 2
    STOCK = 4
    games_by_manuf = 0
    stock_by_manuf = 0

    for game in table:
        if game[MANUFACTURER] == manufacturer:
            games_by_manuf += 1
            stock_by_manuf += int(game[STOCK])

    return stock_by_manuf / games_by_manuf
    
