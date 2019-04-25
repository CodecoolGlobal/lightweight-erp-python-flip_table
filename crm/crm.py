""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
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
                common.go_back_in_menu()

            elif option == "2":
                table = add(table)
                data_manager.write_table_to_file("crm/customer.csv", table)

            elif option == "3":
                id_to_remove = ui.get_inputs(
                    ["Please enter the ID of the person you wish to remove: "],
                    ""
                )
                if common.check_id_in_table(table, id_to_remove):
                    table = remove(table, id_to_remove)
                    data_manager.write_table_to_file("crm/customers.csv", table)

            elif option == "4":
                id_to_update = ui.get_inputs(
                    ["Please enter the ID of the person you wish to update: "],
                    ""
                )
                if common.check_id_in_table(table, id_to_update):
                    update(table, id_to_update)
                    data_manager.write_table_to_file("crm/customers.csv", table)

            elif option == "5":
                ui.print_result(get_longest_name_id(table), "\nThe ID of the longest name is: ")
                common.go_back_in_menu()
            
            elif option == "6":
                ui.print_result(get_subscribed_emails(table), "")
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

    if common.confirm_option():
            
        ID = 0

        for person in table:
            if person[ID] == id_:
                for person_data_index in range(len(new_data)):
                    person[person_data_index + 1] = new_data[person_data_index]

    return table

def get_longest_name_id(table):
    """
        Question: What is the id of the customer with the longest name?

        Args:
            table (list): data table to work on

        Returns:
            string: id of the longest name (if there are more than one, return
                the last by alphabetical order of the names)
        """

    FIRST_ELEMENT = 0
    ID = 0
    NAME = 1

    lenght_of_names = [len(row[NAME]) for row in table]
    max_len = max(lenght_of_names)
    ppl_data_with_max_len_name = []
    for index, longest_name in enumerate(lenght_of_names):
        if longest_name == max_len:
            ppl_data_with_max_len_name.append(table[index])

    if len(ppl_data_with_max_len_name) == 1:
        return ppl_data_with_max_len_name[ID]

    else:
        return common.alph_sorted_names_reversed(ppl_data_with_max_len_name)[FIRST_ELEMENT][ID]


def get_subscribed_emails(table):
    """
        Question: Which customers has subscribed to the newsletter?

        Args:
            table (list): data table to work on

        Returns:
            list: list of strings (where a string is like "email;name")
        """

    NAME = 1
    EMAIL = 2
    SUBSCRIBTION = 3

    subscribed_people = []

    for people in table:
        if people[SUBSCRIBTION] == "1":
            subscribed_people.append((people[NAME] + ";" + people[EMAIL]))
    
    return subscribed_people

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
