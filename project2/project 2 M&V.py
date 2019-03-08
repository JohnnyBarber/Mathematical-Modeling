# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 18:33:44 2018
This transcript focuses on simulation with medicine and vaccine available for Ebola

@author: Jiaqi Li
"""

from scipy import *
from scipy import integrate
import numpy
from matplotlib.pyplot import *

"Guinea has total death of 2536 during outbreak"
"Guinea has max infected of 3804 during outbreak"

#Full-Simulatoin model with medicine&vaccine----------------------------------------------------
death = loadtxt('death.txt')
infected = loadtxt('infected.txt')

N = 6300
delta = 0.003
beta = 0.06
w1 = 0.01
w2 = 0.03
w3 = 0.09
sigma = 0.00001
lam = 0.01
theta = 0.6
mu = 0.001

def system1(X,t):
    S = X[0]
    I = X[1]
    D = X[2]
    M = X[3]
    H = X[4]
    v = beta*(I+D)/(I+S+D)
    return array([-v*S-w1*S, \
                  v*S-delta*I-lam*I-sigma*I, \
                  delta*I+mu*H, \
                  w1*S+sigma*I+theta*H, \
                  lam*I-mu*H-theta*H])

x0 = array([N,1,0,0,0])
t_full = linspace(0,730,731)
x_full_1 = integrate.odeint(system1,x0,t_full)    
    
def system2(X,t):
    S = X[0]
    I = X[1]
    D = X[2]
    M = X[3]
    H = X[4]
    v = beta*(I+D)/(I+S+D)
    return array([-v*S-w2*S, \
                  v*S-delta*I-lam*I-sigma*I, \
                  delta*I+mu*H, \
                  w2*S+sigma*I+theta*H, \
                  lam*I-mu*H-theta*H])    

x0 = array([N,1,0,0,0])
t_full = linspace(0,730,731)
x_full_2 = integrate.odeint(system2,x0,t_full)
    
def system3(X,t):
    S = X[0]
    I = X[1]
    D = X[2]
    M = X[3]
    H = X[4]
    v = beta*(I+D)/(I+S+D)
    return array([-v*S-w3*S, \
                  v*S-delta*I-lam*I-sigma*I, \
                  delta*I+mu*H, \
                  w3*S+sigma*I+theta*H, \
                  lam*I-mu*H-theta*H])
    
x0 = array([N,1,0,0,0])
t_full = linspace(0,730,731)
x_full_3 = integrate.odeint(system3,x0,t_full)

figure(1,figsize=(10,8))
plot(t_full,x_full_1[:,1])
plot(t_full,x_full_2[:,1])
plot(t_full,x_full_3[:,1])
ylabel('Infected',fontsize=20)
xlabel('Days',fontsize=20)
grid(axis='x', linestyle='-')
grid(axis='y', linestyle='-')
legend(['w=0.01','w=0.03','w=0.09'],loc=0,framealpha=1,fontsize=20)
title('Growth of Infection With Vaccine & Medicine (Full Cycle)',fontsize=20)

figure(2,figsize=(10,8))
plot(t_full,x_full_1[:,2])
plot(t_full,x_full_2[:,2])
plot(t_full,x_full_3[:,2])
ylabel('Death',fontsize=20)
xlabel('Days',fontsize=20)
grid(axis='x', linestyle='-')
grid(axis='y', linestyle='-')
legend(['w=0.01','w=0.03','w=0.09'],loc=0,framealpha=1,fontsize=20)
title('Growth of Death With Vaccine & Medicine (Full Cycle)',fontsize=20)

figure(3,figsize=(10,8))
plot(t_full,x_full_1[:,3])
plot(t_full,x_full_2[:,3])
plot(t_full,x_full_3[:,3])
ylabel('Immune',fontsize=20)
xlabel('Days',fontsize=20)
grid(axis='x', linestyle='-')
grid(axis='y', linestyle='-')
legend(['w=0.01','w=0.03','w=0.09'],loc=0,framealpha=1,fontsize=20)
title('Growth of Immune With Vaccine & Medicine (Full Cycle)',fontsize=20)

figure(4,figsize=(12,6))
plot(t_full,x_full_2[:,0])
plot(t_full,x_full_2[:,1])
plot(t_full,x_full_2[:,2])
plot(t_full,x_full_2[:,3])
plot(t_full,x_full_2[:,4])
ylabel('Number of People',fontsize=20)
xlabel('Days',fontsize=20)
grid(axis='x', linestyle='-')
grid(axis='y', linestyle='-')
legend(['Susceptible','Infected','Death','Immune','Isolated'],loc=0,framealpha=1,fontsize=20)
title('Eradication of Ebola With Effective Medicine and Vaccine (Full Cycle)',fontsize=18)

figure(5,figsize=(12,6))
plot(t_full,x_full_3[:,0])
plot(t_full,x_full_3[:,1])
plot(t_full,x_full_3[:,2])
plot(t_full,x_full_3[:,3])
plot(t_full,x_full_3[:,4])
ylabel('Number of People',fontsize=20)
xlabel('Days',fontsize=20)
grid(axis='x', linestyle='-')
grid(axis='y', linestyle='-')
legend(['Susceptible','Infected','Death','Immune','Isolated'],loc=0,framealpha=1,fontsize=20)
title('Eradication of Ebola With Effective Medicine and Vaccine (Full Cycle)',fontsize=18)