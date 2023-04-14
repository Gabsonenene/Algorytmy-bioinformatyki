# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 14:37:52 2019

@author: gzdro
"""
import matplotlib.pyplot as plt
import math
import random

def kula2d(x,y):
    '''Funkcja sprawdza czy wartosci naleza do kuli lezacej w przestrzeni dwuwymiarowej'''
    return x**2 + y**2 <= 1

def kartezjanskie(ilosc_puntkow):
    '''Funkcja wyswietla punkty dla losowo wylosowanych liczb we wspolrzednych karteznajnskich'''
    fig = plt.figure()
    plt.title("Wspolrzedne kartezjanskie")
    for i in range(0, ilosc_puntkow):
        p = [2*random.random()-1, 2*random.random()-1]
        if kula2d(p[0], p[1]):
            plt.plot(p[0], p[1], 'r.')
        else:
            plt.plot(p[0], p[1], 'b.')
    plt.show()
    
def biegunowe(ilosc_puntkow):
    '''Funkcja wyswietla punkty dla losowo wylosowanych liczb we wspolrzednych biegunowyc'''
    fig = plt.figure()
    plt.title("Wspolrzedne biegunowe")
    for i in range(0, ilosc_puntkow):
        p = [random.random(), 360*random.random()]        
        x,y = p[0] * math.cos(math.radians(p[1])), p[0] * math.sin(math.radians(p[1]))
        plt.plot(x, y, 'g.')
    plt.show()

if __name__ == '__main__':
    '''Testy funkcji'''
    kartezjanskie(1000)
    biegunowe(1000)
    
    assert kula2d(-1, 0) == True, 'error'
    assert kula2d(-1, -1) == False, 'error'
    assert round(kula2d(2,0)) == 0, 'error'
    assert round(kula2d(0,1)) == 1, 'error'

    '''Wyniki:
    Dla wspolrzednych kartezjanskich: Rozkład jest jednostajny. Punkty we wnetrzu okregu rozkladaja sie rownomiernie.
    Dla kazdego punktu jest to samo prawdopodobienstwo wystapienia w danym miejscu w obrebie okregu.
    
    Dla wspolrzednych biegunowych: Rozkład nie jest jednostajny. Najwiecej puntow koncentruje sie w poblizu srodka okregu. 
    Wynika to z tego, że im mniejszy promien jest brany, tym blizej siebie skupiaja sie punkty.'''