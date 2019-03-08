# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 15:46:11 2018

@author: Jiaqi Li
"""

from scipy import *
from scipy import linalg
from matplotlib.pyplot import *
import numpy
from decimal import Decimal
import math
from scipy.optimize import fmin

time = array([1,2.00055,3.00011,4.00014,4.98096,5.98096, 6.98096,7.98096,8.98096,9.98096,10.98096,11.98096,12.96699])

POP = loadtxt('data.txt')[:,1]

t = linspace(1790, 1910, 13)

def logistic(p):
    y = p[1]/(exp(-p[0]*time)+p[2])
    Err = linalg.norm(POP/1000 - y,2)
    return Err

p0 = array([0.03,3000,0.01])
Lbest = fmin(logistic,p0, maxfun=1000)
print(Lbest)

y = 2938.28415/(exp(-0.313232819*time)+0.0148457044)*1000

#major = arange(1790,1910, 10)

figure(1)
plot(t,y)
plot(t,POP,'ro')
grid(True)
#xticks(arange(min(time), max(time), 1000))
xlabel('YEAR')
ylabel('POPULATION')
title('POPULATION OF UNITED STATES')
legend(['$y = 2938.28415/(e^{-0.313232819x}+0.0148457044)*1000$'], loc=6, framealpha=0., fontsize = 6)

#typo-----------------------------------------------------------------------------------------------
y = 2930.3009/(exp(-0.03133395*time)+0.014854)*1000

figure(2)
plot(t,y)
plot(t,POP,'ro')
grid(True)
xlabel('YEAR')
ylabel('POPULATION')
title('POPULATION OF UNITED STATES')
legend(['$y = 2938.28415/(e^{-0.0313232819x}+0.0148457044)*1000$'], loc=6, framealpha=0., fontsize = 6)
