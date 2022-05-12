import numpy as np
import matplotlib.pyplot as plt

def funkcja(x, B0, B1):
    return B1*x+B0

punkty = [[2,1],[5,2],[7,3],[8,3]]

x = [punkty[i][0] for i in range(len(punkty))]
y = [punkty[i][1] for i in range(len(punkty))]

mY = np.matrix(y).transpose()

matrixX = [[1, punkty[i][0]] for i in range(len(punkty))]
matrixX = np.matrix(matrixX)

matrixXT = matrixX.transpose()

mXmXT = matrixXT * matrixX

mXmXTinverse = mXmXT**-1

mXtY = matrixXT * mY


result = mXmXTinverse*mXtY

f = []
for i in range(9):
    f.append(funkcja(i, float(result[0][0]), float(result[1][0])))   


plt.plot(f)

plt.scatter(x, y)
plt.show()

