#!/usr/bin/python
import sys
import serial
import struct
import time
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime
import csv

start_frequency = 77000000        #25-6000MHz
increment       = 0
steps           = 4000

sf= int(start_frequency/10)


cmd = "\x8f" + "x" + '{:09d}{:08d}{:04d}'.format(sf, increment, steps)


#transmisja z NWT6000
ser = serial.Serial('COM4', 57600, timeout=100)

ser.write(cmd.encode())

#czas rozpoczęcia pomiaru
dt1 = datetime.now()
print("Data:", dt1)
                     
rsp = ser.read(4 * steps)

#czas zakonczenia pomiaru
dt2 = datetime.now()

if len(rsp) < (4 * steps):
    sys.stderr.write("Warning : Did not read enough measures! Try increasing the timeout\n")
    steps = len(rsp)/4    
val_tab = struct.unpack_from("<" + "h"*2*steps, rsp) 


#wydruk czasow pomiaru: 5 sek, 15 ms
print("Czas pomiaru:")
print(dt2-dt1)


#tu mozna zobaczyc cala tablice pomiarow
#for i in range(0, steps):
#    print(val_tab[2*i])	


# os czasu
t = np.arange(0.0, steps, 1)

# wartości pomiaru
s = list(val_tab)

p = [None]* steps
print("Zebrane probki:")
print(len(s))

#usuwamy co druga probke
for n in range(0, steps):
    #print(n)
    p[n]=(int(val_tab[2*n]))

#wydruk próbek    
print(p)

#wykres
fig, ax = plt.subplots()
ax.plot(t, p)

ax.set(xlabel='Zebrane próbki', ylabel='Napięcie (mV)',
       title="Częstotliwość [Hz] = %d" %start_frequency)
ax.grid()

fig.savefig("test.png")
plt.show()

#zapis do pliku:
np.savetxt('pomiar.csv', p, delimiter=',')
