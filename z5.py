import numpy as np
import math as m
import random

file = open("australian.dat", "r")

listaDecyzji = []

for line in file:
    listaStr = line.split(' ')
    a = lambda e : float(e)
    listaNum = list(map(a, listaStr))
    listaDecyzji.append(listaNum)
file.close()

"""
def policzSrednia(lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    return suma/len(lista)

def policzWariancje(lista, srednia):
    sigma = 0
    for i in range(len(lista)):
        p = m.pow((lista[i] - srednia), 2)
        sigma += p
    sigma /= len(lista)
    return sigma

def policzOdchylenie(lista, srednia):
    return m.sqrt(policzWariancje(lista, srednia))"""

def policzSrednia(lista):
    suma = 0
    wektor = []
    for i in range(len(lista)):
        wektor.append(1)
    suma += np.dot(lista, wektor)
    return suma/len(lista)

def policzWariancje(lista, srednia):
    wektor = []
    x = []
    wynik = []
    for i in range(len(lista)):
        wektor.append(srednia)
    for i in range(len(lista)):
        x.append(lista[i]-wektor[i])
    wynik = np.dot(x,x)
    return wynik/len(lista)

def policzOdchylenie(lista, srednia):
    return m.sqrt(policzWariancje(lista, srednia))


print(policzWariancje([1,2,3,4,5], policzSrednia([1,2,3,4,5]))) 