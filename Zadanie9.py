import numpy as np
import sys
from copy import copy


def proj(u, v):
    temp = u
    cos = (np.dot(v,temp)/np.dot(temp,temp))
    for i in range(len(temp)):
        temp[i] = temp[i]* cos
    return temp

def sumProj(tabU, vector, liczbaProjekcji):
    result =[]
    for j in range(len(vector)):
        result.append(0)
    
    for i in range(liczbaProjekcji):
        u = copy(tabU[i])
        temp = proj(u, vector)
        result = result+temp
    return result

def normalize(u):
    dot = np.sqrt(np.sum(np.dot(u,u)))
    result = u / dot
    return result


A = [
            [2,0,1],
            [0,1,0],
            [1,2,0]
]

tempVectors = np.matrix(A)
tempVectors = np.transpose(tempVectors)
vectors = np.asarray(np.squeeze(tempVectors))

vectors = vectors.astype('float64')


arrayU = []

for i in range(len(vectors)):
    v = vectors[i]
    suma = sumProj(arrayU, v, i)
    arrayU.append( v- suma )

arrayE = []

for i in range(len(arrayU)):
    arrayE.append(normalize(arrayU[i]))


matrixA = np.matrix(A)
matrixQT = np.matrix(arrayE)
matrixQ = np.transpose(matrixQT)
R = matrixQT*matrixA

np.set_printoptions(suppress=True)

A1 = matrixQT * matrixA * matrixQ
print(A1)


a = [
    [1,2,7,4,8,1],
    [4,7,1,0,5,5],
    [0,4,1,8,33,8],
    [1,2,9,1,9,4],
    [0,3,7,3,6,0]
]

b=[[4,2,0], [4,2,0]]

def gaussJoran(a):
    if not type(a) is list:
        a = a.tolist()
    n = len(a)
    b = np.zeros(n)

    for i in range(n):
        print(a)
        if a[i][i] == 0.0:
            sys.exit('Dzielenie przez 0')
            
        for j in range(n):
            if i != j:
                r = a[j][i]/a[i][i]

                for k in range(n+1):
                    a[j][k] = a[j][k] - r * a[i][k]


    for i in range(n):
        b[i] = a[i][n]/a[i][i]

    l = []
    for i in range(n):
        l.append(b[i])
    return l

print(gaussJoran(b))