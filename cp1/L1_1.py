__author__ = 'Hernan Y.Ke'
import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title("test")
#win.resizable(0,0) //not resizable
label = ttk.Label(win, text="a")
label.grid(column=0,row=0)

textLabel = tk.StringVar()
name = ttk.Entry(win,width=12, textvariable=textLabel)
name.grid(column=0,row=2)
name.focus()

def clickMe():
    action.configure(text="clicked")
    label.configure(text=name.get())
    action.configure(state="disabled")

number = tk.StringVar()
combobox = ttk.Combobox(win,width=12, textvariable=number,state='readonly')
combobox['values']=(1,2,3,4)
combobox.grid(column=0,row=4)
combobox.current(0)


action = ttk.Button(win, text="click",command=clickMe)
action.grid(column=0,row=1)
win.mainloop()
