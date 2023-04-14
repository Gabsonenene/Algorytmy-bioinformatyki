# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 17:07:04 2019

@author: gzdro
"""

import fibo
import kula
import macierz
import czas_fibonacci
import wykres_czasu
import random
import numpy as np

'''Wyniki Fibonacci'''
fibo.fibo_rek(28)
fibo.fibo_iter(28)

'''Wyniki wspolrzedne kartezjanskie i biegunowe'''
kula.kartezjanskie(1500)
kula.biegunowe(1500)

'''Wyniki profile_out'''
macierzz = [[0.2, 0.1, 0.5, 0.1, 0.1, 0.4, 0.2, 0.7], 
       [0.4, 0.6, 0.3, 0.3, 0.1, 0.4, 0.0, 0.2], 
       [0.3, 0.3, 0.1, 0.5, 0.6, 0.1, 0.2, 0.1], 
       [0.1, 0.0, 0.1, 0.1, 0.2, 0.1, 0.6, 0.0]]

macierzz = np.array(macierzz)
ran = random.random()
mm = macierz.przedzial(macierzz)
ilosc = [100, 1000, 10000]
for ilo in ilosc:
    print('\n\nDla {n} zestawow:'.format(n=ilo))
    zestawy = macierz.generator(ilo,mm)    
    d = macierz.profile_out(zestawy)
    macierz.wyswietl_macierz(d)    
    zz = macierz.prawdopodobienstwa(d, ilo)
    macierz.wyswietl_sr_odch(macierz.srednia(zz), macierz.odchylenie(zz))
    macierz.wyswietl_macierz(zz)
