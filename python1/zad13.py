import numpy
import random

random.seed()

wymiar=8
#Generowanie macierzy
A=numpy.zeros((wymiar,wymiar), dtype=numpy.int16)
B=numpy.zeros((wymiar,wymiar), dtype=numpy.int16)
Iloczyn=numpy.zeros((wymiar,wymiar), dtype=numpy.int16)

for x in range(wymiar):
    for i in range(wymiar):
        A[x][i]=random.random()*10
print(A)

for x in range(wymiar):
    for i in range(wymiar):
        B[x][i]=random.random()*10
print(B)

#Iloczyn macierzy
for x in range(wymiar):
    for i in range(wymiar):
        for j in range(wymiar):
            Iloczyn[x][i]=Iloczyn[x][i]+A[x][j]*B[j][i]


print(Iloczyn)

