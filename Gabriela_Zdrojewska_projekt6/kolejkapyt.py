# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 16:47:45 2020

@author: gzdro
"""

'''
Klasa, ktora implementuje samosortujaca sie kolejke priorytetowa
(od elementu z najmniejszym priorytetem do elementu o najwiekszym priorytecie) na liscie Python.
Pierwszy element, ktory zostanie usuniety, to ten o najwiekszym priorytecie.
'''
class KolejkaPython:
    def __init__(self): #inicjuje klase
        self.kolejka = []
    
    def __str__(self): #wyswietla zawartosc kolejki
        return 'Kolejka: '+str(self.kolejka)
    
    def is_empty(self): #sprawdza czy jest chociaz 1 element w kolejce
        return len(self.kolejka)<1
    
    def enqueue(self,element): #dodaje element do kolejki w odpowiednie miejsce
        if self.is_empty():# jesli kolejka jest pusta - dodaje na poczatek
            self.kolejka.insert(0,element)
        else:                               #jesli nie jest pusta  
            for kol in range(self.size()):  #szuka indeksu pierwszego wiekszego elementu niz dodawany       
                if element<self.kolejka[kol]: # i dodaje sie przed niego
                    self.kolejka.insert(self.kolejka.index(self.kolejka[kol]),element)
                    return #wychodzi z funckji po dodaniu
        self.kolejka.append(element) # jesli nie znalazlo elementu wiekszego, dodaje sie na koniec
        
    def dequeue(self): #usuwa element o najwyzszym priorytecie
        return self.kolejka.pop()
    
    def size(self): #rozmiar kolejki
        return len(self.kolejka)
    

#Testy:
if __name__ == "__main__":
    kolejka = KolejkaPython()
    assert(kolejka.is_empty()==True), 'błąd'
    print('Dodajemy po kolei elementy do kolejki:')
    print(str(kolejka))
    kolejka.enqueue(1)
    print(str(kolejka))
    kolejka.enqueue(2)
    print(str(kolejka))
    kolejka.enqueue(0)
    print(str(kolejka))
    kolejka.enqueue(5)
    print(str(kolejka))
    kolejka.enqueue(9)
    print(str(kolejka))
    kolejka.enqueue(3)
    assert((kolejka.size())==7), 'błąd'
    print(str(kolejka))
    assert(kolejka.dequeue()==9), 'błąd'
    print('\nPo usunieciu elementu o najwiekszym prirytecie:')
    print(str(kolejka))
    assert(kolejka.dequeue()==5), 'błąd'
    print('\nPo usunieciu kolejnego elementu o najwiekszym prirytecie:')
    print(str(kolejka))
    assert((kolejka.size())==5), 'błąd'
    assert(kolejka.is_empty()==False), 'błąd'
    print('Rozmiar kolejki =', kolejka.size())
    
    
    