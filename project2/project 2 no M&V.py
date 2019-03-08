# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 18:08:54 2018
One basic model and two complex models are included.
The model with medicine and vaccine are seperated from another transcript.
This transcript focuses on fitting data and full cycle simulation of Ebola outbreak.

@author: Jiaqi Li
"""

from scipy import *
from scipy import integrate
import numpy
from matplotlib.pyplot import *

"Guinea has total death of 2536 during outbreak"
"Guinea has max infected of 3804 during outbreak"

#Basic model----------------------------------------------------
death = loadtxt('death.txt')
infected = loadtxt('infected.txt')

N = 4000
delta = 0.006
beta = 0.08

def system(X,t):
    S = X[0]
    I = X[1]
    D = X[2]
    v = beta*I/(I+S+D)
    return array([-v*S, \
                  v*S-delta*I, \
                  delta*I])

t = linspace(0,90,91)
x0 = array([N,648,430])
x_hat = integrate.odeint(system, x0, t)
t_full = linspace(0,730,731)
x_full = integrate.odeint(system,x0,t_full)

figure(1,figsize=(10,8))
plot(t_full,x_full[:,1])
plot(t_full,x_full[:,2])
ylabel('Number of People')
xlabel('Days')
grid(axis='x', linestyle='-')
grid(axis='y', linestyle='-')
legend(['Infected','Death'],loc=0,framealpha=1)
title('Eradication of Ebola')

figure(2,figsize=(10,8))
plot(t,x_hat[:,1])
plot(t,infected)
ylabel('Infected')
xlabel('Days')
grid(axis='y', linestyle='-')
legend(['Simulation','Obsevered'],loc=0,framealpha=1)
title('Growth of Infected')

figure(3,figsize=(10,8))
plot(t,x_hat[:,2])
plot(t,death)
ylabel('Death')
xlabel('Days')
grid(axis='y', linestyle='-')
legend(['Simulation','Obsevered'],loc=0,framealpha=1)
title('Growth of Death')


#Complex model----------------------------------------------------
death = loadtxt('death.txt')
infected = loadtxt('infected.txt')

N = 6300
delta = 0.003
beta = 0.06
w = 0.000000001
sigma = 0.00001
lam = 0.01
theta = 0.004
mu = 0.001

def system(X,t):
    S = X[0]
    I = X[1]
    D = X[2]
    M = X[3]
    H = X[4]
    v = beta*(I+D)/(I+S+D)
    return array([-v*S-w*S, \
                  v*S-delta*I-lam*I-sigma*I, \
                  delta*I+mu*H, \
                  w*S+sigma*I+theta*H, \
                  lam*I-mu*H-theta*H])

t = linspace(0,90,91)
x0 = array([N,648,430,22,87])
x_hat = integrate.odeint(system, x0, t)
t_full = linspace(0,730,731)
x_full = integrate.odeint(system,x0,t_full)

figure(4,figsize=(10,8))
plot(t_full,x_full[:,0])
plot(t_full,x_full[:,1])
plot(t_full,x_full[:,2])
plot(t_full,x_full[:,3])
plot(t_full,x_full[:,4])
ylabel('Number of People',fontsize=20)
xlabel('Days',fontsize=20)
grid(axis='x', linestyle='-')
grid(axis='y', linestyle='-')
legend(['Susceptible','Infected','Death','Immune','Isolated'],loc=0,framealpha=1,fontsize=15)
title('Eradication of Ebola Without Effective Medicine and Vaccine',fontsize=20)

figure(5,figsize=(10,8))
plot(t,x_hat[:,1])
plot(t,infected)
ylabel('Infected',fontsize=20)
xlabel('Days',fontsize=20)
grid(axis='y', linestyle='-')
legend(['Simulation','Obsevered'],loc=0,framealpha=1,fontsize=15)
title('Growth of Infection',fontsize=20)

figure(6,figsize=(12,6))
plot(t,x_hat[:,2])
plot(t,death)
ylabel('Death',fontsize=20)
xlabel('Days',fontsize=20)
grid(axis='y', linestyle='-')
legend(['Simulation','Obsevered'],loc=0,framealpha=1,fontsize=20)
title('Growth of Death',fontsize=20)


#Full-Simulatoin model----------------------------------------------------
death = loadtxt('death.txt')
infected = loadtxt('infected.txt')

N = 6300
delta = 0.003
beta = 0.06
w = 0.000000001
sigma = 0.00001
lam = 0.01
theta = 0.004
mu = 0.001

def system(X,t):
    S = X[0]
    I = X[1]
    D = X[2]
    M = X[3]
    H = X[4]
    v = beta*(I+D)/(I+S+D)
    return array([-v*S-w*S, \
                  v*S-delta*I-lam*I-sigma*I, \
                  delta*I+mu*H, \
                  w*S+sigma*I+theta*H, \
                  lam*I-mu*H-theta*H])

t = linspace(0,90,91)
x0 = array([N,1,0,0,0])
x_hat = integrate.odeint(system, x0, t)
t_full = linspace(0,730,731)
x_full = integrate.odeint(system,x0,t_full)

figure(7,figsize=(12,6))
plot(t_full,x_full[:,0])
plot(t_full,x_full[:,1])
plot(t_full,x_full[:,2])
plot(t_full,x_full[:,3])
plot(t_full,x_full[:,4])
ylabel('Number of People',fontsize=20)
xlabel('Days',fontsize=20)
grid(axis='x', linestyle='-')
grid(axis='y', linestyle='-')
legend(['Susceptible','Infected','Death','Immune','Isolated'],loc=0,framealpha=1,fontsize=20)
title('Eradication of Ebola Without Effective Medicine and Vaccine (Full Cycle)',fontsize=18)
