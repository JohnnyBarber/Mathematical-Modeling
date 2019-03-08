# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 14:15:02 2018

@author: Jiaqi Li
"""

from numpy import *
from numpy import cosh
from matplotlib.pyplot import *
from scipy import *
from scipy.optimize import fmin

#f----------------------------------------------------------
catenary = loadtxt('p6 data.txt',delimiter = ',')
x = catenary[:,0]
y = catenary[:,1]

def error(z):
    b = z[0]
    c = z[1]
    d = z[2]
    i = 0
    E = 0
    while i < len(y): 
        E += abs(y[i] - (b+c*cosh((x[i]-d)/c)))
        i += 1
    return E

z = array([-1000,700,775])
zbest = fmin(error,z,maxfun = 1000000000000)
print('fmin finds a minimum at approximately',zbest)

y_hat = zbest[0] + zbest[1]*cosh((x-zbest[2])/zbest[1])
figure(1,figsize = (10,8))
plot(x,y)
plot(x,y_hat)
legend(['data','estimate'],loc=0,framealpha=0)
xlabel('x',fontsize = 25)
ylabel('y',fontsize = 25)
title('Fitting Tilted Data Plot',fontsize = 25)

#g----------------------------------------------------------
theta = 0.044863
R = matrix([[cos(theta),sin(theta)],[-sin(theta),cos(theta)]])
Adjust = catenary.dot(R)
Y = Adjust[:,1]
X = Adjust[:,0]

def Error(Z):
    b = Z[0]
    c = Z[1]
    d = Z[2]
    i = 0
    E = 0
    while i < len(Y): 
        E += abs(Y[i] - (b+c*cosh((X[i]-d)/c)))
        i += 1
    return E

Z = array([-1000,700,775])
Zbest = fmin(Error,Z,maxfun = 1000000000000)
print('fmin finds a minimum at approximately',Zbest)

Y_hat = Zbest[0] + Zbest[1]*cosh((X-Zbest[2])/Zbest[1])
figure(2,figsize = (10,8))
plot(X,Y)
plot(X,Y_hat)
legend(['data','estimate'],loc=0,framealpha=0)
xlabel('x',fontsize = 25)
ylabel('y',fontsize = 25)
title('Fitting Corrected Data Plot',fontsize = 25)