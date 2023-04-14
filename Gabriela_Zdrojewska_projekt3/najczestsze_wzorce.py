# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 18:42:25 2019

@author: gzdro
"""

import czytaj_z_pliku

def najczestsze_wzorce(sekwencja, n):
    wzorce = [] #pusta lista
    for i in range(0, len(sekwencja) - n):#przeszukuje sekwencje i tworzy liste wzorcow, sprawdza, jakie sa wzorce
        wzorce.append(sekwencja[i:i+n]) 
    #korzystam ze slownika, poniewaz to rozwiauje problem duplikatow
    ilosc_wzorcow = dict.fromkeys(wzorce, 0) #tworzy slownik z listy wzorcow
    for i in range(0, len(sekwencja)-n): #petla zlicza nam ilosc wzorcow    
        ilosc_wzorcow[sekwencja[i:i+n]] += 1
    maxx = 0
    for v in ilosc_wzorcow.values(): #szuka maksa, czyli maksymalnych elementow, ktore wystapily 
        if v > maxx:
            maxx = v
    najczestsze = []
    for k,v in ilosc_wzorcow.items(): #petla filtruje po maksie i dodaje te co maja maksa do tablicy z najczęstszymi
        if v == maxx:
            najczestsze.append(k)
    return [najczestsze, maxx]
            
if __name__=='__main__':
    #Test funkcji najczestsze_wzrce, ktora wyswietla najczesciej pojawiajace sie wzorce w danym genomie
    plik = 'oriC.txt'
    dna = czytaj_z_pliku.czytaj_DNA(plik)
    print('\nNajczestsze wzorce')
    for i in range(3,14): #Petla sluzaca do wyswietlania wynikow funkcji w formie tabelki
        [najczestsze, maxx] = najczestsze_wzorce(dna,i)
        print('rozmiar: ', i,' krotnosc: ', maxx, ' mialy slowa: ', *najczestsze)
        
        
#Wyniki pokrywaja sie z wynikami w ksiazce. Udalo nam sie wyznaczyc najczestsze wzorce dla oriC.