  
#Preparacao do Script

from sense_hat import SenseHat

sense = SenseHat()

from requests import get
import json
from pprint import pprint
from haversine import haversine
from datetime import datetime
from time import sleep
import datetime as dt

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





now = datetime.now()
past=now-dt.timedelta(seconds=30)



horas= ('{0}:{1} {2}/{3}/{4}'.format(now.hour, now.minute,now.day, now.month, now.year))
                                    

h = sense.get_humidity()


v =[0,0,0]  #vazio
b =[255, 255, 255] #branco
a=[0,51,102]#azul escuro
c= [0,215,215]#azul claro
y=[215,215,0]#amarelo

l=[255,128,0]#laranja
v=[255,51,51]#vermelho
r=[125,0,0]#vermelho escuro
quinze = [
a,a,a,a,a,a,a,a,
a,a,b,a,b,b,b,a,
a,b,b,a,b,a,a,a,
a,a,b,a,b,b,b,a,
a,a,b,a,a,a,b,a,
a,a,b,a,b,b,b,a,
a,a,a,a,a,a,a,a,
a,a,a,a,a,a,a,a
]


dezasseis = [
a,a,a,a,a,a,a,a,
a,a,b,a,b,b,b,a,
a,b,b,a,b,a,a,a,
a,a,b,a,b,b,b,a,
a,a,b,a,b,a,b,a,
a,a,b,a,b,b,b,a,
a,a,a,a,a,a,a,a,
a,a,a,a,a,a,a,a
]


dezassete = [
a,a,a,a,a,a,a,a,
a,a,b,a,b,b,b,a,
a,b,b,a,a,a,b,a,
a,a,b,a,a,a,b,a,
a,a,b,a,a,a,b,a,
a,a,b,a,a,a,b,a,
a,a,a,a,a,a,a,a,
a,a,a,a,a,a,a,a
]



dezoito = [
a,a,a,a,a,a,a,a,
a,a,b,a,b,b,b,a,
a,b,b,a,b,a,b,a,
a,a,b,a,b,b,b,a,
a,a,b,a,b,a,b,a,
a,a,b,a,b,b,b,a,
a,a,a,a,a,a,a,a,
a,a,a,a,a,a,a,a
]


dezanove = [
a,a,a,a,a,a,a,a,
a,a,b,a,b,b,b,a,
a,b,b,a,b,a,b,a,
a,a,b,a,b,b,b,a,
a,a,b,a,a,a,b,a,
a,a,b,a,b,b,b,a,
a,a,a,a,a,a,a,a,
a,a,a,a,a,a,a,a
]


vinte=[
c,c,c,c,c,c,c,c,
b,b,b,c,b,b,b,c,
c,c,b,c,b,c,b,c,
b,b,b,c,b,c,b,c,
b,c,c,c,b,c,b,c,
b,b,b,c,b,b,b,c,
c,c,c,c,c,c,c,c,
c,c,c,c,c,c,c,c
]


vinte_e_um=[
c,c,c,c,c,c,c,c,
b,b,b,c,c,c,b,c,
c,c,b,c,c,b,b,c,
b,b,b,c,c,c,b,c,
b,c,c,c,c,c,b,c,
b,b,b,c,c,c,b,c,
c,c,c,c,c,c,c,c,
c,c,c,c,c,c,c,c
]
       

vinte_e_dois=[
c,c,c,c,c,c,c,c,
b,b,b,c,b,b,b,c,
c,c,b,c,c,c,b,c,
b,b,b,c,b,b,b,c,
b,c,c,c,b,c,c,c,
b,b,b,c,b,b,b,c,
c,c,c,c,c,c,c,c,
c,c,c,c,c,c,c,c
]
    


vinte_e_tres=[
c,c,c,c,c,c,c,c,
b,b,b,c,b,b,b,c,
c,c,b,c,c,c,b,c,
b,b,b,c,b,b,b,c,
b,c,c,c,c,c,b,c,
b,b,b,c,b,b,b,c,
c,c,c,c,c,c,c,c,
c,c,c,c,c,c,c,c
]
    


