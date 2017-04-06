
#Preparação do Script

from sense_hat import SenseHat

sense = SenseHat()

from requests import get
import json
from pprint import pprint
from haversine import haversine

my_lat = 41.1496100	
my_lon = -8.6109900

stations = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'

all_stations = get(stations).json()['items']

#Encontrar a estação mais próxima para obter dados precisos RGB


def find_closest():
    smallest = 20036
    for station in all_stations:
        station_lon = station['weather_stn_long']
        station_lat = station['weather_stn_lat']
        distance = haversine(my_lon, my_lat, station_lon, station_lat)
        if distance < smallest:
            smallest = distance
            closest_station = station['weather_stn_id']
            
    return closest_station
closest_stn = find_closest()
weather = weather + str(closest_stn)
my_weather = get(weather).json()['items']


#WINDSPEED 3
wind_speed = my_weather[0]['wind_speed']

#HUMIDITY 4
humidity = my_weather[0]['humidity']

#RAINFALL 5
rainfall = my_weather[0]['rainfall']

#AIRPRESSURE 6
air_pressure = my_weather[0]['air_pressure']

#GROUNDTEMP 1
ground_temp = my_weather[0]['ground_temp']

#AMBIENTTEMP 2
ambient_temp = my_weather[0]['ambient_temp']

i=0

def move_left (event):
    if event.action=='pressed':
        global i
        i = i-1
        print(i)
        print(event)

def move_right (event):
    if event.action=='pressed':
        global i
        i = i+1
        print(i)
        print(event)

sense.stick.direction_right = move_right
sense.stick.direction_left = move_left




        #nao esquecer zero e -1

while True:

    
    while i==0:
        sense.show_message(str(ground_temp))

    while i==1:
        sense.show_message(str(ambient_temp))
        
    while i==2:
        sense.show_message(str(wind_speed))

    while i==3:
        sense.show_message(str(humidity))

    while i==4:
        sense.show_message(str(rainfall))

    while i==5:
        sense.show_message(str(air_pressure))
        

    
   
        

       
    
        
