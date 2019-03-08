# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 18:52:39 2018

@author: Jiaqi Li
"""
from scipy import *
from scipy import linalg
from matplotlib.pyplot import *
import numpy 

r = stringtxt[:,0]
W = stringtxt[:,1]

A = matrix([[1,1,1,1,1,1,1,1,1,1,1,1]])
A = A.T
b = matrix([[log(W[0])-r[0],log(W[1])-r[1],log(W[2])-r[2],log(W[3])-r[3],log(W[4])-r[4],log(W[5])-r[5],log(W[6])-r[6],log(W[7])-r[7],log(W[8])-r[8],log(W[9])-r[9],log(W[10])-r[10],log(W[11])-r[11]]])
b = b.T
Elaw = linalg.solve(A.T.dot(A), A.T.dot(b))

y = exp(Elaw[0])*exp(r)

figure(1)
plot(r, W, 'ro')
plot(r, y, 'bo')
legend(['Data','Fit'], loc=0, framealpha=0.)
xlabel('Revolution', fontsize=15)
ylabel('Weight (oz)', fontsize=15)

figure(2)
semilogy(r, y, 'ro-', r, W, 'bo-', linewidth=2)
legend(['Data','Fit'], loc=0, framealpha=0.)
xlabel('Revolution', fontsize=15)
ylabel('Weight (oz)', fontsize=15)

figure(3)
loglog(r, W, 'o', r, y, 'r-')
legend(['Data','Fit'], loc=0, framealpha=0.)
xlabel('Revolution', fontsize=15)
ylabel('Weight (oz)', fontsize=15)
