
import numpy as np
import matplotlib.pyplot as plt
from copy import copy
# u1 = v1
# e1 = u1/||u1||
# u2 = v2 - proju1(v2)
# e2 = u2/||u2||
#R = Q^T A


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
# arrayU.append(vectors[0])

# arrayE.append(normalize(arrayU[0]))

for i in range(len(vectors)):
    v = vectors[i]
    suma = sumProj(arrayU, v, i)
    arrayU.append( v- suma )

arrayE = []

for i in range(len(arrayU)):
    arrayE.append(normalize(arrayU[i]))

# v2 = [A[x][1] for x in range(len(A))] 
# v2proj = proj(u1,v2)
# u2 = [v2[x] - v2proj[x] for x in range(len(v2))]
# e2 = normalize(u2)


matrixA = np.matrix(A)
matrixQT = np.matrix(arrayE)
matrixQ = np.transpose(matrixQT)
# matrixQT = matrixQT.transpose()
R = matrixQT*matrixA

np.set_printoptions(suppress=True)
print(R)

A1 = matrixQT * matrixA * matrixQ
print(A1)