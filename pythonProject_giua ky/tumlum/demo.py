import tkinter
from tkinter import *
from tkinter import messagebox

top = Tk()
top.title("Demo")
top.geometry("500x500")
def click():
    messagebox.showinfo( "Button clicked")
# c = Button(top, text="Green", command=click, activeforeground="green", activebackground="orange", pady=10)
# d = Button(top, text="red", activeforeground="yellow", command=click, activebackground="orange", pady=10)
submitbtn = Button(top, text="Submit", activebackground="red", command= click, activeforeground="blue").place(x=30, y=170)
# c.pack(side=TOP)
# d.pack(side=BOTTOM)
name = Label(top, bg='green', text="Name").place(x=30, y=50)

email = Label(top,bg='red', text="Email").place(x=30, y=90)

password = Label(top,bg='yellow', text="Password").place(x=30, y=130)

# submitbtn = Button(top, text="Submit", activebackground="red", activeforeground="blue").place(x=30, y=170)

entry1 = Entry(top).place(x=95, y=50)

entry2 = Entry(top).place(x=95, y=90)

entry3 = Entry(top).place(x=95, y=130)



top.mainloop()