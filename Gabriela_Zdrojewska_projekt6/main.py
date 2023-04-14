# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 18:39:10 2020

@author: gzdro
"""

import random
import time
import matplotlib.pyplot as plt
import kolejkalist as klist
import kolejkapyt as kpyt

def listaP():
    czas_kolejkowania = [] #suma czasu dodawania elementow
    czas_odkolejkowania = [] #suma czasu usuwania elementow
    roz = []
    i = 10
    
    for i in range(10,17):
        rozmiar = 2**i
        roz.append(rozmiar)
        start1 = time.time() #czas, kiedy rozpoczyna sie dodawanie el.
        kolejka = kpyt.KolejkaPython()
        while kolejka.size() < rozmiar:
            kolejka.enqueue(random.randint(1,1000))
        koniec1 = time.time() #koniec czasu dodawania el.
        czas_kolejkowania.append(koniec1 - start1)
        start2 = time.time() #czas, kiedy rozpoczyna sie odejmowanie el.
        while kolejka.size() > 0:
            kolejka.dequeue()
        koniec2 = time.time() #koniec czasu odejmowania el.
        czas_odkolejkowania.append(koniec2 - start2)
        i+=1
    return [roz, czas_kolejkowania, czas_odkolejkowania]

[roz,czas_kolejkowania,czas_odkolejkowania] = listaP()
print('Lista Python:')
print('Czas dodawania elementow do kolejki', czas_kolejkowania)
print('Czas odejmowania elementow z kolejki', czas_odkolejkowania)

def listaKD():
    czas_kolejkowaniaa = [] #suma czasu dodawania elementow
    czas_odkolejkowaniaa = [] #suma czast usuwania elementow
    roz = []
    i = 10
    
    for i in range(10,17):
        rozmiar = 2**i
        roz.append(rozmiar)
        start1 = time.time()  #czas, kiedy rozpoczyna sie dodawanie el.
        kolejka = klist.KolejkaZDow()
        while kolejka.size() < rozmiar:
            kolejka.add(random.randint(1,1000))
        koniec1 = time.time() #koniec czasu dodawania el.
        czas_kolejkowaniaa.append(koniec1 - start1)
        start2 = time.time() #czas, kiedy rozpoczyna sie odejmowanie el.
        while kolejka.size() > 0:
            kolejka.remove()
        koniec2 = time.time() #koniec czasu odejmowania el.
        czas_odkolejkowaniaa.append(koniec2 - start2)
        i+=1
    return [roz, czas_kolejkowaniaa, czas_odkolejkowaniaa]

[rozz,czas_kolejkowaniaa,czas_odkolejkowaniaa] = listaKD()
print('\nLista z dowiazaniami:')
print('Czas dodawania elementow do kolejki:', czas_kolejkowaniaa)
print('Czas odejmowania elementow z kolejki:', czas_odkolejkowaniaa)

#Wykresy:
plt.loglog(roz, czas_kolejkowania, basex = 2, basey = 2, color = 'r')
plt.loglog(roz, czas_kolejkowaniaa, basex = 2, basey = 2, color = 'g')
plt.title('Czas budowania kolejki')
plt.xlabel('liczba elementów')
plt.ylabel('log(czas)')
plt.legend(['lista Pythona', 'lista z dowiązaniami'], loc='upper left')
fig=plt.figure()
plt.loglog(roz, czas_odkolejkowania,basex = 2, basey = 2, color = 'r')
plt.loglog(roz, czas_odkolejkowaniaa,basex = 2, basey = 2, color = 'g')
plt.title('Czas odejmowania elementow z kolejki')
plt.xlabel('liczba elementów')
plt.ylabel('log(czas)')
plt.legend(['lista Pythona', 'lista z dowiązaniami'], loc='upper left')
plt.show()  