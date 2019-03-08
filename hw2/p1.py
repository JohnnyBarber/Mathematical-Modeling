# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 01:18:06 2018

@author: Jiaqi Li
"""

from scipy import *
from scipy import linalg

thetas = array([65.197917, 66.404320, 87.040195, 141.356044]) # directly observed values
A = zeros((5,4))
A[0:4,0:4] = eye(4)
A[4,0:4] = 1
b = zeros((5,1))
b[0:4,0] = thetas
b[4] = 360.
W = zeros((5,5))
W[0:5,0:5] = eye(5); W[0,0] = 3; W[1,1] = 3; W[2,2] = 3; W[4,4] = 10**6
xbest = linalg.solve(A.T.dot(W).dot(A), A.T.dot(W).dot(b)) #
print("Corrections, in arc-seconds:\n")
print((xbest.T - thetas)*60**2)
