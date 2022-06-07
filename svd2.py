import numpy as np
import scipy.linalg as la

def svd(A):
    x,y = A.shape
    S = np.zeros(min(x,y))

    h = np.matmul(A, np.transpose(A))
    lamdaWartosc, lamdaWektor = la.eigh(h)
    index = lamdaWartosc.argsort()[::-1]
    lamdaWartosc = lamdaWartosc[index]
    lamdaWektor = lamdaWektor[:, index]
    U = lamdaWektor

    j = 0
    for i in lamdaWartosc:
        if j == S.size:
            break
        elif i >= 0:
            S[j] = np.sqrt(i)
            j += 1
    h = np.matmul(np.transpose(A), A)
    lamdaWartosc, lamdaWektor = la.eigh(h)
    index = lamdaWartosc.argsort()[::-1]
    lamdaWartosc = lamdaWartosc[index]
    lamdaWektor = lamdaWektor[:, index]
    V = np.transpose(lamdaWektor)

    for i in lamdaWartosc:
        if j == S.size:
            break
        elif i >= 0:
            S[j] = np.sqrt(i)
            j += 1

    S[::-1].sort()

    return U, S, V

a = np.array([[1,2,0],[2,0,2]])
x,y = a.shape
u,s,v= svd(a)


sprim = np.ones((x,y))
k = 0
for i in range(x):
    for j in range(y):
        if i != j:
            sprim[i][j] = 0
        else:
            sprim[k][k] = s[k]
            k += 1

print(u)
print(s)
print(v)
