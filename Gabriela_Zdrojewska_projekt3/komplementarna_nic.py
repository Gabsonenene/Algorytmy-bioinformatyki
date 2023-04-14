# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 16:45:44 2019

@author: gzdro
"""

import czytaj_z_pliku

def komplementarna_nic(nic):
    #funkcja zamienia a na t, t na a, g na c, c na g przy zamienianie liter malych na wielkie za pomoca replace
    nic = nic.replace('a', 'T')
    nic = nic.replace('t', 'A')
    nic = nic.replace('g', 'C')
    nic = nic.replace('c', 'G')
    nic = nic.lower()#zamiana duzych liter na male
    komp_nic = nic[::-1]#odwrocenie nici
    return komp_nic

    
if __name__=='__main__':
    #Test funkcji komplementarna_nic, ktora sluzy do wyswietlenia komplementarnej sekwencji dla badanej nici
    sekwencja = czytaj_z_pliku.czytaj_DNA('oriC.txt')
    komp_nic = komplementarna_nic(sekwencja)
    print("Sekwencja komplementarna oriC:", komp_nic)


