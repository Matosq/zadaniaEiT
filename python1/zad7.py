import math


def fun(a,b,c):
    delta=b*b-4*a*c
    if delta >= 0:
        pDelta=math.sqrt(delta)

    if delta > 0:
        print("Funkcja ma dwa pierwiastki: ")
        x1=(-b+pDelta)/(2*a)
        x2=(-b-pDelta)/(2*a)
        print(x1,x2)

    elif delta == 0:
        print("Funkcja ma jeden pierwiastek: ")
        x=(-b)/(2*a)
        print(x)

    else:
        print("Funkcja nie ma pierwiastkow: ")


    return


fun(1,6,10)
