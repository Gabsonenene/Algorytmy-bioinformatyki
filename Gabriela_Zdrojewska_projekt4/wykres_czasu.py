# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 22:38:41 2019

@author: gzdro
"""

'''Obliczenie wydajnosci obliczen Fibonnaciego i przedstawienie ich na wykresie'''

from timeit import default_timer as timer
from fibo import fibo_rek,fibo_iter
import matplotlib.pyplot as plt
import numpy as np

k = range(0,35,3)
rek_czas = []
print('Rekurencyjnie:')
for i in k:
    print("k=%d" % i, end='\t')
    start = timer()
    fib = fibo_rek(i)
    print("rek=%8d" % fibo_rek(i), end='\t')
    end = timer()
    czas = end-start
    rek_czas.append(czas)
    print("Czas=%8fs" % czas)

fig = plt.figure()
iter_czas = []
print('Iteracyjnie:')
for i in k:
    print("k=%d" % i, end='\t')
    start = timer()
    fib = fibo_iter(i)
    print("iter=%8d" % fibo_iter(i), end='\t')
    end = timer()
    czas = end-start
    iter_czas.append(czas)
    print("Czas=%8fs" % czas)

plt.plot(k, iter_czas, 'k-', label = 'dynamicznie')
plt.plot(k, rek_czas,'o-', label = 'rekurencjnie')
plt.legend(fontsize=13)
plt.title("Wykres czasu obliczen liczb Fibonacciego")
plt.xlabel('k')
plt.ylabel("czas(F(k))")
fig = plt.figure()
plt.plot(k, np.log(iter_czas), 'k-', label = 'dynamicznie')
plt.plot(k, np.log(rek_czas),'o-', label = 'rekurencjnie')
plt.legend(fontsize=13)
plt.title("Wykres czasu obliczen logarytmicznie liczb Fibonacciego")
plt.xlabel('k')
plt.ylabel("log(czas(F(k))")
plt.show()

if __name__ == '__main__':
    '''Testy funkcji'''
    assert sum(rek_czas) > sum(iter_czas), 'error'
    assert rek_czas[5] < 1, 'error'
    assert rek_czas[11] > 1, 'error'
    assert iter_czas[11] < 1, 'error'
    
    '''Wyniki: Algorytm dynamiczny jest bardziej wydajny niż algorytm rekurencyjny.
    Dla algorytmu rekurencyjnego wykres funkcji rosnie wykladniczo. Wykres algorytmu dynamicznego jest o wiele mniejszy i staly.
    Przy obliczaniu logarytmu funkcja obliczona rekurencyjnie rosnie liniowo. Za to dla obliczenia dynamicznego wykres losowo rosnie i maleje.
    Jest nadal mniejszy od wykresu algorytmu rekurencyjnego, ale jego czas nie jest juz staly.'''   