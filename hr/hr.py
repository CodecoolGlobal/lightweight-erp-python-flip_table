""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
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

    table = data_manager.get_table_from_file("hr/persons.csv")

    options = [
        "Show table",
        "Add item",
        "Remove item",
        "Update item",
        "Oldest poeple",
        "People closest to birth year avg."
    ]

    while True:
        ui.print_menu("Human resources manager", options, "Back to main menu")
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
                data_manager.write_table_to_file("hr/persons.csv", table)

            elif option == "3":
                id_to_remove = ui.get_inputs(
                    ["Please enter the ID of the person you wish to remove: "],
                    ""
                    )
                table = remove(table, id_to_remove)
                data_manager.write_table_to_file("hr/persons.csv", table)

            elif option == "4":
                which_id = ui.get_inputs(
                    ["Please enter the ID of the person you wish to update: "],
                    ""
                )
                update(table, which_id)
                data_manager.write_table_to_file("hr/persons.csv", table)

            elif option == "5":
                oldest_people = get_oldest_person(table)
                ui.print_result(oldest_people, "The oldest people are: ")
                common.go_back_in_menu()

            elif option == "6":
                closes_person_avg = get_persons_closest_to_average(table)
                ui.print_result(closes_person_avg, "The people born closest to the average are: ")
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
        ["ID", "NAME", "BIRTH YEAR"]
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
        ["Name", "Birth year"],
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
        ["Name", "Birth year"],
        "Please enter the new data to update"
    )
    NAME = 0
    BIRTH_YEAR = 1

    ID = 0

    for person in table:
        if person[ID] == id_:
            for label in range(len(new_data)):
                person[label + 1] = new_data[label]

    return table


# special functions:
# ------------------

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """

    oldest_people = []
    YEAR = 2
    NAME = 1
    oldest_birthyear = min([year[YEAR] for year in table])

    for person in table:
        if person[YEAR] == oldest_birthyear:
            oldest_people.append(person[NAME])
    
    return oldest_people

    # your code


def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """
    YEAR = 2
    NAME = 1
    sum_of_years = 0
    distance_to_zero = []
    list_of_people = []

    for year in [birth_year[YEAR] for birth_year in table]:
        sum_of_years += int(year)

    average = int(sum_of_years / len([year[YEAR] for year in table]))

    for year in [birth_year[YEAR] for birth_year in table]:
        distance_to_zero.append(abs((average - int(year))))

    for number, number_to_zero in enumerate(distance_to_zero):
        if number_to_zero == min(distance_to_zero):
            list_of_people.append(table[number][NAME])

    return list_of_people
    

    # your code
