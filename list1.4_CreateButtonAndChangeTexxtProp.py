#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter as tk
import ttk

window = tk.Tk()
window.title("First Python GUI Demo")
lable = ttk.Label(window, text="This is a label.")
lable.grid(column=0, row=0)

# Button Click Function
def click_me():
    action.configure(text="I have been clicked!")
    lable.configure(foreground='red')

# Adding a button
action = ttk.Button(window, text='Click Me', command=click_me)
action.grid(column=1, row=1)

window.mainloop()
