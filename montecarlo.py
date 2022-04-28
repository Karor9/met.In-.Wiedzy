import numpy as np
import matplotlib.pyplot as plt
import random as random

def prostokat(x, y):
    return x*y

def f(x):
    return x

def makeADot(xk, xp, maxVal):
    x = random.uniform(xk, xp)
    y = random.uniform(0, maxVal)
    return (x,y)


def program(xp, xk, liczbaKropek=10000):
    #xp = float(input("Podaj start: "))
    #xk = float(input("Podaj koneic: "))
    wynik = []
    for i in range(int(xk+5)):
        wynik.append(f(i))   
    plt.plot(wynik)
    plt.axvline(xp, color='red', ls='--')
    plt.axvline(xk, color='red', ls='--')
    maxVal = -float('inf')
    for i in range(xp, xk+1):
        if(f(i) > maxVal):
            maxVal = f(i)
    under = 0
    for i in range(liczbaKropek):
        dot = makeADot(xp, xk, maxVal*2)
        if(dot[1] < f(dot[0])):
            under += 1
            plt.plot(dot[0], dot[1], 'ro', color='b')
        else:
            plt.plot(dot[0], dot[1], 'ro', color='y')
    pole = prostokat(xk-xp, maxVal*2)
    plt.show()
    wynik = pole * (under/liczbaKropek)
    print(wynik)

program(0, 1, 5000)