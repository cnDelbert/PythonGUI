#!/usr/bin/env python
# -*- coding: utf-8 -*-
# It is Tkinter, but not tkinter.
import Tkinter as tk

win = tk.Tk()

win.title("Python GUI")
# resizable is the alias of wm_resizable
# Only `0' could prevent resize.
win.wm_resizable(0, 0)
win.mainloop()
