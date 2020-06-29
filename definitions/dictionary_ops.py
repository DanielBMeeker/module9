"""
Program: dictionary_ops.py
Author: Daniel Meeker
Date: 06/29/2020

This program demonstrates packages by having three modules in one package:
a greeting module, a dictionary module, and a set module. This is the
dictionary module which has a function used to print all the key value
pairs in a dictionary.
"""


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
