import tkinter


def pick_cis():
    label.config(text="Nice choice")
    var2.set(0)


def pick_bis():
    label.config(text="Are you sure?")
    var1.set(0)


m = tkinter.Tk()
'''
widgets
'''
m.title('Major Decision')
label = tkinter.Label(m, text="No Selection Made")
label.grid(row=4)
var1 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="CIS", variable=var1, command=pick_cis).grid(row=0)
var2 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="BIS", variable=var2, command=pick_bis).grid(row=1)
exit_button = tkinter.Button(m, text='Exit', width=25, command=m.destroy)
exit_button.grid(row=5)
'''
end of widgets
'''

m.mainloop()
