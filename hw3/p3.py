# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 18:37:29 2018

@author: Jiaqi Li
"""

from numpy import *
from matplotlib.pyplot import *
from scipy import array, linspace, integrate
from scipy.optimize import fmin

week = p3datatxt[:,0]
death = p3datatxt[:,1]

figure(1)
scatter(week,death)
xlabel("Weeks", fontsize=15)
ylabel("Deaths", fontsize=15)

#b-------------------------------------------------------

def ok(x, t, gama, beta):
    I = x[1]
    S = x[0]
    return array([-beta*S*I, beta*S*I-gama*I])

def main():
    # set up our initial conditions
    S0 = 9000
    I0 = 30
    x0 = array([S0, I0])
    
    # Parameters
    gama = 0.01
    beta = 3*10**(-5)

    t = linspace(0, 52, 53)
    
    # and solve
    x = integrate.odeint(ok, x0, t, args=(gama, beta))
    I = x[:, 0]
    S = x[:, 1]
    
    figure(1)
    scatter(week,death)
    xlabel("Weeks", fontsize=15)
    ylabel("Deaths", fontsize=15)
    
    plot(t, beta*S*I)
    xlabel("Weeks", fontsize=15)
    ylabel("New Infection Rate", fontsize=15)
    
    def Error1(data, beta):
        n = 0
        E = 0
        y = data[:,1]
        x = data[:,0]
        while n < y.shape[0]:
            E = E + abs(y[n] - beta*S[n]*I[n])
            n += 1
            return E

    print('Error1 is',Error1(p3datatxt,beta))

    def Error2(data,beta):
        n = 0
        E = 0
        y = data[:,1]
        x = data[:,0]
        while n < y.shape[0]:
            E = E + (y[n] - beta*S[n]*I[n])**2
            n += 1
            return E
    
    print('Error2 is',Error2(p3datatxt,beta))
    
main()

#d----------------------------------------------------------------------------
t = linspace(0, 52, 53)

def ok(x, t, gama, beta):
    I = x[1]
    S = x[0]
    return array([-beta*S*I, beta*S*I-gama*I])

def Error2(data):
    n = 0
    E = 0
    I0 = data[1]
    S0 = data[0]
    x0 = array([I0, S0])
    beta = data[2]
    gama = data[3]
    x = integrate.odeint(ok, x0, t, args=(gama, beta))
    I = x[:, 0]
    S = x[:, 1]
    while n < death.shape[0]:
            E = E + (death[n]/week[n] - beta*S[n]*I[n])**2
            n += 1
            return E

Z0 = array([10000,1000,0,0])
Zbest = fmin(Error2,Z0)
print('fmin finds a minimum at approximately',Zbest)

def main():
    # set up our initial conditions
    S0 = 9.99954959e+02
    I0 = 1.04438221e+04             
    x0 = array([I0, S0])
    
    # Parameters
    gama = -1.24947152e-04
    beta = 7.61127097e-08

    
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
    
    
    