import numpy as np
import matplotlib.pyplot as plt
mpi = np.pi
print(mpi)
X = [2,4,-1,6]
n = len(X)

k=44100
Y= [0] * n
Zeta = [0]*n


def fu(X):
    n = len(X)
    dupsko = [0] * n

    for i in range(0,n):
        dupa = [0] * n
        for k in range(0,n):
            a = np.exp(-2j * np.pi * k * i / n)*X[k]
           # print a, k
            dupa[k] = dupa[k]+a

        #print sum(dupa), 'sum'
        dupsko[i] = sum(dupa)
    #print dupsko
    return dupsko
print fu(X)
#0
