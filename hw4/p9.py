# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 20:11:12 2018

@author: Jiaqi Li
"""
from scipy import *
import numpy
from matplotlib.pyplot import *
import math

def ErlangB(lam, r, N):
    j = 0
    R = 0
    while j < N+1:
        R = ((lam/r)**j)/math.factorial(j) + R
        j += 1
    f = 1/math.factorial(N)
    s = (lam/r)**N
    t = R**(-1)
    return (f*s*t)

x = [ErlangB(1,8,0),ErlangB(1,8,1),ErlangB(1,8,2),ErlangB(1,8,3),ErlangB(1,8,4),ErlangB(1,8,5)]
t = range(0,6)

print(x)

figure(1,figsize=(10,8))
plot(t,x)
xlabel('number of lines',fontsize = 25)
ylabel('maxed out %',fontsize = 25)


