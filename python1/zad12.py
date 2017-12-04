import numpy
import random

random.seed()

#Generowanie macierzy A
A=numpy.zeros((128,128), dtype=numpy.int16)
for x in range(128):
    for i in range(128):
        A[x][i]=int(random.random()*20)
print(A)

#Generowanie macierzy B
B=numpy.zeros((128,128), dtype=numpy.int16)
for x in range(128):
    for i in range(128):
        B[x][i]=int(random.random()*20)
print(B)


#Sumowanie macierzy
Suma=numpy.zeros((128,128),dtype=numpy.int16)
for x in range(128):
    for i in range(128):
        Suma[x][i]=A[x][i]+B[x][i]
print(Suma)
