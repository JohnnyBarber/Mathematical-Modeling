# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 15:51:50 2018

@author: Jiaqi Li
"""
from scipy import *
from scipy import linalg
from matplotlib.pyplot import *
import numpy
from decimal import Decimal
import math
from scipy.optimize import fmin
from scipy.optimize import fsolve


#parabolas----------------------------------------------------------------------------------------------------
def f(x):
    return array([1,x,x**2,x**3])
A = zeros((13,4))
time = array([-4.98096,-3.98041,-2.98085,-1.98082,-1,0,1,2,3,4,5,6,6.98603])
i = 0
while i <= 12:
    A[i,:] = f(time[i])
    i += 1
    
POP = loadtxt('data.txt')[:,1]

k = linalg.solve(A.T.dot(A), A.T.dot(POP))
print('Following is parabolas')
print(k)

pop = k.dot(A.T)

t = linspace(1790, 1910, 13)

figure(1)
plot(t,pop)
plot(t,POP,'ro')
grid(True)
xlabel('YEAR')
ylabel('POPULATION')
title('POPULATION OF UNITED STATES')
legend(['$y=3827918+120808x+233193t^2+21801t^3$', 'Data'], loc=0, framealpha=0., fontsize = 9)

error = pop - POP
print('Following is parabolas error')
print(error)

#log-----------------------------------------------------------------------------------------------------------------------
def f(x):
    return array([1,x,x**2,math.log(x,10)])
A = zeros((13,4))
time = array([1,2.00055,3.00011,4.00014,4.98096,5.98096, 6.98096,7.98096,8.98096,9.98096,10.98096,11.98096,12.96699])
i = 0
while i <= 12:
    A[i,:] = f(time[i])
    i += 1

k = linalg.solve(A.T.dot(A), A.T.dot(POP))
print('Following is log')
print(k)

pop = A.dot(k.T)

t = linspace(1790, 1910, 13)

figure(2)
plot(t,pop)
plot(t,POP,'ro')
grid(True)
xlabel('YEAR')
ylabel('POPULATION')
title('POPULATION OF UNITED STATES')
legend(['$y=9072386-6223289t+841752x^2+19524417log x$', 'Data'], loc=0, framealpha=0., fontsize = 9)

error = pop - POP
print('Following is log error')
print(error)


#logistic----------------------------------------------------------------------------
def logistic(p):
    y = p[1]/(exp(-p[0]*time)+p[2])
    Err = linalg.norm(POP/1000 - y,2)
    return Err

p0 = array([0.03,3000,0.01])
Lbest = fmin(logistic,p0, maxfun=1000)
print('Following is logistic')
print(Lbest)

y = 2938.28415/(exp(-0.313232819*time)+0.0148457044)*1000

figure(3)
plot(t,y)
plot(t,POP,'ro')
grid(True)
xlabel('YEAR')
ylabel('POPULATION')
title('POPULATION OF UNITED STATES')
legend(['$y = 2938.28415/(e^{-0.313232819x}+0.0148457044)*1000$', 'Data'], loc=0, framealpha=0., fontsize = 9)

error = y - POP
print('Following is logistic error')
print(error)

#fsolve-------------------------------------------------------------------------------------------------
def myfun (q):
    F = empty((3))
    F[0]= q[1]/(exp(-q[0])+q[2])-3929
    F[1] = q[1]/(exp(-q[0]*6.98096)+q[2])-23192
    F[2] = q[1]/(exp(-q[0]*12.96699)+q[2])-91972
    return F

p0 = array([0.03,3000,0.01])
Lbest1 = fsolve(myfun,p0)
print(Lbest1)

y1 = Lbest1[1]/(exp(-Lbest1[0]*time)+Lbest1[2])*1000

figure(4)
plot(t,y1)
plot(t,POP,'ro')
grid(True)
#xticks(arange(min(time), max(time), 1000))
xlabel('YEAR')
ylabel('POPULATION')
title('POPULATION OF UNITED STATES')
legend(['$y = 2927.3953/(e^{-0.314441x}+0.014877)*1000$', 'Data'], loc=0, framealpha=0., fontsize = 9)



error = y1-POP
print(error)


#typo-----------------------------------------------------------------------------------------------
y = 2930.3009/(exp(-0.03133395*time)+0.014854)*1000

figure(5)
plot(t,y)
plot(t,POP,'ro')
grid(True)
xlabel('YEAR')
ylabel('POPULATION')
title('POPULATION OF UNITED STATES')
legend(['$y = 2938.28415/(e^{-0.0313232819x}+0.0148457044)*1000$', 'Data'], loc=0, framealpha=0., fontsize = 9)

#exp-----------------------------------------------------------------------------------------------------------------------
logb = zeros((13,1))
logA = zeros((13,2))
POPe = zeros((13,1))

i = 0
while i <= 12:
    logb[i] = log(POP[i])
    logA[i,0] = 1
    logA[i,1] = time[i]
    i += 1

r = linalg.solve(logA.T.dot(logA), logA.T.dot(logb))
N0 = exp(r[0])
print('Following is exp')
print(N0,r[1])

i = 0
while i <= 12:
    POPe[i] = exp(r[0])*exp(r[1]*time[i])
    i += 1

t = linspace(1790, 1910, 13)

figure(6)
plot(t,POPe)
plot(t,POP,'ro')
grid(True)
xlabel('YEAR')
ylabel('POPULATION')
title('POPULATION OF UNITED STATES')
legend(['$y=3296063.279e^{0.26782946x}$', 'Data'], loc=0, framealpha=0., fontsize = 9)

error = POPe - POP
print('Following is exp error')
print(error)
