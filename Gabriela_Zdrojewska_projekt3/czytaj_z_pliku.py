# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 08:01:04 2019

@author: gzdro
"""

def czytaj_z_pliku(nazwa_pliku):
    ''' czytamy plik znak po znaku '''
    try:
        plik = open(nazwa_pliku, 'r')#otwieramy dany plik
        print ("\n\nCzytam z " + nazwa_pliku)
        zawartosc = plik.read() #czytamy zawartosc pliku
    except IOError:
        print ("\n\nBłąd dostępu do pliku. STOP?")
        zawartosc = []
    return zawartosc


def czytaj_liniami(nazwa_pliku):
    '''czytamy plik linia po linii'''
    try:
        plik = open(nazwa_pliku, 'r')
        zawartosc = plik.readlines()
    except:
        print ("\n\nBłąd dostępu do pliku. STOP?")
        zawartosc = []
    return zawartosc

def czytaj_DNA(nazwa_pliku):
    '''czytamy plik znak po znaku bez znaku \n'''
    try:
        plik = open(nazwa_pliku, 'r')
        rob = plik.read()
        rob = rob.split() #tworzy liste slow danego napisu
        zawartosc = rob[0]
        for i in range(1,len(rob)):
            zawartosc += rob[i]      
    except IOError:
        print("\n\nBłąd dostępu do pliku. STOP?")
        zawartosc = []
    return zawartosc


if __name__== '__main__':
    #Testy funkcji czytajacych z pliku
    nazwa_pliku = "oriC.txt"
    tekst = czytaj_z_pliku(nazwa_pliku)
    print("\n\nAnaliza wczytanej informacji z pliku ")
    ile = len(tekst)
    rozmiar = tekst.__sizeof__()
    if ile > 0:
        print("\nRozmiar wczytanej informacji ", rozmiar)
        print("\nIlosc wczytanych elementow: ", ile)
        print("\nZawartosc pliku:", tekst)
    tekst = czytaj_DNA(nazwa_pliku)
    print("\n\nAnaliza czytanej liniami informacji z pliku")
    ile=len(tekst)
    rozmiar = tekst.__sizeof__()
    if ile > 0:
        print("\nRrozmiar wczytanej informacji ", rozmiar)
        print("\nIlosc wczytanych elementow: ", ile)
        print("\nSekwencja oriC:", tekst)

        