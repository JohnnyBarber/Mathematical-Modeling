# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 20:45:08 2018

@author: Jiaqi Li
"""
from scipy import *
from scipy import linalg
from matplotlib.pyplot import *
import numpy
from decimal import Decimal
import math
from scipy.optimize import fmin

def f(x):
    return array([1,x,x**2,x**3])
A = zeros((13,4))
time = array([1,2.00055,3.00011,4.00014,4.98096,5.98096, 6.98096,7.98096,8.98096,9.98096,10.98096,11.98096,12.96699])
i = 0
while i <= 12:
    A[i,:] = f(time[i])
    i += 1
    
POP = loadtxt('data2.txt')[:,1]

k = linalg.solve(A.T.dot(A), A.T.dot(POP))
print('Following is parabolas')
print(k)

pop = A.dot(k.T)

t = linspace(1790, 1910, 13)

figure(1)
plot(t,pop)
plot(t,POP,'ro')
grid(True)
xlabel('YEAR')
ylabel('POPULATION')
title('POPULATION OF UNITED STATES')
legend(['$y=3827918+120808x+233193t^2+21801t^3$', 'Data'], loc=0, framealpha=0., fontsize = 9)

error = pop - POP
print('Following is parabolas error')
print(error)