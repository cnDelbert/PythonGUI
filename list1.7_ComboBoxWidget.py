#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter as tk
import ttk

window = tk.Tk()
window.title("Focus to a widget")
window.wm_resizable(0, 0)

def click_me():
    btn.configure(text="Hello " + name.get() + num_ent.get())
    btn.config(state='disabled')

lbl = ttk.Label(window, text="Enter your name:")
num_lbl = ttk.Label(window, text="Enter a number:")
btn = ttk.Button(window, text="click me!", command=click_me)

name = tk.StringVar()
name_ent = ttk.Entry(window, width=12, textvariable=name)

num = tk.StringVar()
# num_ent = ttk.Combobox(window, width=12, textvariable=num)
num_ent = ttk.Combobox(window, width=12, textvariable=num, state='readonly')
num_ent['values'] = [1, 2, 3, 4, 5, 10, 100]
num_ent.current(6)

lbl.grid(column=0, row=0)
num_lbl.grid(column=1, row=1)
name_ent.grid(column=0, row=1)
num_ent.grid(column=1, row=1)
btn.grid(column=2, row=1)

name_ent.focus()

window.mainloop()