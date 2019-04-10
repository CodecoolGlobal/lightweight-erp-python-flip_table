""" Common module
implement commonly used functions here
"""

import random


def random_two_number():
    number = ""
    for _ in range(2):
        number = number + chr(random.randint(48, 57))
    return number

def random_letter():
    return chr(random.randint(97, 122))

def random_spec_char():
    spec_char = ""
    for _ in range(2):
        spec_char += chr(random.randint(33, 47))
    return spec_char

def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """

    generated = ''

    generated = generated + random_letter()
    generated = generated + random_letter().upper()
    generated = generated + random_two_number()
    generated = generated + random_letter().upper()
    generated = generated + random_letter()

    return generated

#Counting rows max characters for dynamic table printing

def row_max_length(table):
    max_world_len = []
    for title in range(len(table[0])):
        max_world_len.append(max([len(i[title]) for i in table]))
    return max_world_len