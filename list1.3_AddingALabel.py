#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter as tk
import ttk

window = tk.Tk()
window.title("First Python GUI Demo")
window.wm_resizable(0, 0)
ttk.Label(window, text="This is a label.").grid(column=0, row=0)
window.mainloop()
