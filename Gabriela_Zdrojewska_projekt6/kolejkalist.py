# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 17:39:08 2020

@author: gzdro
"""
'''
Klasa Node reprezentuje pojedynczy element.
Przechowuje obecny oraz nastepny element.
'''
class Node():
    def __init__(self,dane):
        self.dane = dane
        self.nastepny = None
        
    def get_dane(self):
        return self.dane
    
    def get_nastepny(self):
        return self.nastepny
    
    def set_dane(self,dane):
        self.dane = dane
    
    def set_nastepny(self,nastepny):
        self.nastepny = nastepny
    

'''
Klasa KolejkaZDow implementuje kolejke priorytetowa na liscie z dowiazaniami.
'''
class  KolejkaZDow():
    def __init__(self): #inicjuje klase
        self.kolejka = []
        self.head = None
    
    def __str__(self): ##wyswietla zawartosc kolejki oraz head
        s = 'Kolejka: head'
        for node in self.kolejka:
            s+="->"+str(node.get_dane())
        return s
        
    def is_empty(self): #sprawdza czy kolejka nie jest pusta
        return self.head == None
    
    def add(self,element): #dodaje element do kolejki
        node = Node(element)
        if self.head == None:
            self.head = node
        else:
            node.set_nastepny(self.head)
            self.head = node
        self.kolejka.insert(0,node)
    
    def size(self): #rozmiar kolejki
        licznik = 0
        node = self.head
        while node != None:
            licznik+=1
            node = node.get_nastepny()
        return licznik
    
    def remove(self): #usuwa element o najwyzszym priorytecie
        maxx = self.head.get_dane() #max jako pierwszy element
        index = 0
        node = self.head #pierwszy node
        i = 0
        while node != None:            
            if node.get_dane()>maxx: #jesli obecny node jest wiekszy niz max
                maxx = node.get_dane() # to max == node.dane
                index = i
            node = node.get_nastepny() #nastepny node
            i+=1
        self.kolejka.pop(index) #usniecie najwiekszego elementu
        if index == 0: #usuwanie pierwszego elementu (head)
            if self.kolejka != []: # jesli kolejka nie jest pusta
                self.head = self.kolejka[0] #zmiana head
            else:
                self.head = None #jesli kolejka jest pusta, przypisuje None
        elif index == self.size()-1: #usuwanie ostatniego elemnetu
            self.kolejka[index-1].set_nastepny(None) #wyzerowanie referencji
        else:
            self.kolejka[index-1].set_nastepny(self.kolejka[index])
        return maxx
    
    def search(self,element): #wyszukuje dany element w kolejce
        node = self.head
        while node != None:
            if node.dane == element:
                return True
            node = node.get_nastepny()
        return False

if __name__ == "__main__":
    kolejka =  KolejkaZDow()
    assert(kolejka.is_empty()==True), 'błąd'
    kolejka.add(10)
    assert(kolejka.is_empty()==False), 'błąd'
    kolejka.remove()
    assert(kolejka.is_empty()==True), 'błąd'
    kolejka.add(1)
    kolejka.add(1)
    kolejka.add(2)
    kolejka.add(9)
    kolejka.add(3)
    kolejka.add(0)
    kolejka.add(5)
    assert(kolejka.is_empty()==False), 'błąd'
    print('Po dodaniu elementow:')
    print(str(kolejka))
    assert((kolejka.size())==7), 'błąd'
    kolejka.remove()
    print('Kolejka po usunieciu elementu o najwiekszym priorytecie:',kolejka)
    kolejka.remove()
    assert((kolejka.size())==5), 'błąd'
    print('Kolejka po usunieciu kolejnego elementu:')
    print(str(kolejka))  
    assert(kolejka.search(1)==True), 'błąd'
    assert(kolejka.search(10)==False), 'błąd'
    print('Rozmiar kolejki =', kolejka.size())