import numpy as np
from torch import atanh

def normalize(u):
    dot = np.sqrt(np.sum(np.dot(u,u)))
    result = u / dot
    l = []
    for x in result:
        l.append(round(x, 3))
    return l

def makeOrto(a):
    n = len(a)

    at = [[0 for x in range(n)] for y in range(n)]

    r = [[0 for x in range(n)] for y in range(n)]

    for i in range(0, n) :
        for j in range(0, n) :
            at[i][j] = a[j][i]

    r = np.dot(at,a)
    return r

def normalizeMatrix(a):
    n = len(a)
    r = [[0 for x in range(n)] for y in range(n)]
    for i in range(0, n):
        r[i] = normalize(a[i])
    return r
    
def isOrtonormal(a):
    n = len(a)
    for i in range(0, n):
        for j in range(0, n):
            if i == j:
                if a[i][j] != 1:
                    return False
            else:
                if a[i][j] != 0:
                    return False
    return True


def isOrthogonal(a):
    n = len(a)

    for i in range(0, n) :
        for j in range(0, n) :
            if (i != j and a[i][j] != 0) :
                return False
            if (i == j and a[i][j] != 1) :
                return False
    
    return True

def changeBase(b, a, w):
    if isOrtonormal(a):
        bt = np.transpose(b)
        result = np.matmul(bt, w)
        return result
    else:
        bt = np.transpose(b)
        result = bt * a * w
        return result

A = [
    [1,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0],
    [0,0,1,0,0,0,0,0],
    [0,0,0,1,0,0,0,0],
    [0,0,0,0,1,0,0,0],
    [0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,1]
]

BT = [
    [1,1,1,1,1,1,1,1],
    [1,1,1,1,-1,-1,-1,-1],
    [1,1,-1,-1,0,0,0,0],
    [0,0,0,0,1,1,-1,-1],
    [1,-1,0,0,0,0,0,0],
    [0,0,1,-1,0,0,0,0],
    [0,0,0,0,1,-1,0,0],
    [0,0,0,0,0,0,1,-1]
]

B = np.transpose(BT)

ortoB = makeOrto(B)
normB = normalizeMatrix(ortoB)
wektor = [8, 6, 2, 3, 4, 6, 6, 5]
wektor = np.transpose(wektor)
print(changeBase(B, A, wektor))