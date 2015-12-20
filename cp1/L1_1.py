__author__ = 'Hernan Y.Ke'
import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title("test")
#win.resizable(0,0) //not resizable
label = ttk.Label(win, text="a")
label.grid(column=0,row=0)

textLabel = tk.StringVar()
name = ttk.Entry(win,widget=12, textvariable=textLabel)
name.grid(column=0,row=3)

def clickMe():
    action.configure(text="clicked")
    label.configure(text="red")




action = ttk.Button(win, text="click",command=clickMe)
action.grid(column=0,row=1)
win.mainloop()
