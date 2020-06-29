"""
Program: greeting.py
Author: Daniel Meeker
Date: 06/29/2020

This program demonstrates packages by having three modules in one package:
a greeting module, a dictionary module, and a set module. This is the
greeting module which has a function used to print a welcome statement
to the user and a function used to print the author of the program.
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
