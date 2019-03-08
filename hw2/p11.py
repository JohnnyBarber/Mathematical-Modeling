# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 21:04:18 2018

@author: Jiaqi Li
"""

from scipy import array, linspace
from scipy import integrate
from matplotlib.pyplot import *


def ok(x, t, sigma, c, p, epsilon):
    I = x[0]
    V = x[1]
    S = array([c*sigma*V/p-sigma*I, (1-epsilon)*p*I-c*V])
    return S

def main():
    # set up our initial conditions
    I0 = 9.2*10**4
    V0 = 10**6
    x0 = array([I0, V0])
    
    # Parameters
    c = 4.6
    sigma = 0.35
    epsilon = 0.95
    p = 50
    
    # choose the time's we'd like to know the approximate solution
    t = linspace(0, 14, 100)
    
    # and solve
    x = integrate.odeint(ok, x0, t, args=(sigma,c,p,epsilon))
    
    #Plot I(t) and V (t) on separate subplots using ’semilogy()’
    figure(1)    
    subplot(2,1,1)
    semilogy(t, x[:,0], 'b-')
    ylabel('infected cells')
    
    subplot(2,1,2)
    semilogy(t, x[:,1], 'r-')
    xlabel('hours')
    ylabel('virus')
    
    figure(2)
    plot(x[:,0], x[:,1], 'k-')
    xlabel('infected cells')
    ylabel('virus')
    
main()