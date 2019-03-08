# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 19:37:24 2018

@author: Jiaqi Li
"""

from scipy import *
from scipy import linalg
import numpy
from matplotlib.pyplot import *

mesh = loadtxt('p5 data.txt', delimiter = ',')
F = mesh[0:8,5]/100
x = mesh[0:8,2]


b = matrix([log(-log(1 - F[0])),log(-log(1 - F[1])),log(-log(1 - F[2])),log(-log(1 - F[3])),log(-log(1 - F[4])),log(-log(1 - F[5])),log(-log(1 - F[6])),log(-log(1 - F[7]))])
b = b.T
A = matrix([[log(x[0]),log(x[1]),log(x[2]),log(x[3]),log(x[4]),log(x[5]),log(x[6]),log(x[7])],[-1,-1,-1,-1,-1,-1,-1,-1]])
A = A.T

W = linalg.solve(A.T.dot(A), A.T.dot(b))
n = W[0,0]
lam = e**(W[1,0]/n)
print(n,lam)

t = linspace(min(x),max(x),100)
fit = 1-e**(-(t/lam)**n)

figure()
scatter(x,F)
plot(t,fit,'r')
xlabel('particle size (mm)')
ylabel('F(x)')
legend(['Weibull','Data'],loc=0, framealpha=0.)
title('Fit Weibull Distribution to the Data of Rock Size')