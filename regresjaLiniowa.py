"""punkty
2 1
5 2
7 3
8 3

beta0 2/7
beta1 5/14"""
import numpy as np

def obliczBeta(x):
    xTranspose = np.transpose(x)
    firstHalf = xTranspose * x
    inverted = np.linalg.inv(firstHalf)