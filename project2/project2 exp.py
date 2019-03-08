# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 20:52:52 2018

@author: Jiaqi Li
"""

from scipy import *
from scipy import integrate
import numpy
from matplotlib.pyplot import *

"Guinea has total death of 2536 during outbreak"
"Guinea has max infected of 3358 during outbreak"

##Simple model----------------------------------------------------
#death = loadtxt('partial death.txt')
#infected = loadtxt('partial infected.txt')
#N = 2479894
#lam = 0.8
#mu = 0.5
#theta = 0.8
#w = 0.9
#delta = 0.6
#beta = 0.5
#sigma = 0.2
#
#def system(X,t):
#    S = X[0]
#    M = X[1]
#    I = X[2]
#    H = X[3]
#    D = X[4]
#    v = beta*I/N
#    return array([-v*S-w*S, \
#                  theta*H+w*S+sigma*I, \
#                  v*S-lam*I-delta*I-sigma*I, \
#                  lam*I-theta*H-mu*H, \
#                  delta*I+mu*H])
#
#t = linspace(0,20,21)
#x0 = array([N,6,490,87,292])
#x_hat = integrate.odeint(system, x0, t)
#
#figure(1)
#plot(t,x_hat[:,2])
#plot(t,infected)
#ylabel('Infected')
#xlabel('Days')
#title('Eradication of Ebola (Infected)')
#
#figure(2)
#plot(t,x_hat[:,4])
#plot(t,death)
#ylabel('Death')
#xlabel('Days')
#title('Eradication of Ebola (Death)')

##Advanced model----------------------------------------------------
#death = loadtxt('death.txt')
#infected = loadtxt('infected.txt')
#N = 4000
#lam = 0.15
#mu = 0.01
#theta = 0.1
#delta = 0.107
#beta = 5
#sigma = 0.01
#w = 0.001
#
#def system(X,t):
#    S = X[0]
#    M = X[1]
#    I = X[2]
#    H = X[3]
#    D = X[4]
#    v = beta*I/(I+S)
#    return array([-v*S-w*S, \
#                  theta*H+sigma*I+w*S, \
#                  v*S-lam*I-delta*I-sigma*I, \
#                  lam*I-theta*H-mu*H, \
#                  delta*I+mu*H])
#
#t = linspace(0,90,91)
#x0 = array([N,6,648,87,430])
#x_hat = integrate.odeint(system, x0, t)
#t_full = linspace(0,24,25)
#x_hat_full = integrate.odeint(system, x0, t_full)
#x_simulation = array([N,0,1,0,0])
#x_hat_fullsimulation = integrate.odeint(system, x_simulation, t_full)
#
#figure(1)
#plot(t_full,x_hat_full[:,2])
#plot(t_full,x_hat_full[:,4])
#grid(axis='x', linestyle='-')
#grid(axis='y', linestyle='-')
#ylabel('Number of People')
#xlabel('Days')
#legend(['Infected','Death'],loc = 0, framealpha=1)
#title('Full Simulation of Eradication of Ebola (Infected)')
#
#figure(2)
#plot(t,x_hat[:,2])
#plot(t,infected)
#grid(axis='y', linestyle='-')
#ylabel('Infected')
#xlabel('Days')
#legend(['Simulation','Obsevered'],loc=0,framealpha=1)
#title('Eradication of Ebola (Infected)')
#
#figure(3)
#plot(t,x_hat[:,4])
#plot(t,death)
#grid(axis='y', linestyle='-')
#ylabel('Death')
#xlabel('Days')
#legend(['Simulation','Obsevered'],loc=0,framealpha=1)
#title('Eradication of Ebola (Death)')

##Developing model----------------------------------------------------
#death = loadtxt('death.txt')
#infected = loadtxt('infected.txt')
#N = 4000
#lam = 0.5
#mu = 0.1
#theta = 0.23
#delta = 0.107
#beta = 80
#sigma = 0.09
#k = 1
#a = 0.8
#r1 = 0.7
#r2 = 0.8
#fi = 0.9
#
#def system(X,t):
#    S = X[0]
#    M = X[1]
#    I = X[2]
#    H = X[3]
#    D = X[4]
#    R1 = X[5]
#    R2 = X[6]
#    v = beta*I/(I+S+R1+R2)
#    return array([-v*S, \
#                  theta*H+sigma*I-i*M, \
#                  v*S-lam*I-delta*I-sigma*I, \
#                  lam*I-theta*H-mu*H+r1*R1+r2*R2, \
#                  k*R2+mu*H, \
#                  delta*I-r1*R1-fi*R1, \
#                  fi*R1-r2*R2-k*R2])
#
#t = linspace(0,90,91)
#x0 = array([171,6,490,87,292,22,10])
#x_hat = integrate.odeint(system, x0, t)
#t_full = linspace(0,700,701)
#x_hat_full = integrate.odeint(system, x0, t_full)
#x_simulation = array([2,0,1,0,0,0,0])
#x_hat_fullsimulation = integrate.odeint(system, x_simulation, t_full)
#
#figure(1)
#plot(t,x_hat[:,2])
#plot(t,infected)
#ylabel('Infected')
#xlabel('Days')
#legend(['Simulation','Obsevered'],loc=0,framealpha=1)
#title('Eradication of Ebola (Infected)')
#
#figure(2)
#plot(t_full,x_hat_full[:,2])
#plot(t_full,x_hat_full[:,4])
#ylabel('Number of People')
#xlabel('Days')
#legend(['Infected','Death'],loc = 0, framealpha=1)
#title('Full Simulation of Eradication of Ebola (Infected)')
#
#figure(3)
#plot(t,x_hat[:,4])
#plot(t,death)
#ylabel('Death')
#xlabel('Days')
#legend(['Simulation','Obsevered'],loc=0,framealpha=1)
#title('Eradication of Ebola (Death)')

##Basic model good fit----------------------------------------------------
#death = loadtxt('death.txt')
#infected = loadtxt('infected.txt')
#
#N = 4000
#delta = 0.003
#beta = 0.08
#
#def system(X,t):
#    S = X[0]
#    I = X[1]
#    D = X[2]
#    v = beta*I/(I+S+D)
#    return array([-v*S, \
#                  v*S-delta*I, \
#                  delta*I])
#
#t = linspace(0,90,91)
#x0 = array([N,648,430])
#x_hat = integrate.odeint(system, x0, t)
#t_full = linspace(0,730,731)
#x_full = integrate.odeint(system,x0,t_full)
#
#figure(1,figsize=(10,8))
#plot(t_full,x_full[:,1])
#plot(t_full,x_full[:,2])
#ylabel('Number of People')
#xlabel('Days')
#grid(axis='x', linestyle='-')
#grid(axis='y', linestyle='-')
#legend(['Infected','Death'],loc=0,framealpha=1)
#title('Eradication of Ebola')
#
#figure(2,figsize=(10,8))
#plot(t,x_hat[:,1])
#plot(t,infected)
#ylabel('Infected')
#xlabel('Days')
#grid(axis='y', linestyle='-')
#legend(['Simulation','Obsevered'],loc=0,framealpha=1)
#title('Growth of Infected')
#
#figure(3,figsize=(10,8))
#plot(t,x_hat[:,2])
#plot(t,death)
#ylabel('Death')
#xlabel('Days')
#grid(axis='y', linestyle='-')
#legend(['Simulation','Obsevered'],loc=0,framealpha=1)
#title('Growth of Death')




##Advanced model----------------------------------------------------
#death = loadtxt('death.txt')
#infected = loadtxt('infected.txt')
#
#N = 4000
#lam = 0.15
#mu = 0.01
#theta = 0.1
#delta = 0.107
#beta = 5 #"every patient can infect 5 people before isolated, infection rate = 500%"
#sigma = 0.01
#w = 0.001
#
#def system(X,t):
#    S = X[0]
#    M = X[1]
#    I = X[2]
#    H = X[3]
#    D = X[4]
#    v = beta*I/(I+S+M)
#    return array([-v*S-w*S, \
#                  theta*H+sigma*I+w*S, \
#                  v*S-lam*I-delta*I-sigma*I, \
#                  lam*I-theta*H-mu*H, \
#                  delta*I+mu*H])
#
#t = linspace(0,90,91)
#x0 = array([N,6,648,87,430])
#x_hat = integrate.odeint(system, x0, t)
#t_full = linspace(0,24,25)
#x_hat_full = integrate.odeint(system, x0, t_full)
#x_simulation = array([N,0,1,0,0])
#x_hat_fullsimulation = integrate.odeint(system, x_simulation, t_full)
#
#figure(1,figsize=(10,8))
#plot(t_full,x_hat_full[:,2])
#plot(t_full,x_hat_full[:,4])
#grid(axis='x', linestyle='-')
#grid(axis='y', linestyle='-')
#ylabel('Number of People')
#xlabel('Days')
#legend(['Infected','Death'],loc = 0, framealpha=1)
#title('Full Simulation of Eradication of Ebola (Infected)')
#
#figure(2,figsize=(10,8))
#plot(t,x_hat[:,2])
#plot(t,infected)
#grid(axis='y', linestyle='-')
#ylabel('Infected')
#xlabel('Days')
#legend(['Simulation','Obsevered'],loc=0,framealpha=1)
#title('Growth of Infected')
#
#figure(3,figsize=(10,8))
#plot(t,x_hat[:,4])
#plot(t,death)
#grid(axis='y', linestyle='-')
#ylabel('Death')
#xlabel('Days')
#legend(['Simulation','Obsevered'],loc=0,framealpha=1)
#title('Growth of Death')


##Basic model----------------------------------------------------
#death = loadtxt('partial death.txt')
#infected = loadtxt('partial infected.txt')
#
#N = 3000
#delta = 0.021
#beta = 0.08
#
#def system(X,t):
#    S = X[0]
#    I = X[1]
#    D = X[2]
#    v = beta*I/(I+S+D)
#    return array([-v*S, \
#                  v*S-delta*I, \
#                  delta*I])
#
#t = linspace(0,20,21)
#x0 = array([N,490,292])
#x_hat = integrate.odeint(system, x0, t)
#t_full = linspace(0,365,366)
#x_full = integrate.odeint(system,x0,t_full)
#
#figure(1,figsize=(10,8))
#plot(t_hat,x_full[:,1])
#plot(t_hat,x_full[:,2])
#ylabel('Number of People')
#xlabel('Days')
#grid(axis='x', linestyle='-')
#grid(axis='y', linestyle='-')
#legend(['Infected','Death'],loc=0,framealpha=1)
#title('Eradication of Ebola')
#
#figure(2,figsize=(10,8))
#plot(t,x_hat[:,1])
#plot(t,infected)
#ylabel('Infected')
#xlabel('Days')
#grid(axis='y', linestyle='-')
#legend(['Simulation','Obsevered'],loc=0,framealpha=1)
#title('Growth of Infected')
#
#figure(3,figsize=(10,8))
#plot(t,x_hat[:,2])
#plot(t,death)
#ylabel('Death')
#xlabel('Days')
#grid(axis='y', linestyle='-')
#legend(['Simulation','Obsevered'],loc=0,framealpha=1)
#title('Growth of Death')


#Advanced model----------------------------------------------------
death = loadtxt('death.txt')
infected = loadtxt('infected.txt')

N = 8000
delta = 0.012
beta = 0.06
w = 0.000000001
sigma = 0.00001
lam = 0.05
theta = 0.002
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

figure(1,figsize=(10,8))
plot(t_full,x_full[:,0])
plot(t_full,x_full[:,1])
plot(t_full,x_full[:,2])
plot(t_full,x_full[:,3])
plot(t_full,x_full[:,4])
ylabel('Number of People',fontsize=20)
xlabel('Days',fontsize=20)
grid(axis='x', linestyle='-')
grid(axis='y', linestyle='-')
legend(['Susceptible','Infected','Death','Immune','Isolated'],loc=0,framealpha=1)
title('Eradication of Ebola Without Effective Medicine and Vaccine',fontsize=20)

figure(2,figsize=(10,8))
plot(t,x_hat[:,1])
plot(t,infected)
ylabel('Infected',fontsize=20)
xlabel('Days',fontsize=20)
grid(axis='y', linestyle='-')
legend(['Simulation','Obsevered'],loc=0,framealpha=1)
title('Growth of Infected',fontsize=20)

figure(3,figsize=(10,8))
plot(t,x_hat[:,2])
plot(t,death)
ylabel('Death',fontsize=20)
xlabel('Days',fontsize=20)
grid(axis='y', linestyle='-')
legend(['Simulation','Obsevered'],loc=0,framealpha=1)
title('Growth of Death',fontsize=20)