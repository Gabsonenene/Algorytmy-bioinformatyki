# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 22:19:00 2019

@author: gzdro
"""


def fibo_rek(n):
    '''wyznacza n-ta wartosc ciagu Fibonacciego rekurencyjnie'''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo_rek(n-1) + fibo_rek(n-2)
    
def fibo_iter(n):
    '''wyznacza n-ta wartosc ciagu Fibonacciego iteracyjnie'''
    a = 0
    b = 1
    for i in range(n):
        a, b = b , a+b
    return a

print("\nfunkcja: ", fibo_rek.__name__, fibo_rek.__doc__.upper())
print("\nfunkcja: ", fibo_iter.__name__, fibo_iter.__doc__.upper())
print()
for k in range(28):
    print ("fib dla k=", k, "rekurncyjnie =", fibo_rek(k), "dynamicznie =", fibo_iter(k))
lista_rek = [fibo_rek(k) for k in range(15)]
lista_iter = [fibo_iter(k) for k in range(15)]
print("\nWydruki list:")
print('Rekurencyjnie:', lista_rek)
print('Iteracyjnie:', lista_iter)

if __name__ == '__main__':
    '''Testy dla funkcji:'''
    print(fibo_rek.__name__, '- ', fibo_rek.__doc__.upper())
    assert fibo_rek(12) == 144, 'error:rekurencja'
    assert fibo_rek(0) == 0, 'error:rekurencja'
    assert fibo_rek(1) == 1, 'error:rekurencja'
    print(fibo_iter.__name__, '- ', fibo_iter.__doc__.upper())
    assert fibo_iter(12) == 144 , 'error:iteracja'
    assert fibo_iter(0) == 0, 'error:iteracja'
    assert fibo_iter(1) == 1, 'error:iteracja'
    
    '''Algorytm rekurencyjny ma zlozonosc = 2**n, a algorytm dynamiczny zlozonosc = n.'''