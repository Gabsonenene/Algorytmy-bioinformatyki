# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 17:27:34 2019

@author: gzdro
"""

import czytaj_z_pliku
import matplotlib.pyplot as plt

def skew(sekwencja, dlugosc):
    #Funkcja sluzy do stworzenia diagramu skosnosci za pomoca wyznaczenia roznicy pomiedzy liczba wystapien G i C w badanej sekwencji 
    C = [] #pusta lista
    ilosc_C = 0 #zmienna ilosc_C na poczatku wynosi 0
    G = [] #pusta lista
    ilosc_G = 0 #zmienna ilosc_G na poczatku wynosi 0
    if dlugosc > len(sekwencja): #jesli dlugosc jest dluzsza od dlugosci sekwencji
        dlugosc = len(sekwencja) #nasza slugosc jest rowna dlugosci sekwencji
    for i in range(0, dlugosc): #petla szuka c i g w calym badanym genomie od 0 przez cala dlugosc sekwencji
        if sekwencja[i] == 'c': #jak zostanie odnalezione c, to ilosc_C wzrasta o 1
            ilosc_C += 1
        elif sekwencja[i] == 'g': #jak odnaleziono g, to ilosc_G wzrsta o 1
            ilosc_G += 1
        C.append(ilosc_C) #wyniki zapisywane sa do list
        G.append(ilosc_G)
    return [C,G]


def rysuj(C,G): #Funkcja sluzy do wyswietlenia wykresu 
    l = len(C) #dlugosc C
    roznica = [] #pusta lista, do ktorej bedzie zapisywana roznica miedzy odelglosciami C i G
    for i in range(0, l):
        roznica.append(G[i] - C[i]) #odejmuje wystapienia C i G, czyli liczy roznice miedzy nimi i zapisuje wyniki do listy  
    plt.plot(range(0, l), roznica) #tworzy wykres z podanych danych
    
if __name__=='__main__':
    #Diagram skosnosci dla oriC
    plik = 'oriC.txt'
    dna = czytaj_z_pliku.czytaj_DNA(plik)
    [C,G] = skew(dna, len(dna))
    plt.title('Diagram skosnosci dla oriC')
    rysuj(C,G)