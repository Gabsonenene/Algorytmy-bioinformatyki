# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 20:07:12 2019

@author: gzdro
"""

import czytaj_z_pliku
import pattern_count

def odleglosc(lok, roznica):
    blisko_siebie = [] #pusta lista, do ktorej beda zapisaywane lokalizacje znajdujace sie blisko siebie
    for i in range(1, len(lok)-1): #petla leci od pierwszej pozycji do konca
        if (lok[i] - lok[i-1]) < roznica and (lok[i+1] - lok[i]) < roznica: #porowujemy pozycje, czy mieszcza sie w wyznaczonym zakresie 
            blisko_siebie.append((lok[i-1],lok[i],lok[i+1])) #za pomoca append do listy zapisywane sa szukane pozycje
    return blisko_siebie


if __name__=='__main__':
    #Test funkcji odleglosc, do ktorej potrzebne sa lokalizacje znalezione za pomoca funkcji pattern_count
    dna = czytaj_z_pliku.czytaj_DNA('oriC.txt')
    pattern = 'atgatcaag'
    wystapienia, lista_gdzie = pattern_count.pattern_countt(dna, pattern)
    print('Lokalizacje szukanego wzorca:')
    print(*lista_gdzie) # * usuwa []
    roznica = 600
    blisko_siebie = odleglosc(lista_gdzie, roznica)
    print('Pattern ', pattern, ' wystepuje w odleglosc mniejszej niz ', roznica,' na pozycjach: ', *blisko_siebie)