vinte_e_quatro=[
c,c,c,c,c,c,c,c,
b,b,b,c,b,c,b,c,
c,c,b,c,b,c,b,c,
b,b,b,c,b,b,b,c,
b,c,c,c,c,c,b,c,
b,b,b,c,c,c,b,c,
c,c,c,c,c,c,c,c,
c,c,c,c,c,c,c,c
]
    


vinte_e_cinco=[
y,y,y,y,y,y,y,y,
b,b,b,y,b,b,b,y,
y,y,b,y,b,y,y,y,
b,b,b,y,b,b,b,y,
b,y,y,y,y,y,b,y,
b,b,b,y,b,b,b,y,
y,y,y,y,y,y,y,y,
y,y,y,y,y,y,y,y
]


vinte_e_seis=[
y,y,y,y,y,y,y,y,
b,b,b,y,b,b,b,y,
y,y,b,y,b,y,y,y,
b,b,b,y,b,b,b,y,
b,y,y,y,b,y,b,y,
b,b,b,y,b,b,b,y,
y,y,y,y,y,y,y,y,
y,y,y,y,y,y,y,y
]





vinte_e_sete=[
y,y,y,y,y,y,y,y,
b,b,b,y,b,b,b,y,
y,y,b,y,y,y,b,y,
b,b,b,y,y,y,b,y,
b,y,y,y,y,y,b,y,
b,b,b,y,y,y,b,y,
y,y,y,y,y,y,y,y,
y,y,y,y,y,y,y,y
]






vinte_e_oito=[
y,y,y,y,y,y,y,y,
b,b,b,y,b,b,b,y,
y,y,b,y,b,y,b,y,
b,b,b,y,b,b,b,y,
b,y,y,y,b,y,b,y,
b,b,b,y,b,b,b,y,
y,y,y,y,y,y,y,y,
y,y,y,y,y,y,y,y
]





vinte_e_nove=[
y,y,y,y,y,y,y,y,
b,b,b,y,b,b,b,y,
y,y,b,y,b,y,b,y,
b,b,b,y,b,b,b,y,
b,y,y,y,y,y,b,y,
b,b,b,y,b,b,b,y,
y,y,y,y,y,y,y,y,
y,y,y,y,y,y,y,y
]


trinta=[
l,l,l,l,l,l,l,l,
b,b,b,l,b,b,b,l,
l,l,b,l,b,l,b,l,
b,b,b,l,b,l,b,l,
l,l,b,l,b,l,b,l,
b,b,b,l,b,b,b,l,
l,l,l,l,l,l,l,l,
l,l,l,l,l,l,l,l
]




trinta_e_um=[
l,l,l,l,l,l,l,l,
b,b,b,l,l,l,b,l,
l,l,b,l,l,b,b,l,
b,b,b,l,l,l,b,l,
l,l,b,l,l,l,b,l,
b,b,b,l,l,l,b,l,
l,l,l,l,l,l,l,l,
l,l,l,l,l,l,l,l
]




trinta_e_dois=[
l,l,l,l,l,l,l,l,
b,b,b,l,b,b,b,l,
l,l,b,l,l,l,b,l,
b,b,b,l,b,b,b,l,
l,l,b,l,b,l,l,l,
b,b,b,l,b,b,b,l,
l,l,l,l,l,l,l,l,
l,l,l,l,l,l,l,l
]



trinta_e_tres=[
l,l,l,l,l,l,l,l,
b,b,b,l,b,b,b,l,
l,l,b,l,l,l,b,l,
b,b,b,l,b,b,b,l,
l,l,b,l,l,l,b,l,
b,b,b,l,b,b,b,l,
l,l,l,l,l,l,l,l,
l,l,l,l,l,l,l,l
]



trinta_e_quatro=[
l,l,l,l,l,l,l,l,
b,b,b,l,b,l,b,l,
l,l,b,l,b,l,b,l,
b,b,b,l,b,b,b,l,
l,l,b,l,l,l,b,l,
b,b,b,l,l,l,b,l,
l,l,l,l,l,l,l,l,
l,l,l,l,l,l,l,l
]




