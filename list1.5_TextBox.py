#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter as tk
import ttk

window = tk.Tk()
window.title('TextBox')
window.wm_resizable(0, 0)
def click_me():
    btn.configure(text='Hello ' + name.get())
lbl = ttk.Label(window, text="Enter your name:")
lbl.grid(column=0, row=0)
btn = ttk.Button(window, text="Click me!", command=click_me)
btn.grid(column=1, row=1)
name = tk.StringVar()
name_entered = ttk.Entry(window, width=3, textvariable=name)
name_entered.grid(column=0, row=1)

window.mainloop()