# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from scipy import array, linspace
from scipy import integrate
from matplotlib.pyplot import *
import numpy

A = bowditchtxt 
At = numpy.transpose(A)
b = conttxt
x = numpy.linalg.inv(At.dot(A)).dot(At).dot(-b)
print('\nvalue of d, t, p, n, i')
print(x)

dtpni = numpy.transpose(x)
answer = A.dot(dtpni)-b

book = [0.595, 0.537, 0.693, 1.154, 0.352]
y = A.dot(numpy.transpose(book))-b

figure(1)
t = linspace(1,56,56)
plot(t,answer,'bx-',t,y,'rx-',linewidth=1)
legend(['Best fit', 'Estimated'], loc=0, framealpha=0)
xlabel('euqation number', fontsize=15)
ylabel('errors', fontsize=15)

