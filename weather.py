from tkinter import *
from tkinter import ttk
import requests

def getdata():
    city=cityName.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=c8db362275e45a573a39773546bff701").json()
    climate1.config(text=data["weather"][0]["main"])
    des1.config(text=data["weather"][0]["description"])
    temp1.config(text=str(int(data["main"]["temp"]-273.15))+" °C")
    pressure1.config(text=str(int(data["main"]["pressure"]))+" mb")

win=Tk()
win.title("Weather")
win.config(bg ="sky blue")
win.geometry("500x570")
win.resizable(False,False)

name=Label(win,text="Weather App",font=("Time New Roman",40,"bold"))
name.place(x=25,y=50,height=50,width=450)
cityName=StringVar()
stateName=[
    "Guwahati",
    "Silchar",
    "Dibrugarh",
    "Jorhat",
    "Nagaon",
    "Tezpur",
    "Tinsukia",
    "Bongaigaon",
    "Dhubri",
    "Diphu",
    "Karimganj",
    "Sivasagar",
    "Goalpara",
    "Barpeta",
    "Duliajan",
    "North Lakhimpur",
    "Hailakandi",
    "Golaghat",
    "Mangaldoi",
    "Nalbari",
    "Kokrajhar",
    "Margherita",
    "Morigaon",
    "Hojai",
    "Biswanath Chariali",
    "Udalguri",
    "Haflong",
    ]

state=ttk.Combobox(win,values=stateName,font=("Time New Roman",20),state="readonly",textvariable=cityName)
state.set("Select a city")
state.place(x=25,y=120,height=50,width=450)
done=Button(win,text="Done",font=("Time New Roman",20,"bold"),command=getdata)
done.place(x=200,y=190,height=50,width=100)

climate=Label(win,text="Climate",font=("Time New Roman",10,"bold"))
climate.place(x=25,y=260,height=50,width=210)
climate1=Label(win,text="",font=("Time New Roman",10,"bold"))
climate1.place(x=250,y=260,height=50,width=210)

des=Label(win,text="Description",font=("Time New Roman",10,"bold"))
des.place(x=25,y=330,height=50,width=210)
des1=Label(win,text="",font=("Time New Roman",10,"bold"))
des1.place(x=250,y=330,height=50,width=210)

temp=Label(win,text="Temperature",font=("Time New Roman",10,"bold"))
temp.place(x=25,y=400,height=50,width=210)
temp1=Label(win,text="",font=("Time New Roman",10,"bold"))
temp1.place(x=250,y=400,height=50,width=210)

pressure=Label(win,text="Pressure",font=("Time New Roman",10,"bold"))
pressure.place(x=25,y=470,height=50,width=210)
pressure1=Label(win,text="",font=("Time New Roman",10,"bold"))
pressure1.place(x=250,y=470,height=50,width=210)

win.mainloop()