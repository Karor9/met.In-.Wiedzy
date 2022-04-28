import math as m
import sys
file = open("australian.dat", "r")

listaDecyzji = []

for line in file:
    listaStr = line.split(' ')
    a = lambda e : float(e)
    listaNum = list(map(a, listaStr))
    listaDecyzji.append(listaNum)
file.close()

def z2(lista, k, wniosek):
    wynik = []
    suma = 0
    odleglosc = 0
    for i in range(0, len(lista)):
        for j in range(len(lista[0])-1):
            suma += m.pow((wniosek[j]-lista[i][j]),2) 
        odleglosc = m.sqrt(suma)
        id = lista[i][14]
        wynik.append((id, odleglosc))
        suma = 0
    slow = {}
    for i in range(0, len(wynik)):
        if wynik[i][0] not in slow:
            slow[wynik[i][0]] = []
        slow[wynik[i][0]].append(wynik[i][1])
    w = {}
    pomoc = {x:sorted(slow[x]) for x in slow.keys()}
    s = 0
    for keys in pomoc.keys():
        for i in range(k):
            s += pomoc[keys][i]
        if keys not in w:
            pomoc[keys] = []
        w[keys] = s
        s = 0
    print(w)    
    min = float('inf')
    decyzja = 0
    for keys in w.keys():
        if(w[keys] < min):
            min = w[keys]
            decyzja = keys
        elif(min == w[keys]):
            return None

    return decyzja

print(z2(listaDecyzji, 5, [1,1,1,1,5,1,1,1,1,1,1,1,1,1]))
print(z2(listaDecyzji, 5, [1,1,1,1,11115,1,1,1,1,1,1,1,1,1]))


