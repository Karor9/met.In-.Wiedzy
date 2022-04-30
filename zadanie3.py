import math as m    

file = open("australian.dat", "r")

newList = []

for line in file:
    listaStr = line.split(' ')
    a = lambda e : float(e)
    listaNum = list(map(a, listaStr))
    newList.append(listaNum)


odl = []


sum = 0
for j in range(1,4):
    for i in range(len(newList[0])-1):
        sum += m.pow((newList[0][i]-newList[j][i]),2)
    odl.append(m.sqrt(sum))
    sum = 0

#print(odl)


file.close()

#Wybieram y=lista[0] muszę odległość od y a x, gdzie x należy do listy bez 0 indeksu z pozostałymi
#robie z tego słownik - klucz to klasa decyzyjna, wartośc to odległość (z tej samej klasy)

def makeDictionay(newList):
    slownik = {}
    suma = 0
    odleglosc = 0
    for i in range(1, len(newList)):
        for j in range(len(newList[0])-1):
            suma += m.pow((newList[0][j]-newList[i][j]),2) 
        odleglosc = m.sqrt(suma)
        id = newList[i][14]
        if id in slownik:
            slownik[id].append(odleglosc)
        else:
            slownik[id] = []
            slownik[id].append(odleglosc)
        
        suma = 0
    return slownik


#print(makeDictionay(newList))

#print(newList)

def zad(lista):
    wynik = []
    suma = 0
    odleglosc = 0
    for i in range(0, len(newList)):
        for j in range(len(newList[0])-1):
            suma += m.pow((1-newList[i][j]),2) 
        odleglosc = m.sqrt(suma)
        id = newList[i][14]
        wynik.append((id, odleglosc))
        suma = 0
    return wynik

def intoSlownik(lista):
    help = zad(lista)
    wynik = {}
    for i in range(0, len(help)):
        if help[i][0] not in wynik:
            wynik[help[i][0]] = []
        wynik[help[i][0]].append(help[i][1])
    return wynik

def decyduj(slownik, k=5):
    wynik = {}
    pomoc = {x:sorted(slownik[x]) for x in slownik.keys()}

    suma = 0
    for keys in pomoc.keys():
        for i in range(k):
            suma += pomoc[keys][i]
        if keys not in wynik:
            pomoc[keys] = []
        wynik[keys] = suma
        suma = 0
        

    return wynik

#print(decyduj(intoSlownik(newList)))



#mamy metrykę euklidesową. Robimy pierwiastek z sumy kwadratów różnic Zrobić metrykę w oparciu o wektor i działania na wektorze
#łączac to, trzeba wyprodukować funkcje x, liste oarz k i zwroci decyzje