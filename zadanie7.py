import numpy as np

def normalizuj(u):
    return u / np.sqrt(np.sum(np.dot(u,u)))


def projekcja(u,v):
    proj = (np.dot(v,u)/np.dot(u,u))
    for i in range(len(u)):
        u[i] = u[i] * proj
    return u

macierz= [[1,0],[1,1],[0,1]]
QT = []
v = [macierz[x][0] for x in range(len(macierz))]
u = v
e = normalizuj(u)
QT.append(e)
for i in range(1, len(macierz)-1):
    v = [macierz[x][i] for x in range(len(macierz))]
    vproj = projekcja(u, v)
    u = [v[x] - vproj[x] for x in range(len(v))]
    e = normalizuj(u)
    QT.append(e)


"""
v1 = [macierz[x][0] for x in range(len(macierz))]
u1 = v1

e1 = normalizuj(u1)

v2 = [macierz[x][1] for x in range(len(macierz))] 
v2proj = projekcja(u1,v2)
u2 = [v2[x] - v2proj[x] for x in range(len(v2))]
e2 = normalizuj(u2)

"""
macierzA = np.matrix(A)
macierzQT = np.matrix(QT)

R = macierzQT*macierzA
print(R)



