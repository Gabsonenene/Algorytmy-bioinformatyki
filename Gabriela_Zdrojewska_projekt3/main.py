# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 08:28:44 2019

@author: gzdro
"""
#Moduly:
import czytaj_z_pliku as czp
import pattern_count as pc
import odleglosci as o
import komplementarna_nic as kn
import diagram as d
import pylab as pl
import matplotlib.pyplot as plt

plik = 'V_C.fna'
dna = czp.czytaj_DNA(plik)

print('Badamy genom Vibrio cholerae')

#Sprawdzamy lokalizacje najczesciej pojawiajacych sie w oriC 9-merow w celu zlokalizowania oriC w calym genomie cholery

#Dla ATGATCAAG:
pattern = 'atgatcaag'.upper() #upper zwieksza znaki
print('\n\nBadany pattern:', pattern)
#Funkcja pattern_count:
wystapienia, lista_gdzie = pc.pattern_countt(dna, pattern)
print('Liczba wystapien:', wystapienia)
print('Lokalizacje szukanego wzorca:')
print(*lista_gdzie) # * - usuwa []
#Funkcja odleglosc:
roznica = 600
przefiltrowane = o.odleglosc(lista_gdzie, roznica)
print('Pattern ', pattern, ' wystepuje w odleglosc mniejszej niz ', roznica,' na pozycjach: ', *przefiltrowane)


#Dla CTCTTGATC:
pattern = 'ctcttgatc'.upper()
print('\n\nBadany pattern:', pattern)
wystapienia, lista_gdzie = pc.pattern_countt(dna, pattern)
print('Liczba wystapien:', wystapienia)
print('Lokalizacje szukanego wzorca:')
print(*lista_gdzie)
roznica = 600
przefiltrowane = o.odleglosc(lista_gdzie, roznica)
print('Pattern: ', pattern, ' wystepuje w odleglosc mniejszej niz ', roznica,' na pozycjach: ', *przefiltrowane)


#Dla TCTTGATCA:
pattern = 'tcttgatca'.upper()
print('\n\nBadany pattern:', pattern)
wystapienia, lista_gdzie = pc.pattern_countt(dna, pattern)
print('Liczba wystapien:', wystapienia)
print('Lokalizacje szukanego wzorca:')
print(*lista_gdzie)
roznica = 600
przefiltrowane = o.odleglosc(lista_gdzie, roznica)
print('Pattern: ', pattern, ' wystepuje w odleglosc mniejszej niz ', roznica,' na pozycjach: ', *przefiltrowane)

#Dla CTTGATCAT:
pattern = 'cttgatcat'.upper()
print('\n\nBadany pattern:', pattern)
wystapienia, lista_gdzie = pc.pattern_countt(dna, pattern)
print('Liczba wystapien:', wystapienia)
print('Lokalizacje szukanego wzorca:')
print(*lista_gdzie)
roznica = 600
przefiltrowane = o.odleglosc(lista_gdzie, roznica)
print('Pattern: ', pattern, ' wystepuje w odleglosc mniejszej niz ', roznica,' na pozycjach: ', *przefiltrowane)


#Sprawdzenie, czy ATGATCAAG jest komplementarne do CTTGATCAT:
sekwencja = 'ATGATCAAG'.lower() #lower zmniejsza znaki
komp = kn.komplementarna_nic(sekwencja)
print('\n\nSekwencja komplementarna do ATGATCAAG:', komp.upper())

print('\nUdalo nam sie odnalezc oriC!')

#Diagram skosnosci dla V_C
[c,g] = d.skew(dna.lower(), len(dna))
plt.title('Diagram skosnosci dla Vibrio cholerae') #tytul
d.rysuj(c,g) #wyswietla wykres


#Diagram skosnosci dla E. coli
plik = 'ecoli.fna'
sekwen = czp.czytaj_DNA(plik)
[CC,GG] = d.skew(sekwen.lower(), len(sekwen))
plt.figure()#rozdziela wykresy na dwa 
plt.title('Diagram skosnosci dla E. coli') #tytul
d.rysuj(CC,GG) #wyswietla wykres


#W main sprawdzona zostala liczba i lokalizacja danych 9-merow.
#'ATGATCAAG' w całym genomie wystąpił 37 razy.
#Jego lokalizacja, powtarzająca się trzy razy najczęściej w najmniejszych odstępach od siebie, to:
#(2961525, 2961582, 2961653)
#Komplementarną do niego sekwencją okazał się 9-mer 'CTTGATCAT', który wystąpił w całym genomie aż 49 razy.
#Jego lokalizacja w badanym miejscu jest bardzo podobna do lokazlizacji 'ATGATCAAG': (2961542, 2961923, 2962023)
#Pozostałe dwa 9-mery nie posiadają sekwencji, które leżałyby tak blisko siebie.
#Z tego możemy wynioskować, że poszukiwany oriC znajduje się w lokazliacji od 2961525 do 2962023.
#Dzieki diagramowi skosnosci udalo sie potwierdzic hipoteze, ze oriC znajduje sie w takiej lokalizacji.
#Punty minimum znajdujace sie na wykresie pokrywaja sie z polozeniem szukanego oriC.
#Udalo sie takze wyznaczyc oriC w genomie E. coli za pomoca diagramu skosnosci.