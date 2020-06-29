"""
Program: test_my_definitions.py
Author: Daniel Meeker
Date: 6/29/2020

This program defines a module with 4 functions in it
then imports the module into the testing file and calls
the functions.
"""
from module1 import my_definitions as md

student = {
    "name": "Daniel",
    "year": 2,
    "major": "BIS-OOP"
}

classes = ("Javascript", "Python", "Data Structures")

if __name__ == '__main__':
    print(md.welcome('Joe'))
    print(md.author())
    print(md.print_dict(student))
    print(md.print_set(classes))