trinta_e_cinco=[
v,v,v,v,v,v,v,v,
b,b,b,v,b,b,b,v,
v,v,b,v,b,v,v,v,
b,b,b,v,b,b,b,v,
v,v,b,v,v,v,b,v,
b,b,b,v,b,b,b,v,
v,v,v,v,v,v,v,v,
v,v,v,v,v,v,v,v
]



trinta_e_seis=[
v,v,v,v,v,v,v,v,
b,b,b,v,b,b,b,v,
v,v,b,v,b,v,v,v,
b,b,b,v,b,b,b,v,
v,v,b,v,b,v,b,v,
b,b,b,v,b,b,b,v,
v,v,v,v,v,v,v,v,
v,v,v,v,v,v,v,v
]



trinta_e_sete=[
v,v,v,v,v,v,v,v,
b,b,b,v,b,b,b,v,
v,v,b,v,v,v,b,v,
b,b,b,v,v,v,b,v,
v,v,b,v,v,v,b,v,
b,b,b,v,v,v,b,v,
v,v,v,v,v,v,v,v,
v,v,v,v,v,v,v,v
]



trinta_e_oito=[
v,v,v,v,v,v,v,v,
b,b,b,v,b,b,b,v,
v,v,b,v,b,v,b,v,
b,b,b,v,b,b,b,v,
v,v,b,v,b,v,b,v,
b,b,b,v,b,b,b,v,
v,v,v,v,v,v,v,v,
v,v,v,v,v,v,v,v
]



trinta_e_nove=[
v,v,v,v,v,v,v,v,
b,b,b,v,b,b,b,v,
v,v,b,v,b,v,b,v,
b,b,b,v,b,b,b,v,
v,v,b,v,v,v,b,v,
b,b,b,v,b,b,b,v,
v,v,v,v,v,v,v,v,
v,v,v,v,v,v,v,v
]


quarenta=[
r,r,r,r,r,r,r,r,
b,r,b,r,b,b,b,r,
b,r,b,r,b,r,b,r,
b,b,b,r,b,r,b,r,
r,r,b,r,b,r,b,r,
r,r,b,r,b,b,b,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r
]


quarenta_e_um=[
r,r,r,r,r,r,r,r,
b,r,b,r,r,r,b,r,
b,r,b,r,r,b,b,r,
b,b,b,r,r,r,b,r,
r,r,b,r,r,r,b,r,
r,r,b,r,r,r,b,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r
]


quarenta_e_dois=[
r,r,r,r,r,r,r,r,
b,r,b,r,b,b,b,r,
b,r,b,r,r,r,b,r,
b,b,b,r,b,b,b,r,
r,r,b,r,b,r,r,r,
r,r,b,r,b,b,b,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r
]


quarenta_e_tres=[
r,r,r,r,r,r,r,r,
b,r,b,r,b,b,b,r,
b,r,b,r,r,r,b,r,
b,b,b,r,b,b,b,r,
r,r,b,r,r,r,b,r,
r,r,b,r,b,b,b,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r
]


quarenta_e_quatro=[
r,r,r,r,r,r,r,r,
b,r,b,r,b,r,b,r,
b,r,b,r,b,r,b,r,
b,b,b,r,b,b,b,r,
r,r,b,r,r,r,b,r,
r,r,b,r,r,r,b,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r
]


quarenta_e_cinco=[
r,r,r,r,r,r,r,r,
b,r,b,r,b,b,b,r,
b,r,b,r,b,r,r,r,
b,b,b,r,b,b,b,r,
r,r,b,r,r,r,b,r,
r,r,b,r,b,b,b,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r
]


#print("temperatura = " + str(temperatura))


        


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




