#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter as tk
import ttk

window = tk.Tk()
window.title("Focus to a widget")
window.wm_resizable(0, 0)

def click_me():
    btn.configure(text="Hello " + name.get())
    btn.config(state='disabled')

lbl = ttk.Label(window, text="Enter your name:")
btn = ttk.Button(window, text="click me!", command=click_me)

name = tk.StringVar()
name_ent = ttk.Entry(window, width=12, textvariable=name)

lbl.grid(column=0, row=0)
name_ent.grid(column=0, row=1)
btn.grid(column=1, row=1)

name_ent.focus()

window.mainloop()