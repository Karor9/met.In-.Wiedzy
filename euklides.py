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


def policzOdleglosc(lista1, lista2, utnij=False):
    if(utnij):
        v1 = np.array(lista1[:-1])
        v2 = np.array(lista2[:-1])
    else:
        v1 = np.array(lista1)
        v2 = np.array(lista2)

    c = v1-v2

    s = np.dot(c,c)
    return m.sqrt(s)

def policzOdleglosci(losoweDecyzje):
    wynik = {}
    for keys in losoweDecyzje.keys():
        for a in losoweDecyzje[keys]:
            odleglosc = 0
            for b in losoweDecyzje[keys]:
                odleglosc += policzOdleglosc(a,b, True)
            if keys not in wynik:
                wynik[keys] = []
            wynik[keys].append((odleglosc, a))
    return wynik

def generujDecyzje(lista):
    wynik = {}
    for row in lista:
        r = random.randrange(0,2)
        row[-1] = r
        if r not in wynik:
            wynik[r] = []
        wynik[r].append(row)
    return wynik

def znajdzMinimum(lista):
    minimum = float('inf')
    minimalnyPunkt = []
    for x in lista:
        if(x[0] < minimum):
            minimum = x[0]
            minimalnyPunkt = x[1]
    return(minimum, minimalnyPunkt)

def znajdzDecyzje(minima, lista):
    for row in lista:
        minimum = float('inf')
        minimalnaDecyzja = None
        for keys in minima.keys():
            odleglosc = policzOdleglosc(row, lista[keys][1])
            if(odleglosc < minimum):
                minimum = odleglosc
                minimalnaDecyzja = minima[keys][1][-1]
        row[-1] = minimalnaDecyzja
    wynik = {}
    for row in lista:
        if row[-1] not in wynik:
            wynik[row[-1]] = []
        wynik[row[-1]].append(row)
    return wynik


def zmienDecyzje(slownik, minima):
    pomoc = []
    for keys in slownik.keys():
        for row in slownik[keys]:
            pomoc.append(row)
    wynik = {}
    wynik = znajdzDecyzje(minima, pomoc)
    return wynik

def koloruj(lista):
    losoweDecyzje = generujDecyzje(lista)
    for x in range(25):
        listaOdleglosci = policzOdleglosci(losoweDecyzje)
        listaMinimow = {}
        for keys in losoweDecyzje.keys():
            listaMinimow[keys] = znajdzMinimum(listaOdleglosci[keys])
        losoweDecyzje = zmienDecyzje(losoweDecyzje, listaMinimow)
    return losoweDecyzje
    

test = koloruj(listaDecyzji)

print(test)
