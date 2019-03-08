# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 19:35:06 2018

@author: Jiaqi Li
"""

from numpy import *
from matplotlib.pyplot import *
from scipy import array, linspace, integrate

time = p4datatxt[:,0]
concentration = p4datatxt[:,1]

figure(1)
scatter(time,concentration)
xlabel("time", fontsize=15)
ylabel("concentration", fontsize=15)

#d----------------------------------------------------------------------------
t = linspace(0, 52, 53)

def ok(x, t, a, b):
    X = x[0]
    Y = x[1]
    return array([a-X+(X**2)*I, b-(X**2)*Y])

def Error2(data):
    n = 0
    E = 0
    X0 = data[0]
    Y0 = data[1]
    x0 = array([X0, Y0])
    a = data[2]
    b = data[3]
    x = integrate.odeint(ok, x0, t, args=(a, b))
    I = x[:, 0]
    S = x[:, 1]
    while n < death.shape[0]:
            E = E + (concentration[n] - x)**2
            n += 1
            return E

Z0 = array([1000,10000,0.001,0.25])
Zbest = fmin(Error2,Z0)
print('fmin finds a minimum at approximately',Zbest)

def main():
    # set up our initial conditions
    S0 = 8.19569017e+03
    I0 = 1.06202593e+03           
    x0 = array([I0, S0])
    
    # Parameters
    gama = 3.99778578e-01
    beta = 9.13222275e-08

    
    # choose the time's we'd like to know the approximate solution
    t = linspace(0, 52, 53)
    
    # and solve
    x = integrate.odeint(ok, x0, t, args=(gama, beta))
    I = x[:, 0]
    S = x[:, 1]
    
    #Plot I(t) and V (t) on separate subplots using ’semilogy()’
    figure(3)
    scatter(t, gama*I)
    scatter(week, death)
    xlabel("Weeks", fontsize=15)
    ylabel("New Infection Rate", fontsize=15)
    
    
main()