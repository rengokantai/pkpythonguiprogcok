__author__ = 'Hernan Y.Ke'
__author__ = 'Hernan Y.Ke'
import tkinter as tk
from tkinter import ttk,scrolledtext

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
combobox = ttk.Combobox(win,width=12, textvariable=number,state='readonly') # belongs to ttk
combobox['values']=(1,2,3,4)
combobox.grid(column=0,row=4)
combobox.current(0)

chvar1 = tk.IntVar()
chkbox1 = tk.Checkbutton(win,text="disabled",variable=chvar1,state="disabled") # checkbox belongs to tk
chkbox1.select()
chkbox1.grid(column=0,row=5)


action = ttk.Button(win, text="click",command=clickMe)
action.grid(column=0,row=1)

#radio
radVar = tk.IntVar()
def radCall():
    radCol =radVar.get()
    if radCol == 1: win.configure(background="red")
    elif radCol == 2: win.configure(background="blue")

radio1 = tk.Radiobutton(win, text="option1",variable=radVar,value=1,command=radCall)
radio1.grid(column=0,row=6)
radio2 = tk.Radiobutton(win, text="option2",variable=radVar,value=2,command=radCall)
radio2.grid(column=1,row=6)

scr = scrolledtext.ScrolledText(win,width=10,height=20,wrap=tk.WORD)
scr.grid(column=0,columnspan=3)

labelFrame = ttk.LabelFrame(win, text='Frame')
labelFrame.grid(column=0,row=8,padx=20,pady=40)
ttk.Label(labelFrame,text="1").grid(column=0,row=0)
ttk.Label(labelFrame,text="2").grid(column=1,row=0)
win.mainloop()
