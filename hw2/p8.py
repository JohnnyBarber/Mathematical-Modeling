# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 01:16:54 2018

@author: Jiaqi Li
"""

from numpy import *
from scipy import integrate,cos,pi
from matplotlib.pyplot import *

r1 = 0.4
dose = 325
V_blood = 5000. # 5 liters approximately
mmg_per_mg = 1000.

def model1(X, t):
    return array([ 100*(1 - cos(2*pi*t/6)) - r1*X[0] ])

x0 = array([0.])
t = linspace(0, 48, 1000)
x = integrate.odeint(model1, x0, t)

figure(1)
plot(t, x[:,0], 'b-', linewidth=3)
ylabel('Dosage', fontsize=15)
xlabel('Time (hours from initial dose)', fontsize=15)

figure(2)
plot(t, x[:,0]*mmg_per_mg/V_blood, 'g-', linewidth=3, label='Model')
ylabel('Dosage x(t)', fontsize=15)
xlabel('Time (hours from initial dose)', fontsize=15)
tight_layout()
