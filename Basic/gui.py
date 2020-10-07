# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 11:39:06 2020

@author: ST16
"""

from tkinter import *

master = Tk()
var = DoubleVar()
w = Scale(master,variable = var, from_=0, to=20, orient=HORIZONTAL)
w.pack()
label = Label(var)
label.pack()

mainloop()