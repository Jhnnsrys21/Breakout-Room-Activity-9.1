from tkinter import *
from tkinter import messagebox
from mapquest_enhance import *

root1 = Tk()
root1.title('Login')
root1.geometry("400x250")

def submit():
    root2()

Button(root1,text="Submit",command=submit,height=1,width=10,bd=5).place(x=20,y=180)


root1.mainloop()