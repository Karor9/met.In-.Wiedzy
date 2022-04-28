#conajmniej 10 znaków, duże i małe, oraz !
import sys

def testPassword(password):
    if(len(password) <= 10):
        return False
    if(password.lower() == password):
        return False
    if(password.upper() == password):
        return False
    if("!" not in password):
        return False
    return True


string = "toFsthaslot!est"
string2 = "HASLOHASLO!"

#print(testPassword(string))
#print(testPassword(string2))

lista = [41, 2, 51, 6, 1, 99]

#for element in lista:
#    if(element != 99):
#        print(element)

def czyNalezy(lista, element):
    i = 0
    nalezy = False
    while(i < len(lista)):
        if(lista[i] == element):
            nalezy = True
            break
        i += 1
    return nalezy

#print(czyNalezy(lista, 99))
#print(czyNalezy(lista, 4))

plik = open("plik.txt", "r")

for line in plik:
    print(line)

plik.close()
plik = open("plik.txt", "r")

for line in plik:
    print(line, end='')
plik.close()

lista = ["C#", "python", "C++", "C", "Java"]


#with open('plik2.txt', 'w') as plik:
#    for jezyk in lista:
#        print(jezyk, file=plik)


lista1 = ["Olsztyn", "Warszawa", "Kraków", "Łódź"]

mapa = map(lambda x : x[:3],lista1)

converted_list = list(mapa)
print()
print(str(converted_list))

listaPlikow = ["text.txt", "dokument.doc", "zdjecie.png", "inneZdjecie.jpg", "jeszczeinnezdjecie.png"]

def sprawdzRozszerzenie(lista, rozszerzenie):
    listaPlik = []
    for element in lista:
        indexDot = element.find(".")
        if(element[indexDot+1:] == rozszerzenie):
            listaPlik.append(element)


    return listaPlik

def generatorRozszerzen(lista, rozszerzenie):
    for element in lista:
        indexDot = element.find(".")
        if(element[indexDot+1:] == rozszerzenie):
            yield element


print(sprawdzRozszerzenie(listaPlikow, "txt"))
listazGeneratora = list(generatorRozszerzen(listaPlikow, "png"))
print(listazGeneratora)

