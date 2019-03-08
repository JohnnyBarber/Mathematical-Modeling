# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
import numpy
from matplotlib.pyplot import *
from scipy import *


def sterling(n):
    x = math.factorial(n)/(math.sqrt(2*math.pi*n)*(n/math.e)**n)
    return x

t = linspace(1,12,12)

i = 0
y = zeros((1,12))
z = zeros((1,12))
while i < 12:
    y[0,i] = sterling(t[i])
    z[0,i] = 1
    i += 1

y = hstack(y)
z = hstack(z)

print()

figure(1,figsize=(10,5))
plot(t, y)
plot(t, z, '--')
xlabel('n',fontsize=18)
ylabel('Value of the function',fontsize=18)
legend([r'$\frac{n!}{\sqrt{2n\pi}(\frac{n}{e})^n}$','1'],loc = 0)