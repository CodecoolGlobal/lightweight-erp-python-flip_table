""" User Interface (UI) module """
import common

def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    print("\x1b[2J\x1b[H",end="")
    table.insert(0, title_list)
    max_length_of_titles = row_max_length(table)
    for table_row in table:
        for i in range(len(table[0])):
            print(table_row[i].center(max_length_of_titles[i]+2,' '),end="|")
        print("\n")  
    del table[0]


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    
    if type(result) == dict:
        print("\x1b[2J\x1b[H",end="")
        print("")
        max_length_value = max([max([len(value) for value in str(result.values())]),len(label[1])])
        max_length_key = max([len(key) for key in result.keys()])
        print("|",label[0].center(max_length_key," "),"|",label[1].center(max_length_value," "),"|")
        for i in result.items():
            print("|",str(i[0]).center(max_length_key," "),'|',str(i[1]).center(max_length_value," "),"|")

    elif type(result) == int or type(result) == float:
        print("")
        print(label, result)
    
    elif type(result) == list:
        try:
            print("")
            print(label)
            for elements in result:
                print("\n" + elements)
        except IndexError:
            print("\x1b[2J\x1b[H",end="")
            print("\n", label, "\n")
            for names in result:
                print("\n", "-", names)

    elif type(result) == str:
        print(label)
        print("")
        print(result)

def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    
    print("\x1b[2J\x1b[H",end="")
    max_lenght = max([len(menu_option) for menu_option in list_options]) + 4
    main_menu_decor_lenght = int((max_lenght - len(title)))
    print("")
    print("\n" + title.center(max_lenght, "-") + "\n")
    for number, option in enumerate(list_options, 1):
        print(f"({number}) {option}")
    print("")
    print("(0)",exit_message,"\n")


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """

    inputs = []

    if title == "":
        return input(list_labels[0])
    else:
        print(title)
        for label in list_labels:
            inputs.append(input(label+": "))

    return inputs


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    print(message)


def row_max_length(table):
    AN_ELEMENT = 0
    max_world_len = []
    for title in range(len(table[AN_ELEMENT])):
        max_world_len.append(max([len(element[title]) for element in table]))
    return max_world_len