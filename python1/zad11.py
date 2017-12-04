import math


A=[1,2,12,4]
B=[2,4,2,8]

def iloczynSkalarny(a,b):
    if len(a) != len(b):
        print("Dlugosci wektorow sa rozne. Nie mozna policzyc iloczynu")
        return 0
    L=[]
    for i in range(len(a)):
        L.append(a[i]*b[i])

    return L








print(iloczynSkalarny(A,B))
