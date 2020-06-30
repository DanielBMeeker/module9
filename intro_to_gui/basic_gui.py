"""
Program: basic_gui.py
Author: Daniel Meeker
Date: 6/30/2020

This program creates a basic GUI that allows the user
to select between 4 different meals.
"""
import tkinter


def pick_breakfast():
    """
    This function changes the label to reflect
    the user selecting breakfast. It also unchecks
    all the other check boxes.
    """
    label.config(text="Mmmmm, bacon.")
    var2.set(0)
    var3.set(0)
    var4.set(0)


def pick_second_breakfast():
    """
    This function changes the label to reflect
    the user selecting second breakfast. It also
    unchecks all the other check boxes.
    """
    label.config(text="Brunch!")
    var1.set(0)
    var3.set(0)
    var4.set(0)


def pick_lunch():
    """
    This function changes the label to reflect
    the user selecting lunch. It also unchecks
    all the other check boxes.
    """
    label.config(text="I <3 Food")
    var1.set(0)
    var2.set(0)
    var4.set(0)


def pick_dinner():
    """
    This function changes the label to reflect
    the user selecting dinner. It also unchecks
    all the other check boxes.
    """
    label.config(text="Winner Winner Chicken Dinner!")
    var1.set(0)
    var2.set(0)
    var3.set(0)


m = tkinter.Tk()
'''
widgets
'''
m.title('Favorite Meal')
label = tkinter.Label(m, text="Waiting")
label.grid(row=5)
var1 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Breakfast", variable=var1, command=pick_breakfast).grid(row=1)
var2 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Second Breakfast", variable=var2, command=pick_second_breakfast).grid(row=2)
var3 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Lunch", variable=var3, command=pick_lunch).grid(row=3)
var4 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Dinner", variable=var4, command=pick_dinner).grid(row=4)
exit_button = tkinter.Button(m, text='Exit', width=25, command=m.destroy)
exit_button.grid(row=6)
'''
end of widgets
'''

m.mainloop()
