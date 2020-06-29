"""
Program: my_definitions.py
Author: Daniel Meeker
Date: 6/29/2020

This program defines a module with 4 functions in it
then imports the module into the testing file and calls
the functions.
"""


def welcome(name):
    """
    This function is used to print a greeting
    :param name: Name that is being welcomed
    :return: a string greeting the name
    """
    return "Hello, " + name + "\n"


def author():
    """
    This function is used to print the Author of the program
    :return: string declaring who the author is
    """
    return "Author of this program is Daniel Meeker\n"


def print_dict(a_dict):
    """
    This function prints all the key value pairs in a dictionary
    :param a_dict: the dictionary to be printed
    :return: a string that prints each key value pair on a new line
    """
    return_string = ''
    for key, value in a_dict.items():
        return_string += "{} == {}\n".format(key, value)
    return return_string


def print_set(a_set):
    """
    This function prints all the elements of a set
    :param a_set: a set that is passed in
    :return: a string with all the values - one on each line
    """
    return_string = ''
    for x in a_set:
        return_string += str(x) + '\n'
    return return_string
