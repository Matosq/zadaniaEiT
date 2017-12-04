import math


class Complex:

    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

    def __abs__(self):
        return math.sqrt(self.re * self.re + self.im * self.im)

    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        return Complex(self.re - other.re, self.im - other.im)

    def __mul__(self, other):
        return Complex(self.re * other.re - self.im * other.im, self.re * other.im + other.re * self.im)

    def __truediv__(self, other):
        return Complex(((self.re*other.re+self.im*other.im)/(other.re*other.re+other.im*other.im))+((self.im*other.re-self.re*other.im)/(other.re*other.re+other.im*other.im)))

    def __str__(self):
        if self.im >= 0:
            return str(self.re)+"+"+str(self.im)+"j"
        else:
            return str(self.re)+str(self.im)+"j"


