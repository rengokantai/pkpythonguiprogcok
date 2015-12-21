__author__ = 'Hernan Y.Ke'
import tkinter as tk
from tkinter import ttk
win = tk.Tk()
tabControl = ttk.Notebook(win)
tab1 = ttk.Frame(tabControl)

tabControl.add(tab1,text="aaaaa")
tabControl.pack(expand=1,fill="both")
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2,text="bbbbbb")

fm = ttk.Labelframe(tab1,text="frame")
fm.grid(column=1,row=1)
ttk.Label(fm,text="test").grid(column=1,row=0)
win.mainloop()