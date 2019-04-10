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
    
    while True:
        generated = ''
        generated += random_letter()
        generated += random_letter().upper()
        generated += random_two_number()
        generated += random_letter().upper()
        generated += random_letter()
        generated += random_spec_char()
        if generated not in [table_row[0] for table_row in table]:
            break

    return generated

