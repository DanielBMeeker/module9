"""
Program: set_ops.py
Author: Daniel Meeker
Date: 06/29/2020

This program demonstrates packages by having three modules in one package:
a greeting module, a dictionary module, and a set module. This is the
set module which has a function used to print all the elements of a set.
"""


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
