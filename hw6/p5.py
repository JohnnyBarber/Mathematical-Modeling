# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 17:11:56 2018

@author: Jiaqi Li
"""

from scipy import *
import scipy.integrate
from matplotlib.pyplot import *
from numpy import *

def system(X,t):
    #The differential equations are:
    #
    #    dtheta
    #    --     = u = -e^(theta)*x + constant
    #    dx
    #
    #    du
    #    --     = -e^(theta)
    #    dx
    u = X[0]
    theta = X[1]
    return array([u, -exp(theta)])

x = linspace(0,2.5,101)
m = [-1,0,1,2,3,4]

def M(m):
    #I do not know about the initial condition for u
    #Temporary set u = 0 at m = -1,0,1,2,3,4
    x0 = array([0,m])
    x_hat = scipy.integrate.odeint(system, x0, x)
    return x_hat

figure(1, figsize = (10,8))
plot(x,M(m[0])[:,1])
plot(x,M(m[1])[:,1])
plot(x,M(m[2])[:,1])
plot(x,M(m[3])[:,1])
plot(x,M(m[4])[:,1])
plot(x,M(m[5])[:,1])
xlabel('Cross-Section length x',fontsize = 20)
ylabel('Temperature At Cross-Section x',fontsize = 20)
legend(['m=-1','m=0','m=1','m=2','m=3','m=4'],loc=0,framealpha=1)

for i in range(101):
    if (M(m[5])[i,1] < 1.10 and M(m[5])[i,1] > 1):
        n = i
        print('At m=4 : %d' %(n+1))

L = 2*n*2.5/100

print(L)

