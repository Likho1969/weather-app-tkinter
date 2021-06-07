from tkinter import *
import tkinter as tk
import requests
import tkinter.messagebox
from datetime import datetime
# import tinker as a whole and after import tkinter as tk
# added tkinter.message box for error handling display message
# adding functionality to the app

root = Tk()

# configure app title and dimensions and background colour
root.title("Global Weather App")
root.configure(bg="RoyalBlue4")
root.geometry("1000x800")


'''start our fields and labels which will be displaying
the data'''
# title labels
title_1 = Label(text="Global Weather App", width=20, font=("bold", 30), bg="black", fg="white")

current_date = Label(text=datetime.now().date(), width=20, font=("bold", "30"), bg="SteelBlue1")
current_date.place(x=400, y=400)


title_2 = Label(text="Enter City name ", width=32, font=("italics", 15), bg="SkyBlue3")

search_city = Entry(text="Search for city")

# Search field and button in grid format
city_name = StringVar()
search_city = tk.Entry(textvariable=city_name, text="Search for city")


def search_weather():
    api_key = "5738dfc6e8c227f5125072b505c2c4c8"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    city_names = search_city.get()
    complete_url = base_url + "appid=" + api_key + "&q=" + city_names

    # response

    response = requests.get(complete_url)
    x = response.json()

    try:
        if['cod'] != '400':
            y = x['main']
            temp_High = round(y['temp_max'] - 273.15)
            temp_Low = round(y['temp_min'] - 273.15)
            pressure_value = y['pressure']
            hum_value = y['humidity']

        z = x['weather']
        description_weather = z[0]['description']

        m = x['sys']
        country_detail = m['country']

        temp_high_rs.configure(text=temp_High)
        temp_low_rs.configure(text=temp_Low)
        pres_rs.configure(text=pressure_value)
        hum_rs.configure(text=hum_value)
        des_rs.configure(text=description_weather)
        coun_rs.configure(text=country_detail)

    except:   # if there errors this will be executed
        tkinter.messagebox.showinfo("Error", "City not found")


button_search = tk.Button(text="Search", bg="green3", command=search_weather)

# function for closing app via menu


def close_app():
    closeapp = tkinter.messagebox.askyesno("Global Weather App", "Do you really want to exit Global Weather App?")
    if closeapp > 0:
        root.destroy()
        return

# additional function for displaying credits in menu


def credits_func():
    credits_func = tkinter.messagebox.showinfo(title="Credits", message='Made with love by Developer Likho Kapesi')
    return


# tkinter gui formatting

# menu bars

menubar = Menu(root)
root.configure(menu=menubar)
submenu1 = Menu(menubar)
submenu2 = Menu(menubar)
menubar.add_cascade(label="File", menu=submenu1)
menubar.add_cascade(label="Help", menu=submenu2)

submenu1.add_command(label="Exit", command=close_app)
submenu2.add_command(label="About", command=credits_func)

# temperature output and label
temp_high = Label(text="Temp(high) :", width=20, font=("bold", 20), bg="SkyBlue3")
temp_high_rs = Label(text="", width=20, font=("bold", 20), bg="DarkOliveGreen3")

temp_low = Label(text="Temp(low) :", width=20, font=("bold", 20), bg="SkyBlue3")
temp_low_rs = Label(text="", width=20, font=("bold", 20), bg="DarkOliveGreen3")

# pressure label and fetched data
pres = Label(text="Pressure :", width=20, font=("bold", 20), bg="SkyBlue3")
pres_rs = Label(text="", width=20, font=("bold", 20), bg="DarkOliveGreen3")

# humidity label and data
hum = Label(text="Humidity :", width=20, font=("bold", 20), bg="SkyBlue3")
hum_rs = Label(text="", width=20, font=("bold", 20), bg="DarkOliveGreen3")

# description
desc = Label(text="Description :", width=20, font=("bold", 20), bg="SkyBlue3")
des_rs = Label(text="", width=20, font=("bold", 20), bg="DarkOliveGreen3")

# country
coun = Label(text="Country :", width=20, font=("bold", 20), bg="SkyBlue3")
coun_rs = Label(text="", width=20, font=("bold", 20), bg="DarkOliveGreen3")

footer_1 = Label(text="Temperature is measured in Degrees Celsius", bg="SkyBlue3")
footer_2 = Label(text="Pressure in Pascals (Pa)", bg="SkyBlue3")
footer_3 = Label(text="Humidity is measured in grams Per Kilogram of air(g/Kg)", bg="SkyBlue3")

# the grid lay out
title_1.grid(row=0, column=2)
current_date.grid(row=0, column=3)
title_2.grid(row=2, column=2)
search_city.grid(row=3, column=2)
button_search.grid(row=3, column=3)
temp_high.grid(row=4, column=2)
temp_high_rs.grid(row=4, column=3)
temp_low.grid(row=5, column=2)
temp_low_rs.grid(row=5, column=3)
pres.grid(row=6, column=2)
pres_rs.grid(row=6, column=3)
hum.grid(row=7, column=2)
hum_rs.grid(row=7, column=3)
desc.grid(row=8, column=2)
des_rs.grid(row=8, column=3)
coun.grid(row=9, column=2)
coun_rs.grid(row=9, column=3)
footer_1.grid(row=10, column=2)
footer_2.grid(row=11, column=2)
footer_3.grid(row=12, column=2)


# start the app and make the app run until its closed
root.mainloop()
