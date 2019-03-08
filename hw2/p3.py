# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 01:57:42 2018

@author: Jiaqi Li
"""

from scipy import *
from scipy import linalg
from matplotlib.pyplot import *
import numpy 
from astropy.table import Table

deer = deertxt
t = Table(rows=deer, names=('Mean Body Mass', 'Mean Antler Mass'))
print(t)

bw = deer[:,0]
aw = deer[:,1]

A = matrix([[1,1,1,1,1,1,1,1,1,1],[log(bw[0]),log(bw[1]),log(bw[2]),log(bw[3]),log(bw[4]),log(bw[5]),log(bw[6]),log(bw[7]),log(bw[8]),log(bw[9])]])
A = A.T
b = matrix([[log(aw[0]),log(aw[1]),log(aw[2]),log(aw[3]),log(aw[4]),log(aw[5]),log(aw[6]),log(aw[7]),log(aw[8]),log(aw[9])]])
b = b.T
Plaw = linalg.solve(A.T.dot(A), A.T.dot(b))
k = exp(Plaw[0,0])
y = k*bw**(Plaw[1,0])

#I found that the Arrhenius Law fit the data well
A2 = matrix([[1,1,1,1,1,1,1,1,1,1],[1/bw[0],1/bw[1],1/bw[2],1/bw[3],1/bw[4],1/bw[5],1/bw[6],1/bw[7],1/bw[8],1/bw[9]]])
A2 = A2.T
b2 = matrix([[log(aw[0]),log(aw[1]),log(aw[2]),log(aw[3]),log(aw[4]),log(aw[5]),log(aw[6]),log(aw[7]),log(aw[8]),log(aw[9])]])
b2 = b2.T
Alaw = linalg.solve(A2.T.dot(A2), A2.T.dot(b2))

y2 = exp(Alaw[0,0]+Alaw[1,0]/bw)

print('\n  fitted parameter values')
print(y)

figure(1)
plot(bw, aw, 'bo')
plot(bw, y, 'ro-')
legend(['Data','Best fit (Power Law)'], loc=0, framealpha=0.)
xlabel('Body Weigth (kg)', fontsize=15)
ylabel('Antler Weight (kg)', fontsize=15)

figure(2)
plot(bw, aw, 'bo')
plot(bw, y2, 'ro-')
legend(['Data','Arrhenious Law'], loc=0, framealpha=0.)
xlabel('Body Weigth (kg)', fontsize=15)
ylabel('Antler Weight (kg)', fontsize=15)

