import requests

from datetime import datetime

api_key = "54660e15089486d929f5f518e14b0f0e"
location = input("Enter City Name: ")

compleate_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(compleate_api_link)
api_data = api_link.json()


temp_city=((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_TIME = datetime.now().strftime("%d %b %y ! %I:%M:%S %p")

print("--------------------------------------------------------------------")
print("Weather Stats for = {}".format(location.upper(), date_TIME))
print("--------------------------------------------------------------------")

print("Current Temprature is: {:.2f} deg C".format(temp_city))
print("Current weather desc :",weather_desc)
print("Current Humidity     :",hmdt,'%')
print("Currnet wind speed   :",wind_spd,'kmph')



def save():
    file = open('data.txt','w')
    file.write("Current Temprature is: {:.2f} deg C".format(temp_city))
    file.write("Current weather desc :",weather_desc)
    file.write("Current Humidity     :",hmdt,'%')
    file.write("Currnet wind speed   :",wind_spd,'kmph')

    file.close()
    save()
