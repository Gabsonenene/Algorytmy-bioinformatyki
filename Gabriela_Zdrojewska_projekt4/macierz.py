# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 15:30:24 2019

@author: gzdro
"""
import math
import random
import numpy as np

def przedzial(mac):
    '''Funkcja tworzy przedzialy'''
    for i in range(1, len(mac)):
        for j in range(0, len(mac[0])):
            mac[i][j] += mac[i-1][j]
            mac[i][j] = round(mac[i][j],1)
    return mac

def litera(prawd, mac): 
    '''Funkcja zwraca nam A, C, G, T w zaleznosci od prawdopodobienstwa podanego w macierzy'''
    if prawd < mac[0]:
        return 'A'
    elif prawd < mac[1]:
        return 'C'
    elif prawd < mac[2]:
        return 'G'
    elif prawd < mac[3]:
        return 'T'
    else:
        return ''

def generator(ilosc, mac):
    '''Funkcja generuje nam zestawy 8-merow dla losowych liczb'''
    zestawy = []
    for z in range(ilosc):
        zestaw = ''
        for i in range(8):
            r = random.random()
            zestaw += litera(r, mac[:,i])
        zestawy.append(zestaw)
    return zestawy

def profile_out(zestawy):
    '''Funkcja sluzy do stworzenia macierzy profile_out'''
    d = dict.fromkeys(range(1,9),{})
    for k in d:
        miejsce = dict.fromkeys(['A','C','G','T'], 0)
        d[k] = miejsce     
    for zestaw in zestawy:        
        for i in range(8): 
            d[i+1][zestaw[i]] += 1
    return d

def prawdopodobienstwa(zliczone, ilosc):
    '''Funkcja zlicza ilosc prawdopodobienstw'''
    for k in zliczone:
        for ki in zliczone[k]:
            zliczone[k][ki] /= ilosc
    return zliczone

def srednia(zliczone):
    '''Funkcja sluzy do wyliczenia sredniej ilosci wystapien danego nukleotydu na danej pozycji'''
    sr = np.zeros((4,1))
    for k in zliczone:
        i = 0
        for ki in zliczone[k]:        
            sr[i] += zliczone[k][ki]
            i += 1
    sr = sr/8
    return sr

def odchylenie(zliczone):
    '''Funkcja sluzy do wyliczenia odchylenia standardowego dla danej sredniej'''
    z = {}
    sr = srednia(z)    
    suma = np.zeros((4,))
    for k in zliczone:
        i = 0
        for ki in zliczone[k]:        
            suma[i] += (zliczone[k][ki]-sr[i])**2
            i += 1 
    odchylenie = np.sqrt(suma/8)    
    return odchylenie
        
def wyswietl_macierz(z):
    '''Funkcja sluzy do wyswietlenia macierzy'''
    acgt = list(z[1].keys())
    print('\t{0}\t{1}\t{2}\t{3}'.format(acgt[0], acgt[1], acgt[2], acgt[3]))
    for k in z:
        print(k, z[k]['A'], z[k]['C'], z[k]['G'], z[k]['T'], sep='\t')
    
def wyswietl_sr_odch(srd, od):
    '''Funckja wyswietla srednia oraz odchylenie standardowe'''
    print('Srednia \u00B1 Odchylenie')
    litery = ['A','C','G','T']
    for i in range(len(srd)):        
        print('p({litera}): {sr} \u00B1 {odch}'.format(litera = litery[i], sr = srd[i], odch = od[i]))
    
    
if __name__ == '__main__':         
    '''Testy'''
    macierz = [[0.2, 0.1, 0.5, 0.1, 0.1, 0.4, 0.2, 0.7], 
       [0.4, 0.6, 0.3, 0.3, 0.1, 0.4, 0.0, 0.2], 
       [0.3, 0.3, 0.1, 0.5, 0.6, 0.1, 0.2, 0.1], 
       [0.1, 0.0, 0.1, 0.1, 0.2, 0.1, 0.6, 0.0]]
    macierz = np.array(macierz)
    r = random.random()
    m = przedzial(macierz)
    ilosc = [100, 1000, 10000]
    for ilo in ilosc:
        print('\n\nDla {n} zestawow:'.format(n=ilo))
        zestawy = generator(ilo,m)    
        d = profile_out(zestawy)
        wyswietl_macierz(d)    
        z = prawdopodobienstwa(d, ilo)    
        wyswietl_sr_odch(srednia(z),odchylenie(z))   
        wyswietl_macierz(z)
    
    assert m.all() == 1, 'error'
    assert sum(m).any() == 1, 'error'
    
    '''Wyniki: dla 10000 zestawow prawdopodobienstwa w macierzy profile_out sa najbardziej zblizone do prawdopodienstw z macierzy profile_in.
    Im wiekszy numer zestawow, tym mniejsze odchylenie standardowe. Im mniejsze odchylenie, tym bardziej podobne wartosci.'''
    
    
