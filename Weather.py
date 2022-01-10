import requests
from datetime import datetime 
import time

user_api = "" #add ur own api dont wanna disclose mine

location = input("Enter your city u wanna look about : ")

api_link = f"https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api

linkk = requests.get(api_link)
api_data = linkk.json()

if api_data ['cod'] == '404':
    print(f"Check city name! {location}")
else:

    temprature = ((api_data['main']['temp'])- 273.15)
    description = api_data['weather'][0]['description']
    windspeed = api_data['wind']['speed']
    date_time = datetime.now()
    print("____________________________________________________")
    print (f"Weather stats for {location}  ||  {date_time}")
    print("____________________________________________________")

    
    print(f"Current temp : {temprature}")
    print(f"Current description : {description}")
    print(f"Current windspeed : {windspeed} kmph")

    time.sleep(10)
