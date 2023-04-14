# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 08:21:37 2019

@author: gzdro
"""

import czytaj_z_pliku

#Funkcje pokazuja liczbe wystąpien danego k-meru oraz jego lokalizacje
def pattern_countt(sekw, kmer):
    count = 0 #zmienna count poczatkowo wynosi 0, to nasza ilosc wystapien 
    lokalizacja = [] #poczatkowo lista jest pusta
    k_mer = len(kmer) #funkcja len zwraca dlugosc lancucha
    for i in range(len(sekw) - k_mer): #petla przeszukuje lanuch, szukajac ilosci wystpien w sekwencji dlanego kmeru  
        if (sekw[i:(i+k_mer)] == kmer):
            count += 1 #jak zostanie odnalezniony kolejne wystapinie kmeru, count wrasta o 1
            lokalizacja.append(i)#jak kmer zostanie odnaleziony do listy zapisywana jest jego lokalizajca dzieki funkcji append, ktora dodaje do listy kolejny element
    return count, lokalizacja

def count_wzorzec(txt, wzorzec):
    gdzie = [] #pusta lista
    bylo = txt.find(wzorzec) #za pomoca find odnajdujemy szukany kmer w sekwencji, zwraca -1 jesli kmer nie zostanie odnaleziony
    while bylo > -1: #dopoki find nie zwroci -1, czyli nie da nam znac, ze nie ma wiecej poszukiwanych kmerow, petla bedzie wykonywana
        gdzie.append(bylo) #zapisuje do listy gdzie lokalizacje odnalezionego kmeru
        bylo = txt.find(wzorzec, bylo+1)
    return gdzie


if __name__=='__main__':
    dna = czytaj_z_pliku.czytaj_DNA('oriC.txt')
    
    #Test funkcji pattern_count, ktora dla danego kmeru pokazuje liczbe jego wystapien oraz lokalizacje
    print('Test pattern_count:')
    pattern = 'atgatcaag'
    wystapienia, lista_gdzie = pattern_countt(dna, pattern)
    print("Poszukiwany k-mer:", pattern)
    print("Liczba wystapien:", wystapienia)
    print("Lokalizacja:", *lista_gdzie)# * - usuwa []
    
    #Test funkcji count_wzorzec, ktorej wyniki sa takie same jak dla funkcji pattern_count
    print('\n\nTest count_wzorzec:')
    txt = czytaj_z_pliku.czytaj_DNA('oriC.txt')
    szukam = 'atgatcaag'
    print('Poszukiwany k-mer', szukam)
    gdzie = count_wzorzec(txt, szukam)
    wystapienia = count_wzorzec(txt, szukam)
    print('Liczba wystapien:', len(wystapienia))
    print('Lokalizacja:', *gdzie)# * - usuwa []
    
    