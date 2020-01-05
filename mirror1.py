import Tkinter as tk
import os
import time as tm
import requests, json 

def display_time():
	current_time = tm.strftime('%H:%M:%S')
	clock_label['text'] = current_time
	root.after(1000,display_time)

def get_weather(url):
  response = requests.get(complete_url) 
  x = response.json() 
  if x["cod"] != "404": 

      y = x["main"] 
      current_temperature = y["temp"] 
      max_temp = y["temp_max"]
      min_temp = y["temp_min"]
      current_pressure = y["pressure"] 
  
      current_humidiy = y["humidity"] 
  
      z = x["weather"] 
  
      weather_description = z[0]["description"] 
  
      weather_str= (str(weather_description) + "\nTemperature = " +
                    str(current_temperature - 273.15) + 
                    "\nMax Temperature = " +
                    str(max_temp- 273.15)  +
                    "\nMin Temperature = " +
                    str(min_temp- 273.15)  +
          "\nHumidity = " +
                    str(current_humidiy) )
  
  else:
      weather_str = " City Not Found "
  return weather_str

api_key = "dfd6047ba35a44fac0012a4e46f1bed5"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = "Berlin" 
complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
weather = get_weather(complete_url)

root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(background = "black")
clock_label = tk.Label(root,font = 'courier 50', bg = 'black', fg = 'white')
clock_label.grid(row = 0, column = 0, padx= 100,pady = 100)
display_time()
weather_label = tk.Label(root,font = 'courier 30', bg = 'black', fg = 'white',text = get_weather(complete_url))
weather_label.grid(row = 1, column = 0, padx= 100,pady = 200)
root.mainloop()
