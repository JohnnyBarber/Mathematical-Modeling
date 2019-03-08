# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 14:25:55 2018

@author: Jiaqi Li
"""
from scipy import *
from scipy import integrate
from scipy.optimize import fmin
import numpy
from matplotlib.pyplot import *

"Guinea has total death of 2536 during outbreak"
"Guinea has max infected of 3804 during outbreak"

#Complex model----------------------------------------------------
death = loadtxt('death.txt')
infected = loadtxt('infected.txt')

N = 1.17351753e+03
delta = 2.38313977e-02
beta = 7.81041449e-02
w = -4.17197464e-02
sigma = -1.09207416e-02
lam = -5.49601368e-03
theta = -9.66760677e-02
mu = 3.44482230e-02

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
t_full = linspace(0,730,731)
x_full = integrate.odeint(system,x0,t_full)

figure(1,figsize=(10,8))
plot(t_full,x_full[:,0])
plot(t_full,x_full[:,1])
plot(t_full,x_full[:,2])
plot(t_full,x_full[:,3])
plot(t_full,x_full[:,4])
plot(t_full,x_full[:,5])
ylabel('Number of People',fontsize=20)
xlabel('Days',fontsize=20)
grid(axis='x', linestyle='-')
grid(axis='y', linestyle='-')
legend(['Susceptible','Infected','Death','Immune','Isolated'],loc=0,framealpha=1,fontsize=15)
title('Eradication of Ebola Without Effective Medicine and Vaccine',fontsize=20)

figure(2,figsize=(10,8))
plot(t,x_hat[:,5])
plot(t,infected)
ylabel('Infected',fontsize=20)
xlabel('Days',fontsize=20)
grid(axis='y', linestyle='-')
legend(['Simulation','Obsevered'],loc=0,framealpha=1,fontsize=15)
title('Growth of Infection',fontsize=20)

figure(3,figsize=(12,6))
plot(t,x_hat[:,2])
plot(t,death)
ylabel('Death',fontsize=20)
xlabel('Days',fontsize=20)
grid(axis='y', linestyle='-')
legend(['Simulation','Obsevered'],loc=0,framealpha=1,fontsize=20)
title('Growth of Death',fontsize=20)

#fmin----------------------------------------------------------------------
death = loadtxt('death.txt')
infected = loadtxt('infected.txt')

def system(X,t,delta,beta,w,sigma,lam,theta,mu):
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

def Error(para):
    N = para[0]
    delta = para[1]
    beta = para[2]
    w = para[3]
    sigma = para[4]
    lam = para[5]
    theta = para[6]
    mu = para[7]
    x0 = array([N,648,430,22,87,648])
    t = linspace(0,90,91)
    x = integrate.odeint(system, x0, t, args=(delta,beta,w,sigma,lam,theta,mu))
    err = sum(abs(x[:,5]-infected))+sum(abs(x[:,2]-death))
    return err

para = array([6300,0,0,0,0,0,0,0])
paraBest = fmin(Error,para,maxfun = 1000000000000)
    