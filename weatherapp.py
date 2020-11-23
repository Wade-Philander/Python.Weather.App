#Wade Philander
import requests
from tkinter import *
from tkinter import messagebox as mb
import pyowm
from pyowm import *
from datetime import *


window = Tk()
window.title("Weather App")
window.geometry('550x350')
window.configure(bg='red')



def Check_Weather():

    #city = input(str("Where are you:"))  #user input, wheather of the area they want.
    try:
        city = loc_en.get()

        url = "https://api.openweathermap.org/data/2.5/weather?q="+ city + "&appid=e30a3785da67bd9d83b65bf8933359b5"

        x = requests.get(url)                 # API data
        
        json_data = x.json() 
        print(json_data) 
        weather_data = json_data['weather'][0]['main'] 

    except:
        mb.showerror('Error', 'PLEASE ENTER A REAL CITY')
        pass

    print(x) 

              #WEATHER
    print("Weather:",weather_data)                          # Print only the specified weather
    weather_data_label['text']="Your weather today is: " + weather_data

        #Weather Desciption
    weather_main = json_data['weather'][0]['description']     # getting the weather description from the place user input using json data. 
    print("Description:", weather_main)                       # Print only the specified description
    weather_main_lb['text']="Cloud cover: " + weather_main
    
            #WIND SPEED
    weather_wind = json_data['wind']['speed']                   # Getting the wind speed from json file
    print("Wind speed of:", weather_wind)
    weather_wind_lb['text']="Wind speeds " + str(weather_wind) +"km/h"
    
            #MIN TEMP
    weather_min_temp = json_data['main']['temp_min']                # getting the min. temperature
    conv_min_temp = round(float(weather_min_temp)-273.15,2)         # Convert kelvin to degrees celcius
    print("Minimum Temperature is:", conv_min_temp,"'C")
    weather_min_temp_lb['text']="Minimum temperature is: " + str(conv_min_temp) +"'C"          # displays the text lable of weather_min_temp_lb

        #MAX TEMP
    weather_max_temp = json_data['main']['temp_max']                #does the same as above code but for the maximum temp
    conv_max_temp = round(float(weather_max_temp)-273.15,2)
    print("Maximum Temperature is:", conv_max_temp,"'C")
    weather_max_temp_lb['text']="Maximum temperature is: " + str(conv_max_temp) +"'C"


    if conv_min_temp < 10:
        window.configure(bg='light blue')
    else:
        window.configure(bg='yellow')

    # Getting forecast for the next 5 days as well as weather description.

def sec_win():
    
    root = Tk()
    root.title('5-day weather forcast')
    root.geometry('500x500')

    city = loc_en.get()
    url = "https://api.openweathermap.org/data/2.5/forecast?q="+ city +"&appid=e30a3785da67bd9d83b65bf8933359b5"
    x = requests.get(url)
    print(x)
    
    json_data = x.json()
    print(json_data)

    for a in range(5):
        a1 = json_data['list'][a*8]['main']['temp']
        a2 = round(a1-273,1)
        print(a2)

        c1 = json_data['list'][a*8]['weather'][0]['description']
        print(c1)



    a2_label= Label(root)
    a2_label.grid(row=0, column=2)

    c1_label= Label(root)
    c1_label.grid(row=1, column=2)

    root.mainloop()

#************************************************************************************************************************************************************

#                                                                Tkinter widgets

loc_en = Entry(window)
loc_en.place( x=200, y=20)

loc_en_label = Label(window, text='Where are you: ')
loc_en_label.place( x=25, y=20)
loc_en_label.config(bg='white', fg='blue', font="Times 17")

btn = Button(window, text='Check Your Weather', command=Check_Weather)
btn.place( x=100, y=60)


weather_data_label = Label(window, text='Weather Condition')
weather_data_label.place( x=175, y=100)
weather_data_label.config(bg='white', fg='blue', font="Times 17")

weather_main_lb = Label(window, text='Weather description')
weather_main_lb.place( x=175, y=150)
weather_main_lb.config(bg='white', fg='blue', font="Times 17")

weather_wind_lb = Label(window, text='Wind Condition')
weather_wind_lb.place( x=175, y=200)
weather_wind_lb.config(bg='white', fg='blue', font="Times 17")

weather_min_temp_lb = Label(window, text='Minimum Temperature')
weather_min_temp_lb.place( x=175, y=250)
weather_min_temp_lb.config(bg='white', fg='blue', font="Times 17")

weather_max_temp_lb = Label(window, text='Maximum Temperature')
weather_max_temp_lb.place( x=175, y=300)
weather_max_temp_lb.config(bg='white', fg='blue', font="Times 17")


#*******************************************************************************************************************************************


#*******************************************************************************************************************************************

#                                     ******** SECOND WINDOW *******
sec_win_btn = Button(window, text='Check your 5-day forcast', command=sec_win)
sec_win_btn.place( x=300, y=60)  


window.mainloop()