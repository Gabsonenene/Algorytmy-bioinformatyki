# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 16:58:27 2019

@author: gzdro
"""

import timeit

'''Zliczenie czasu wykonywanych obliczen: rekurencyjnie i algorytmem dynamicznym'''

my_setup='''
import random
from fibo import fibo_iter, fibo_rek
k = random.sample(range(10,51), 10)
k.sort()
   '''
my_code_r ='''
k=15
fibo_rek(k)    
   '''
my_code_i = '''
k=15
fibo_iter(k)
    '''

    
if __name__ == '__main__':
    '''Testy funkcji:'''
    czas_rek = timeit.timeit(setup= my_setup, stmt = my_code_r, number = 1000)
    print('CZAS rekurencji: %8f' % czas_rek)
    czas_iter = timeit.timeit(setup= my_setup, stmt = my_code_i, number = 1000)
    print('CZAS iteracji: %8f' % czas_iter)
    
    assert czas_rek > czas_iter, 'error'
    
    '''Obliczanie rekurencyjnie ciagu Fibonnaciego jest bardziej czasochlonne niz iteracyjnie.'''
    
    
