# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 18:08:54 2018

This transcript focuses on fitting data and full cycle simulation of Ebola outbreak.

@author: Jiaqi Li
"""

from scipy import *
from scipy import integrate
import numpy
from matplotlib.pyplot import *
from scipy.optimize import fmin

"Guinea has total death of 2536 during outbreak"
"Guinea has max infected of 3804 during outbreak"

#Basic model----------------------------------------------------
death = loadtxt('death.txt')
infected = loadtxt('infected.txt')
date = loadtxt('Date.txt').tolist()

N = 3156
delta = 0.0225
beta = 0.0676

def system(X,t):
    S = X[0]
    I = X[1]
    D = X[2]
    T = X[3]
    v = beta*(I+D)/(I+S+D)
    return array([-v*S, \
                  v*S-delta*I, \
                  delta*I, \
                  v*S])

t = linspace(0,90,91)
x0 = array([N,648,430,648])
x_hat = integrate.odeint(system, x0, t)
t_full = linspace(0,717,718)
x_full = integrate.odeint(system,x0,t_full)

figure(1,figsize=(10,8))
plot(t_full,x_full[:,0])
plot(t_full,x_full[:,1])
plot(t_full,x_full[:,2])
plot(t_full,x_full[:,3])
ylabel('Number of People')
xlabel('Days')
grid(axis='x', linestyle='-')
grid(axis='y', linestyle='-')
legend(['Susceptible','Infected','Death','Total Infected'],loc=0,framealpha=1)
title('Eradication of Ebola')

figure(2,figsize=(10,8))
plot(date,x_hat[:,3])
plot(date,infected)
ylabel('Infected')
xlabel('Days')
grid(axis='y', linestyle='-')
legend(['Simulation','Obsevered'],loc=0,framealpha=1)
title('Growth of Total Infected')

figure(3,figsize=(10,8))
plot(date,x_hat[:,2])
plot(date,death)
ylabel('Death')
xlabel('Days')
grid(axis='y', linestyle='-')
legend(['Simulation','Obsevered'],loc=0,framealpha=1)
title('Growth of Total Death')

#fmin-----------------------------------------------------------
def system(X,t,delta, beta):
    S = X[0]
    I = X[1]
    D = X[2]
    T = X[3]
    v = beta*(I+D)/(I+S+D)
    return array([-v*S, \
                  v*S-delta*I, \
                  delta*I, \
                  v*S])
def Error(para):
    N = para[0]
    delta = para[1]
    beta = para[2]
    t = linspace(0,90,91)
    x0 = array([N,648,430,648])
    x_hat = integrate.odeint(system, x0, t, args=(delta,beta))
    err = sum(abs(x_hat[:,3]-infected))+sum(abs(x_hat[:,2]-death))
    return err
    
para = [N,0,0]
paraBest = fmin(Error,para)

#Complex model----------------------------------------------------
death = loadtxt('death.txt')
infected = loadtxt('infected.txt')
date = loadtxt('Date.txt').tolist()

N = 3156
delta = 0.07
beta = 0.08
w = 0.000000001
sigma = 0.00001
lam = 0.06
theta = 0.01
mu = 0.001

def system(X,t):
    S = X[0]
    I = X[1]
    D = X[2]
    M = X[3]
    H = X[4]
    T = X[5]
    v = beta*(I+D)/(I+S+D)
    return array([-v*S-w*S, \
                  v*S-delta*I-lam*I-sigma*I, \
                  delta*I+mu*H, \
                  w*S+sigma*I+theta*H, \
                  lam*I-mu*H-theta*H, \
                  v*S])

t = linspace(0,90,91)
x0 = array([N,648,430,22,87,648])
x_hat = integrate.odeint(system, x0, t)
t_full = linspace(0,717,718)
x_full = integrate.odeint(system,x0,t_full)

figure(4,figsize=(12,6))
plot(t_full,x_full[:,0])
plot(t_full,x_full[:,1])
plot(t_full,x_full[:,2])
plot(t_full,x_full[:,3])
plot(t_full,x_full[:,4])
plot(t_full,x_full[:,5],dashes=[5, 5], label='Using the dashes parameter')
ylabel('Number of People',fontsize=20)
xlabel('Days',fontsize=20)
grid(axis='x', linestyle='-')
grid(axis='y', linestyle='-')
legend(['Susceptible','Infected','Death','Immune','Isolated','Total Infected'],loc=1,framealpha=1,fontsize=15)
title('Eradication of Ebola Without Effective Medicine and Vaccine',fontsize=20)

figure(5,figsize=(10,8))
plot(date,x_hat[:,5])
plot(date,infected)
ylabel('Infected',fontsize=20)
xlabel('Days',fontsize=20)
grid(axis='y', linestyle='-')
legend(['Simulation','Obsevered'],loc=0,framealpha=1,fontsize=15)
title('Growth of Total Infection',fontsize=20)

figure(6,figsize=(10,8))
plot(date,x_hat[:,2])
plot(date,death)
ylabel('Death',fontsize=20)
xlabel('Days',fontsize=20)
grid(axis='y', linestyle='-')
legend(['Simulation','Obsevered'],loc=0,framealpha=1,fontsize=20)
title('Growth of Total Death',fontsize=20)


#Full-Simulatoin model----------------------------------------------------
death = loadtxt('death.txt')
infected = loadtxt('infected.txt')
date = loadtxt('Date.txt').tolist()

N = 3804
delta = 0.07
beta = 0.08
w = 0.000000001
sigma = 0.00001
lam = 0.06
theta = 0.01
mu = 0.001

def system(X,t):
    S = X[0]
    I = X[1]
    D = X[2]
    M = X[3]
    H = X[4]
    T = X[5]
    v = beta*(I+D)/(I+S+D)
    return array([-v*S-w*S, \
                  v*S-delta*I-lam*I-sigma*I, \
                  delta*I+mu*H, \
                  w*S+sigma*I+theta*H, \
                  lam*I-mu*H-theta*H, \
                  v*S])

x0 = array([N,1,0,0,0,1])
t_full = linspace(0,730,731)
x_full = integrate.odeint(system,x0,t_full)

figure(7,figsize=(12,6))
plot(t_full,x_full[:,0])
plot(t_full,x_full[:,1])
plot(t_full,x_full[:,2])
plot(t_full,x_full[:,3])
plot(t_full,x_full[:,4])
plot(t_full,x_full[:,5],dashes=[5, 5], label='Using the dashes parameter')
ylabel('Number of People',fontsize=20)
xlabel('Days',fontsize=20)
grid(axis='x', linestyle='-')
grid(axis='y', linestyle='-')
legend(['Susceptible','Infected','Death','Immune','Isolated','Total Infected'],loc=0,framealpha=1,fontsize=12)
title('Eradication of Ebola Without Effective Medicine and Vaccine (Full Cycle)',fontsize=18)


#M&V available model----------------------------------------------------
death = loadtxt('death.txt')
infected = loadtxt('infected.txt')
date = loadtxt('Date.txt').tolist()

N = 3804
delta = 0.07
beta = 0.08
w1 = 0.01
w2 = 0.03
w3 = 0.09
sigma = 0.00001
lam = 0.06
theta = 0.6
mu = 0.001

x0 = array([N,1,0,0,0,1])
t_full = linspace(0,299,300)

def system1(X,t):
    S = X[0]
    I = X[1]
    D = X[2]
    M = X[3]
    H = X[4]
    T = X[5]
    v = beta*(I+D)/(I+S+D)
    return array([-v*S-w1*S, \
                  v*S-delta*I-lam*I-sigma*I, \
                  delta*I+mu*H, \
                  w1*S+sigma*I+theta*H, \
                  lam*I-mu*H-theta*H, \
                  v*S])

x_full_1 = integrate.odeint(system1,x0,t_full)    
    
def system2(X,t):
    S = X[0]
    I = X[1]
    D = X[2]
    M = X[3]
    H = X[4]
    T = X[5]
    v = beta*(I+D)/(I+S+D)
    return array([-v*S-w2*S, \
                  v*S-delta*I-lam*I-sigma*I, \
                  delta*I+mu*H, \
                  w2*S+sigma*I+theta*H, \
                  lam*I-mu*H-theta*H, \
                  v*S])    

x_full_2 = integrate.odeint(system2,x0,t_full)
    
def system3(X,t):
    S = X[0]
    I = X[1]
    D = X[2]
    M = X[3]
    H = X[4]
    T = X[5]
    v = beta*(I+D)/(I+S+D)
    return array([-v*S-w3*S, \
                  v*S-delta*I-lam*I-sigma*I, \
                  delta*I+mu*H, \
                  w3*S+sigma*I+theta*H, \
                  lam*I-mu*H-theta*H, \
                  v*S])
    
x_full_3 = integrate.odeint(system3,x0,t_full)

figure(8,figsize=(6,8))
plot(t_full,x_full_1[:,1])
plot(t_full,x_full_2[:,1])
plot(t_full,x_full_3[:,1])
ylabel('Infected',fontsize=20)
xlabel('Days',fontsize=20)
grid(axis='x', linestyle='-')
grid(axis='y', linestyle='-')
legend(['w=0.01','w=0.03','w=0.09'],loc=1,framealpha=1,fontsize=20)
title('Infection With Vaccine & Medicine',fontsize=20)

figure(9,figsize=(6,8))
plot(t_full,x_full_1[:,2])
plot(t_full,x_full_2[:,2])
plot(t_full,x_full_3[:,2])
ylabel('Death',fontsize=20)
xlabel('Days',fontsize=20)
grid(axis='x', linestyle='-')
grid(axis='y', linestyle='-')
legend(['w=0.01','w=0.03','w=0.09'],loc=0,framealpha=1,fontsize=20)
title('Total Death With Vaccine & Medicine',fontsize=20)

figure(10,figsize=(6,8))
plot(t_full,x_full_1[:,3])
plot(t_full,x_full_2[:,3])
plot(t_full,x_full_3[:,3])
ylabel('Immune',fontsize=20)
xlabel('Days',fontsize=20)
grid(axis='x', linestyle='-')
grid(axis='y', linestyle='-')
legend(['w=0.01','w=0.03','w=0.09'],loc=0,framealpha=1,fontsize=20)
title('Total Immune With Vaccine & Medicine',fontsize=20)

figure(11,figsize=(6,8))
plot(t_full,x_full_1[:,5])
plot(t_full,x_full_2[:,5])
plot(t_full,x_full_3[:,5])
ylabel('Total Infected',fontsize=20)
xlabel('Days',fontsize=20)
grid(axis='x', linestyle='-')
grid(axis='y', linestyle='-')
legend(['w=0.01','w=0.03','w=0.09'],loc=0,framealpha=1,fontsize=20)
title('Total Infection With Vaccine & Medicine',fontsize=20)

figure(12,figsize=(12,6))
plot(t_full,x_full_3[:,0])
plot(t_full,x_full_3[:,1])
plot(t_full,x_full_3[:,2])
plot(t_full,x_full_3[:,3])
plot(t_full,x_full_3[:,4])
plot(t_full,x_full_3[:,5],dashes=[5, 5], label='Using the dashes parameter')
ylabel('Number of People',fontsize=20)
xlabel('Days',fontsize=20)
grid(axis='x', linestyle='-')
grid(axis='y', linestyle='-')
legend(['Susceptible','Infected','Death','Immune','Isolated','Total Infected'],loc=0,framealpha=1,fontsize=12)
title('Eradication of Ebola With Effective Medicine and Vaccine (Full Cycle)',fontsize=20)