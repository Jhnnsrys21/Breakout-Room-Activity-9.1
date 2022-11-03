from tkinter import *
from tkinter import messagebox
import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "9nul8nQElewdmRWvNpRyyLDGBGpVL8Qd"

def submit():
    location=entry1.get()
    destination=entry2.get()

    url = main_api + urllib.parse.urlencode({"key": key, "from":location, "to":destination})
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        ml1 = Label(root,text="API Status: " + str(json_status) + " = A successful route call.\n").place(x=20,y=160)
        ml2 = Label(root,text="Directions from " + (location + " to " + (destination))).place(x=20,y=200)
        ml3 = Label(root,text="Time Duration: " + (json_data["route"]["formattedTime"])).place(x=20,y=240)
        ml4 = Label(root,text="Distance: " + str("{:.2f}".format((json_data["route"]["distance"])*1.61))).place(x=20,y=280)
            
    else:
        messagebox.showinfo("","Unknown Information!")
    

# def route():
#     lbl = Label(root,text="Alternative Route")

root=Tk()
root.title("Mapquest")
root.geometry("500x500")


global entry1
global entry2

Label(root,text="Location").place(x=20,y=20)
Label(root,text="Destination").place(x=20,y=60)

entry1=Entry(root,bd=1)
entry1.place(x=150,y=20)

entry2=Entry(root,bd=1)
entry2.place(x=150,y=60)

Button(root,text="Submit",command=submit,height=1,width=10,bd=5).place(x=150,y=100)

#Button(root,text="Alternative Route",command=route,height=1,width=12,bd=5).place(x=150,y=240)

root.mainloop()
