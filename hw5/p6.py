# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 10:25:38 2018

@author: Jiaqi Li
"""

from scipy import *
from scipy import linalg
import numpy
from matplotlib.pyplot import *

#a--------------------------------------------------
chain = loadtxt('p6 data.txt',delimiter=',')
x = chain[:,0]
y = chain[:,1]
figure(1,figsize = (10,8))
plot(x,y)
xlabel('x coordinates',fontsize = 25)
ylabel('y coordinates',fontsize = 25)
title('Plot of Extract Data Point',fontsize = 25)

#b--------------------------------------------------
A = zeros((12621,3))
A[:,0] = 1; A[:,1] = x; A[:,2] = x**2
b = y
law = linalg.solve(A.T.dot(A), A.T.dot(b))
print(law)

#c--------------------------------------------------
figure(2,figsize = (10,8))

subplot(2,1,1)
plot(x,y)
plot(x,A.dot(law))
ylabel('y',fontsize = 25)
legend(['observed','estimated'],loc = 0, framealpha=0.)

subplot(2,1,2)
plot(x,y-A.dot(law))
ylabel('residuals',fontsize = 25)
xlabel('x',fontsize = 25)

#d--------------------------------------------------
'not random'

#e--------------------------------------------------
E = sum(abs(y-A.dot(law)))
print(E)
