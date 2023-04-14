# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 13:00:55 2020

@author: gzdro
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Wczytujemy tabelę z pliku titanic.csv:
data = pd.read_csv("titanic.csv")
print("Rozmiar danych:", data.shape)
print("ilosc wierszy:", data.shape[0])
print("ilosc kolumn:", data.shape[1])
print("\n\nNa początku:\n")
print(data.head(20))
print(data.tail(20))

#Symbolizacja wartosci kategorycznych - płeć i gdzie wsiedli:
data["Sex_cleaned"] = np.where(data["Sex"] == "male", 0, 1)
data["Embarked_cleaned"] = np.where(data["Embarked"] == "S", 0, np.where(data["Embarked"] == "C", 1, np.where(data["Embarked"] == "Q", 2, 3)))

#Usuniecie rekordów o niepełnej informacji w badanych kolumnach:
data_poprawne = data[["Survived", "Pclass", "Sex_cleaned", "Age", "SibSp", "Parch",  "Fare","Embarked_cleaned"]].dropna(axis = 0, how = 'any')
print("\n\nPoprawne:\n", data_poprawne)

#Zmienna, ktora zawiera osoby, ktore przezyly
data_przezyli = data_poprawne.loc[(data_poprawne.Survived == 1)]

#Wiek a przezycie - tableka i wykres:
data_wiek = data[["Survived", "Age"]].dropna(axis = 0, how = "any")
print("\n\nWiek a przezycie:\n", data_wiek)
x = data_wiek["Age"]
y = data_przezyli["Age"]
plt.hist(x, edgecolor = 'black', label = 'Wszyscy')
plt.hist(y, edgecolor = 'black', label = 'Przezyli')
plt.xlabel('wiek')
plt.ylabel('liczba osob')
plt.title('Wiek a przezycie na Titanicu')
plt.legend(loc = 'upper right')
plt.show()

#Cena biletu a przezycie - tableka i wykres:
data_oplata = data[["Survived", "Fare"]].dropna(axis = 0, how = "any")
print("\n\nCena biletu a przezycie:\n", data_oplata)
fig = plt.figure()
x = data_oplata["Fare"]
y = data_przezyli["Fare"]
plt.hist(x, edgecolor='black', bins = 50, color = 'red', label = 'Wszyscy')
plt.hist(y, edgecolor='black', bins = 50, color = 'green', label = 'Przezyli')
plt.xlabel('cena biletu')
plt.ylabel('liczba osob')
plt.title('Cena biletu a przezycie na Titanicu')
plt.legend(loc = 'upper right')
plt.show()

#Płeć a przezycie - tableka i wykres:
data_plec = data[["Survived", "Sex_cleaned"]].dropna(axis = 0, how = "any")
print("\n\nPłeć a przezycie:\n", data_plec)
fig = plt.figure()
x = data_plec["Sex_cleaned"]
y = data_przezyli["Sex_cleaned"]
plt.xticks([0, 1]) #usuwa wartosci z osi x miedzy 0 a 1
plt.hist(x, bins = [0, 0.5, 1], edgecolor = 'black', color = 'violet', label = 'Wszyscy')
plt.hist(y, bins = [0, 0.5, 1], edgecolor = 'black', color = 'yellow', label = 'Przezyli')
plt.xlabel('płeć: 0 dla mężczyzn (po lewej), 1 dla kobiet (po prawej)')
plt.ylabel('liczba osob')
plt.title('Płeć a przezycie na Titanicu')
plt.legend(loc = 'upper right')
plt.show()