#name = input("Jak się nazywasz?\n")

#print("Cześć {}".format(name))


from tkinter.tix import ExFileSelectBox


s = "test"
c = 5
f = 7.1

print("s: {0}, typ: {1}\nc: {2}, typ: {3}\nf: {4}, typ: {5}".format(s, type(s), c, type(c), f, type(f)))




lista = ["to", "jest", "kilka", "slow"]

laczone = '#'.join(lista)

print(laczone)

dzielone = laczone.split('#')

print(dzielone)

z = "Metody Inżynierii Wiedzy są najlepsze"
print("{0} - jest to {1} znaków".format(z, len(z)))
z = z.lower()
print("{0} - jest to {1} znaków".format(z, len(z)))
print("{0} - jest to {1} znaków".format(z.upper(), len(z)))

zm = z.replace("ą", "a").replace("ę", "e").replace("ś","s").replace("ć","c").replace("ó","o").replace("ł", "l").replace("ż","z").replace("ź","z").replace("ń", "n").replace(" ", "")

print("{0} - jest to {1} znaków".format(zm, len(zm)))

se = set(zm)

print("{0} - jest to {1} znaków".format(se, len(se)))

s1 = "toString"
i1 = 5

para = (s1,i1)

print("{0} - typ {1}".format(para, type(para)))

l2 = ["C++", "C#", "python", "Java"]


print(l2.index('python'))

slownik = {"Polska":"Warszawa","Rosja":"Moskwa","Litwa":"Wilno","Białoruś":"Mińsk","Ukraina":"Kijów","Słowacja":"Bratysława","Czechy":"Praga","Niemcy":"Berlin"}

print("{0}".format(sorted(slownik)))

print(bool(" "))
print(bool(""))
print(bool("1"))
print(bool("0"))
print(bool(["",""]))

zdanie = "Trzeba sobie wymyśleć jakieś zdanie i napisać z ifem taki warunek że sprawdza czy jest więcej niż 15 unikalnych znaków"
if(len(set(zdanie)) > 15):
    print("jest więcej")
else:
    print("jest mniej")

print("\n")

for i in range(0,10):
    print(i)

q = ""
for char in laczone:
    if(char != "#"):
        q = q + char
    else:
        print(q)
        q = ""
print(q)