

from sense_hat import SenseHat
from datetime import datetime
sense = SenseHat()
from time import sleep

now = datetime.now()

horas= ('{0}:{1} {2}/{3}/{4}'.format(now.hour, now.minute,now.day, now.month, now.year))

                                    

h = sense.get_humidity()




"""class StackList(list):
    def push(self, item):
        self.append(item)


temperatura=StackList([])

temperatura.push(t)"""


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

while True:

        t = ((sense.get_temperature_from_humidity()+sense.get_temperature_from_pressure())/2)
        temperatura=int(round(t,0))

        if temperatura == 15:
                sense.set_pixels(quinze)
        if temperatura == 16:
                sense.set_pixels(dezasseis)
        if temperatura == 17:
                sense.set_pixels(dezassete)
        if temperatura == 18:
                sense.set_pixels(dezoito)
        if temperatura == 19:
                sense.set_pixels(dezanove)
        if temperatura == 20:
                sense.set_pixels(vinte)
        if temperatura == 21:
                sense.set_pixels(vinte_e_um)
        if temperatura == 22:
                sense.set_pixels(vinte_e_dois)
        if temperatura == 23:
                sense.set_pixels(vinte_e_tres)
        if temperatura == 24:
                sense.set_pixels(vinte_e_quatro)
        if temperatura == 25:
                sense.set_pixels(vinte_e_cinco)
        if temperatura == 26:
                sense.set_pixels(vinte_e_seis)
        if temperatura == 27:
                sense.set_pixels(vinte_e_sete)
        if temperatura == 28:
                sense.set_pixels(vinte_e_oito)
        if temperatura == 29:
                sense.set_pixels(vinte_e_nove)
        if temperatura == 30:
                sense.set_pixels(trinta)
        if temperatura == 31:
                sense.set_pixels(trinta_e_um)
        if temperatura == 32:
                sense.set_pixels(trinta_e_dois)
        if temperatura == 33:
                sense.set_pixels(trinta_e_tres)
        if temperatura == 34:
                sense.set_pixels(trinta_e_quatro)
        if temperatura == 35:
                sense.set_pixels(trinta_e_cinco)
        if temperatura == 36:
                sense.set_pixels(trinta_e_seis)
        if temperatura == 37:
                sense.set_pixels(trinta_e_sete)
        if temperatura == 38:
                sense.set_pixels(trinta_e_oito)
        if temperatura == 39:
                sense.set_pixels(trinta_e_nove)
        if temperatura == 40:
                sense.set_pixels(quarenta)
        if temperatura == 41:
                sense.set_pixels(quarenta_e_um)
        if temperatura == 42:
                sense.set_pixels(quarenta_e_dois)
        if temperatura == 43:
                sense.set_pixels(quarenta_e_tres)
        if temperatura == 44:
                sense.set_pixels(quarenta_e_quatro)
        if temperatura == 45:
                sense.set_pixels(quarenta_e_cinco)


        sleep (5)
        sense.clear()
        sense.show_message(str(horas))
        sense.clear()
        
