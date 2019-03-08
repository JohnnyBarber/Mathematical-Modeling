# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 01:00:13 2018

@author: Jiaqi Li
"""
from numpy import *
from scipy import integrate, cos, pi
from matplotlib.pyplot import *
from astropy.table import Table

r1 = 0.4
r0 = 0.15
m01 = 2.8 
dose = 500*2
V_blood = 5000. 

def f(X, t):
    return array([-(r0+m01)*X[0] + 100*(1 - cos(2*pi*t/6)), \
                  m01*X[0] - r1*X[1] ])

x0 = array([0, 0.])
t = linspace(0, 48, 1000)
x = integrate.odeint(f, x0, t)

figure(1)
plot(t, x[:,0], 'b-', linewidth=3)
ylabel('Stomach content (mg)')
xlabel('Time (hours from initial dose)')

figure(2)
plot(t, x[:,1]*1000./V_blood, 'g-', linewidth=3)
ylabel('Plasma concentration ($\mu$g/ml)')
xlabel('Time (hours from initial dose)')

row_data = [(x[624,0], x[624,1])]
t = Table(rows=row_data, names=('Acetaminophen in gut', 'Plasma concentration'))
print('\nThe following is the Acetaminophen in guy and body\n')
print(t)
