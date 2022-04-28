import random
import numpy as np
import matplotlib.pyplot as plt

# prostokatne
def prostokat(x, y):
    return x*y

def f(x):
    return x

def findMax(x1, x2):
    if x1 > x2:
        return x1
    else:
        return x2

def prostokatne(xp, xk, liczbaPodzialow=5):

    wynik = []
    for i in range(xk+5):
        wynik.append(f(i))   

    plt.plot(wynik)
    plt.axvline(xp, color='red', ls='--')
    plt.axvline(xk, color='red', ls='--')

    podzialy = [xk, xp]
    for i in range(liczbaPodzialow):
        podzialy.sort()
        for j in range(len(podzialy)-1):
            x = (podzialy[j] + podzialy[j+1])/2
            podzialy.append(x)
        podzialy.sort()
    sumaPola = 0
    for i in range(len(podzialy)-1):
        sumaPola += prostokat(podzialy[i+1]-podzialy[i], findMax(f(podzialy[i]), f(podzialy[i+1])))
    for x in range(len(podzialy)):
        if(x + 1 < len(podzialy)):
            plt.hlines(xmin=podzialy[x], xmax=podzialy[x+1], y=f(podzialy[x+1]), colors='green')
            max = findMax(f(podzialy[x]), f(podzialy[x+1]))
        plt.vlines(podzialy[x], ymin=0, ymax=max, colors='green')

    plt.show()
    return sumaPola



print(prostokatne(0, 1, 10))