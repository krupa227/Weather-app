from tkinter import *
from tkinter import ttk
import requests #to run the url , intract with the browser, #configration change

def data_get():
    City = city_name.get() #data get for the city_name which we can want to search
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+City+"&appid=aaa8502a4090f22aa21cc8d665e6f4e2").json()
    w_label1.config(text=data["weather"][0]["main"]) #index num 0 dis thats why put 0#get info to the data, want info about wether make a disctionry
    wb_label2.config(text=data["weather"][0]["description"])
    temp_label3.config(text=str(int(data["main"]["temp"]-273.15))) #convert temp kelvin to celsuis
    per_label4.config(text=data["main"]["pressure"])


#combo box which include the information and list of country and city
win = Tk() #make a window for app
win.title("WeatherTech Pro")
win.config(bg="blue") #used for background color change
win.geometry("500x570") #for big pixel

name_label = Label(win,text = "WeatherTech Pro",font=("Time New Roman",30,"bold")) #for app name
name_label.place(x=25,y=50,height=50,width=450) #x and y for app name box

city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

com = ttk.Combobox(win,text = "WeatherTech Pro",values=list_name,font=("Time New Roman",20,"bold"),textvariable=city_name)#for state name list
#make a varabile to get a city name which we can search for the wether
com.place(x=25,y=120,height=50,width=450)

w_label = Label(win,text = "Weather Climate",font=("Time New Roman",17)) #for wether list
w_label.place(x=25,y=260,height=50,width=210) #

w_label1 = Label(win,text = "",font=("Time New Roman",17))
w_label1.place(x=250,y=260,height=50,width=210) #for the result

wb_label = Label(win,text = "Weather Description",font=("Time New Roman",17)) #for wether list
wb_label.place(x=25,y=330,height=50,width=210)

wb_label2 = Label(win,text= "",font=("Time New Roman",17))
wb_label2.place(x=250,y=330,height=50,width=210) #for the result

temp_label = Label(win,text="Temperature",font=("Time New Roman",17)) #for wether list
temp_label.place(x=25,y=400,height=50,width=210)

temp_label3 = Label(win,text = "",font=("Time New Roman",17)) #for wether list
temp_label3.place(x=250,y=400,height=50,width=210)

per_label = Label(win,text = "Pressure",font=("Time New Roman",17)) #for wether list
per_label.place(x=25,y=470,height=50,width=210)

per_label4 = Label(win,text = "",font=("Time New Roman",17)) #for wether list
per_label4.place(x=250,y=470,height=50,width=210)

done_button = Button(win,text = "Done",font=("Time New Roman",20,"bold"),command=data_get)#with the help of command we call the function
done_button.place(y=190,height=50,width=100,x=200)

win.mainloop() #loop for app
