# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 22:48:18 2018

@author: Jiaqi Li
"""

from scipy import *
from scipy import integrate
import numpy
from matplotlib.pyplot import *
from numpy import arcsin

G = 6.674e-11
M = 5.972e24
R = 6.378e6
m = 1200
k = 1e-04
B = 4.8e-5

def system(X,t):
    x = X[0]
    y = X[1]
    u = X[2]
    v = X[3]
    r = sqrt(x**2 + y**2)
    s = sqrt(u**2 + v**2)
    fG = G*M/r**3
    fD = (k/m)*exp(-B*(r-R))*s
    return array([u, v, -fG*x-fD*u, -fG*y-fD*v])

t = linspace(0,1900,1900)
x0 = array([0,100000+R,7850.,0.])
x_hat = integrate.odeint(system, x0, t)

#plot------------------------------------
x = linspace(-R,R,2*R+1)
y1 = sqrt(R**2 - x**2)
y2 = -sqrt(R**2 - x**2)

figure(1,figsize = (10,10))
plot(x_hat[:,0],x_hat[:,1],'r-')
plot(x,y1,'b')
plot(x,y2,'b')
xlim(-7000000,7000000)
ylim(-7000000,7000000)
legend(['capsule travel pass','earth surface'],loc = 0, framealpha=0)
xlabel('x coordinates',fontsize = 25)
ylabel('y coordinates',fontsize = 25)
title('Capsule Landing on Earth with (0,0) as Earth Core',fontsize = 25)

#c--------------------------------------
a = (R+100000)+(-x_hat[1899,1])
b = x_hat[1899,0]
c = sqrt(a**2+b**2)
arclength = arcsin(c/(2*R))*2*R
ratio = arclength/(2*pi*R)
longitude = round(ratio*360,2)
print(longitude)