while True:

    if 
    
    if i==-1:
        i=6
    if i==7:
        i=0


    while i==0:
    
        t = ((sense.get_temperature_from_humidity()+sense.get_temperature_from_pressure())/2)
        temperatura=int(round(t,0))

        if temperatura == 15:
                sense.show_message('Temperatura da sala')
                sense.set_pixels(quinze)
        if temperatura == 16:
                sense.show_message('Temperatura da sala')
                sense.set_pixels(dezasseis)
        if temperatura == 17:
                sense.show_message('Temperatura da sala')
                sense.set_pixels(dezassete)
        if temperatura == 18:
                sense.show_message('Temperatura da sala')
                sense.set_pixels(dezoito)
        if temperatura == 19:
                sense.show_message('Temperatura da sala')
                sense.set_pixels(dezanove)
        if temperatura == 20:
                sense.show_message('Temperatura da sala')
                sense.set_pixels(vinte)
        if temperatura == 21:
                sense.show_message('Temperatura da sala')
                sense.set_pixels(vinte_e_um)
        if temperatura == 22:
                sense.show_message('Temperatura da sala')
                sense.set_pixels(vinte_e_dois)
        if temperatura == 23:
                sense.show_message('Temperatura da sala')
                sense.set_pixels(vinte_e_tres)
        if temperatura == 24:
                sense.show_message('Temperatura da sala')
                sense.set_pixels(vinte_e_quatro)
        if temperatura == 25:
                sense.show_message('Temperatura da sala')
                sense.set_pixels(vinte_e_cinco)
        if temperatura == 26:
                sense.show_message('Temperatura da sala')
                sense.set_pixels(vinte_e_seis)
        if temperatura == 27:
                sense.show_message('Temperatura da sala')
                sense.set_pixels(vinte_e_sete)
        if temperatura == 28:
                sense.show_message('Temperatura da sala')
                sense.set_pixels(vinte_e_oito)
        if temperatura == 29:
                sense.show_message('Temperatura da sala')
                sense.set_pixels(vinte_e_nove)
        if temperatura == 30:
                sense.show_message('Temperatura da sala')
                sense.set_pixels(trinta)
        if temperatura == 31:
                sense.show_message('Temperatura da sala')
                sense.set_pixels(trinta_e_um)
        if temperatura == 32:
                sense.show_message('Temperatura da sala')
                sense.set_pixels(trinta_e_dois)
        if temperatura == 33:
                sense.show_message('Temperatura da sala')
                sense.set_pixels(trinta_e_tres)
        if temperatura == 34:
                sense.show_message('Temperatura da sala')
                sense.set_pixels(trinta_e_quatro)
        if temperatura == 35:
                sense.show_message('Temperatura da sala')
                sense.set_pixels(trinta_e_cinco)
        if temperatura == 36:
                sense.show_message('Temperatura da sala')
                sense.set_pixels(trinta_e_seis)
        if temperatura == 37:
                sense.show_message('Temperatura da sala')
                sense.set_pixels(trinta_e_sete)
        if temperatura == 38:
                sense.show_message('Temperatura da sala')
                sense.set_pixels(trinta_e_oito)
        if temperatura == 39:
                sense.show_message('Temperatura da sala')
                sense.set_pixels(trinta_e_nove)
        if temperatura == 40:
                sense.show_message('Temperatura da sala')
                sense.set_pixels(quarenta)
        if temperatura == 41:
                sense.show_message('Temperatura da sala')
                sense.set_pixels(quarenta_e_um)
        if temperatura == 42:
                sense.show_message('Temperatura da sala')
                sense.set_pixels(quarenta_e_dois)
        if temperatura == 43:
                sense.show_message('Temperatura da sala')
                sense.set_pixels(quarenta_e_tres)
        if temperatura == 44:
                sense.show_message('Temperatura da sala')
                sense.set_pixels(quarenta_e_quatro)
        if temperatura == 45:
                sense.show_message('Temperatura da sala')
                sense.set_pixels(quarenta_e_cinco)


        sleep (5)
        sense.clear()
        sense.show_message(str(horas))
        sense.clear()

    
    while i==1:
        #GROUNDTEMP 1
        ground_temp = int(round(my_weather[0]['ground_temp'],0))
        
        if ground_temp== 15:
                sense.show_message('Temperatura do solo')
                sense.set_pixels(quinze)
        if ground_temp== 16:
                sense.show_message('Temperatura do solo')
                sense.set_pixels(dezasseis)
        if ground_temp== 17:
                sense.show_message('Temperatura do solo')
                sense.set_pixels(dezassete)
        if ground_temp== 18:
                sense.show_message('Temperatura do solo')
                sense.set_pixels(dezoito)
        if ground_temp== 19:
                sense.show_message('Temperatura do solo')
                sense.set_pixels(dezanove)
        if ground_temp== 20:
                sense.show_message('Temperatura do solo')
                sense.set_pixels(vinte)
        if ground_temp== 21:
                sense.show_message('Temperatura do solo')
                sense.set_pixels(vinte_e_um)
        if ground_temp== 22:
                sense.show_message('Temperatura do solo')
                sense.set_pixels(vinte_e_dois)
        if ground_temp== 23:
                sense.show_message('Temperatura do solo')
                sense.set_pixels(vinte_e_tres)
        if ground_temp== 24:
                sense.show_message('Temperatura do solo')
                sense.set_pixels(vinte_e_quatro)
        if ground_temp== 25:
                sense.show_message('Temperatura do solo')
                sense.set_pixels(vinte_e_cinco)
        if ground_temp== 26:
                sense.show_message('Temperatura do solo')
                sense.set_pixels(vinte_e_seis)
        if ground_temp== 27:
                sense.show_message('Temperatura do solo')
                sense.set_pixels(vinte_e_sete)
        if ground_temp== 28:
                sense.show_message('Temperatura do solo')
                sense.set_pixels(vinte_e_oito)
        if ground_temp== 29:
                sense.show_message('Temperatura do solo')
                sense.set_pixels(vinte_e_nove)
        if ground_temp== 30:
                sense.show_message('Temperatura do solo')
                sense.set_pixels(trinta)
        if ground_temp== 31:
                sense.show_message('Temperatura do solo')
                sense.set_pixels(trinta_e_um)
        if ground_temp== 32:
                sense.show_message('Temperatura do solo')
                sense.set_pixels(trinta_e_dois)
        if ground_temp== 33:
                sense.show_message('Temperatura do solo')
                sense.set_pixels(trinta_e_tres)
        if ground_temp== 34:
                sense.show_message('Temperatura do solo')
                sense.set_pixels(trinta_e_quatro)
        if ground_temp== 35:
                sense.show_message('Temperatura do solo')
                sense.set_pixels(trinta_e_cinco)
        if ground_temp== 36:
                sense.show_message('Temperatura do solo')
                sense.set_pixels(trinta_e_seis)
        if ground_temp== 37:
                sense.show_message('Temperatura do solo')
                sense.set_pixels(trinta_e_sete)
        if ground_temp== 38:
                sense.show_message('Temperatura do solo')
                sense.set_pixels(trinta_e_oito)
        if ground_temp== 39:
                sense.show_message('Temperatura do solo')
                sense.set_pixels(trinta_e_nove)
        if ground_temp== 40:
                sense.show_message('Temperatura do solo')
                sense.set_pixels(quarenta)
        if ground_temp== 41:
                sense.show_message('Temperatura do solo')
                sense.set_pixels(quarenta_e_um)
        if ground_temp== 42:
                sense.show_message('Temperatura do solo')
                sense.set_pixels(quarenta_e_dois)
        if ground_temp== 43:
                sense.show_message('Temperatura do solo')
                sense.set_pixels(quarenta_e_tres)
        if ground_temp== 44:
                sense.show_message('Temperatura do solo')
                sense.set_pixels(quarenta_e_quatro)
        if ground_temp== 45:
                sense.show_message('Temperatura do solo')
                sense.set_pixels(quarenta_e_cinco)
        sleep (5)
        
   
    while i==2:
        #AMBIENTTEMP 2
        ambient_temp =int(round( my_weather[0]['ambient_temp'],0))

        if ambient_temp== 15:
                sense.show_message('Temperatura ambiente')
                sense.set_pixels(quinze)
        if ambient_temp== 16:
                sense.show_message('Temperatura ambiente')
                sense.set_pixels(dezasseis)
        if ambient_temp== 17:
                sense.show_message('Temperatura ambiente')
                sense.set_pixels(dezassete)
        if ambient_temp== 18:
                sense.show_message('Temperatura ambiente')
                sense.set_pixels(dezoito)
        if ambient_temp== 19:
                sense.show_message('Temperatura ambiente')
                sense.set_pixels(dezanove)
        if ambient_temp== 20:
                sense.show_message('Temperatura ambiente')
                sense.set_pixels(vinte)
        if ambient_temp== 21:
                sense.show_message('Temperatura ambiente')
                sense.set_pixels(vinte_e_um)
        if ambient_temp== 22:
                sense.show_message('Temperatura ambiente')
                sense.set_pixels(vinte_e_dois)
        if ambient_temp== 23:
                sense.show_message('Temperatura ambiente')
                sense.set_pixels(vinte_e_tres)
        if ambient_temp== 24:
                sense.show_message('Temperatura ambiente')
                sense.set_pixels(vinte_e_quatro)
        if ambient_temp== 25:
                sense.show_message('Temperatura ambiente')
                sense.set_pixels(vinte_e_cinco)
        if ambient_temp== 26:
                sense.show_message('Temperatura ambiente')
                sense.set_pixels(vinte_e_seis)
        if ambient_temp== 27:
                sense.show_message('Temperatura ambiente')
                sense.set_pixels(vinte_e_sete)
        if ambient_temp== 28:
                sense.show_message('Temperatura ambiente')
                sense.set_pixels(vinte_e_oito)
        if ambient_temp== 29:
                sense.show_message('Temperatura ambiente')
                sense.set_pixels(vinte_e_nove)
        if ambient_temp== 30:
                sense.show_message('Temperatura ambiente')
                sense.set_pixels(trinta)
        if ambient_temp== 31:
                sense.show_message('Temperatura ambiente')
                sense.set_pixels(trinta_e_um)
        if ambient_temp== 32:
                sense.show_message('Temperatura ambiente')
                sense.set_pixels(trinta_e_dois)
        if ambient_temp== 33:
                sense.show_message('Temperatura ambiente')
                sense.set_pixels(trinta_e_tres)
        if ambient_temp== 34:
                sense.show_message('Temperatura ambiente')
                sense.set_pixels(trinta_e_quatro)
        if ambient_temp== 35:
                sense.show_message('Temperatura ambiente')
                sense.set_pixels(trinta_e_cinco)
        if ambient_temp== 36:
                sense.show_message('Temperatura ambiente')
                sense.set_pixels(trinta_e_seis)
        if ambient_temp== 37:
                sense.show_message('Temperatura ambiente')
                sense.set_pixels(trinta_e_sete)
        if ambient_temp== 38:
                sense.show_message('Temperatura ambiente')
                sense.set_pixels(trinta_e_oito)
        if ambient_temp== 39:
                sense.show_message('Temperatura ambiente')
                sense.set_pixels(trinta_e_nove)
        if ambient_temp== 40:
                sense.show_message('Temperatura ambiente')
                sense.set_pixels(quarenta)
        if ambient_temp== 41:
                sense.show_message('Temperatura ambiente')
                sense.set_pixels(quarenta_e_um)
        if ambient_temp== 42:
                sense.show_message('Temperatura ambiente')
                sense.set_pixels(quarenta_e_dois)
        if ambient_temp== 43:
                sense.show_message('Temperatura ambiente')
                sense.set_pixels(quarenta_e_tres)
        if ambient_temp== 44:
                sense.show_message('Temperatura ambiente')
                sense.set_pixels(quarenta_e_quatro)
        if ambient_temp== 45:
                sense.show_message('Temperatura ambiente')
                sense.set_pixels(quarenta_e_cinco)
        sleep (5)
                
        
    while i==3:
        #WINDSPEED 3
        wind_speed = int(round(my_weather[0]['wind_speed'],0))
        sense.show_message('Velocidade do vento')
        sense.show_message(str(wind_speed))

    while i==4:
        #HUMIDITY 4
        humidity = int(round(my_weather[0]['humidity'],0))
        sense.show_message('Humidade')
        sense.show_message(str(humidity))

    while i==5:
        #RAINFALL 5
        rainfall = int(round(my_weather[0]['rainfall'],0))
        sense.show_message('Precipitacao')
        sense.show_message(str(rainfall))
        
    while i==6:
        #AIRPRESSURE 6
        air_pressure = int(round(my_weather[0]['air_pressure'],0))
        sense.show_message('Pressao do ar')
        sense.show_message(str(air_pressure))
        

    
   




       
    
        
