import numpy
import random
import scipy

random.seed()
wymiar=int(random.random()*10)
A=numpy.zeros((wymiar,wymiar), dtype=numpy.int16)

for x in range(wymiar):
    for i in range(wymiar):
        A[x][i]=int(random.random()*10)
print(A)


print("Wyznacznik wynosi: ",numpy.linalg.det(A))
