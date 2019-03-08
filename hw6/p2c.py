# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 21:21:47 2018

@author: Jiaqi Li
"""

from pylab import *
from scipy import *
import numpy

def printbinarymatrix(A):
    m,n = A.shape
    s = '\n'.join([ \
            '|%s|'%''.join([( ' ' if i < 0.5 else '#' ) for i in row]) for row in A])
    #s = '\n'.join(['+%s+'%('-'*n),s,'+%s+'%('-'*n)])
    s = '\n'.join(['+%s+'%('-'*n),s,'+%s+'%('-'*n)])
    print(s)
    return

def calc_percolation_depth(A, i0=None):
    """
    Given an array A of {0,1}'s, find the farthest across the
    matrix we can walk on 0-entries, when
    using a von Neumann neighborhood, if we start
    at the left side in row i0.

    If i0 == None, return the maximum over all initial rows.
    """

    upper_bound = A.shape[1]
    if i0 == None:
        return max([calc_percolation_depth(A,i) for i in range(upper_bound)])

    neighbors = [(1,0), (-1,0), (0,1), (0,-1)]

    # to track which sites we have visited ...
    visited = 0*A
    def next(i,j):
        if i < 0 or i >= A.shape[0] or j < 0:
            return 0
        if j >= upper_bound:
            return upper_bound
        if visited[i,j] == 1:
            return 0
        visited[i,j] = 1
        if A[i,j] > 0.5:
            return j
        return max([next(i+dx,j+dy) for (dx,dy) in neighbors])
    return next(i0,0)


M5 = zeros(31)
M = zeros(1001)
p = 0.3
N = 5
i = 0
while p < 0.6001:
    print('p = %f' %p)
    n = 0
    for j in range(1001):
        A = floor(rand(N,N) + p)
        M[j] =calc_percolation_depth(A)
    for k in range(1001):
        if M[k] == N:
            n += 1
    M5[i] = n/1001
    p += 0.01
    i += 1
M5 = sorted(M5,reverse=True)

M10 = zeros(31)
M = zeros(1001)
p = 0.3
N = 10
i = 0
while p < 0.6001:
    print('p = %f' %p)
    n = 0
    for j in range(1001):
        A = floor(rand(N,N) + p)
        M[j] =calc_percolation_depth(A)
    for k in range(1001):
        if M[k] == N:
            n += 1
    M10[i] = n/1001
    p += 0.01
    i += 1
M10 = sorted(M10,reverse=True)

M20 = zeros(31)
M = zeros(1001)
p = 0.3
N = 20
i = 0
while p < 0.6001:
    print('p = %f' %p)
    n = 0
    for j in range(1001):
        A = floor(rand(N,N) + p)
        M[j] =calc_percolation_depth(A)
    for k in range(1001):
        if M[k] == N:
            n += 1
    M20[i] = n/1001
    p += 0.01
    i += 1
M20 = sorted(M20,reverse=True)

M50 = zeros(31)
M = zeros(1001)
p = 0.3
N = 50
i = 0
while p < 0.6001:
    print('p = %f' %p)
    n = 0
    for j in range(1001):
        A = floor(rand(N,N) + p)
        M[j] =calc_percolation_depth(A)
    for k in range(1001):
        if M[k] == N:
            n += 1
    M50[i] = n/1001
    p += 0.01
    i += 1
M50 = sorted(M50,reverse=True)

sys.setrecursionlimit(10000)
M100 = zeros(31)
M = zeros(1001)
p = 0.3
N = 100
i = 0
while p < 0.6001:
    print('p = %f' %p)
    n = 0
    for j in range(1001):
        print('j = %d' %j)
        A = floor(rand(N,N) + p)
        M[j] =calc_percolation_depth(A)
    for k in range(1001):
        if M[k] == N:
            n += 1
    M100[i] = n/1001
    p += 0.01
    i += 1
M100 = sorted(M100,reverse=True)
    
figure(2,figsize = (10,8))
plot(linspace(0.3,0.6,31),M5)
plot(linspace(0.3,0.6,31),M10)
plot(linspace(0.3,0.6,31),M20)
plot(linspace(0.3,0.6,31),M50)
plot(linspace(0.3,0.6,31),M100)
xlabel('Fill Fraction p',fontsize = 18)
ylabel('Fraction of Matrices that Percolate All The Way Through',fontsize = 15)
legend(['N=5','N=10','N=20','N=50','N=100'], loc=0, framealpha=1)