""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
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

    table = data_manager.get_table_from_file("crm/customers.csv")

    options = [
        "Show table",
        "Add item",
        "Remove item",
        "Update item",
        "ID of the longest name",
        "Customers subscribed to newsletter"
    ]

    while True:
        ui.print_menu("- CRM manager -", options, "Back to Main menu")
        option = ui.get_inputs(["Please enter a number: "], "")

        try:
            if option == "1":
                show_table(table)

            elif option == "2":
                table = add(table)
                data_manager.write_table_to_file("crm/customer.csv", table)

            elif option == "3":
                id_to_remove = ui.get_inputs(
                    ["Please enter the ID of the person you wish to remove: "],
                    ""
                )
                table = remove(table, id_to_remove)
                data_manager.write_table_to_file("crm/customers.csv", table)

            elif option == "4":
                which_id = ui.get_inputs(
                    ["Please enter the ID of the person you wish to update: "],
                    ""
                )
                update(table, which_id)
                data_manager.write_table_to_file("crm/customers.csv", table)
            
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
        ["ID", "NAME", "E-MAIL", "SUBSCRIBED"]
    )


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    input_for_new_row = ui.get_inputs(
        ["Name", "E-mail", "Subscribed"],
        "Please enter the persons details"
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

    for person in table:
        if person[ID] == id_:
            table.remove(person)

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
        ["NAME", "E-MAIL", "SUBSCRIBED"],
        "Please enter the new data to update"
    )

    NAME = 0
    E_MAIL = 1
    SUBSCRIBED = 2

    ID = 0

    for person in table:
        if person[ID] == id_:
            for label in range(len(new_data)):
                person[label + 1] = new_data[label]

    return table


# special functions:
# ------------------

def get_longest_name_id(table):
    """
        Question: What is the id of the customer with the longest name?

        Args:
            table (list): data table to work on

        Returns:
            string: id of the longest name (if there are more than one, return
                the last by alphabetical order of the names)
        """


# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    """
        Question: Which customers has subscribed to the newsletter?

        Args:
            table (list): data table to work on

        Returns:
            list: list of strings (where a string is like "email;name")
        """

    # your code


# functions supports data analyser
# --------------------------------


def get_name_by_id(id):
    """
    Reads the table with the help of the data_manager module.
    Returns the name (str) of the customer with the given id (str) on None om case of non-existing id.

    Args:
        id (str): the id of the customer

    Returns:
        str: the name of the customer
    """

    # your code



def get_name_by_id_from_table(table, id):
    """
    Returns the name (str) of the customer with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the customer table
        id (str): the id of the customer

    Returns:
        str: the name of the customer
    """

    # your code
