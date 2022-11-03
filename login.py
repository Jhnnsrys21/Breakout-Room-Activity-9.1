from tkinter import *
from tkinter import messagebox
from mapquest_enhance import *


root1=Tk()
root1.title("Login")
root1.geometry("400x250")

def submit():
    username=uname.get()
    password=psswd.get()

    if (username == "" and password == ""):
        messagebox.showinfo("","Input Information!")
    else:
        mapq()
    
global uname
global psswd

Label(root1,text="Enter Username:", font=("Courier New", 20)).place(x=20,y=20)
Label(root1,text="Enter Password:", font=("Courier New", 20)).place(x=20,y=100)

uname=Entry(root1,bd=1)
uname.place(x=20,y=60)

psswd=Entry(root1,show='*', bd=1)
psswd.place(x=20,y=140)

Button(root1,text="Submit",command=submit,height=1,width=10,bd=5).place(x=20,y=180)


root1.mainloop()