# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 17:13:32 2018

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

def p3():
    p = 0.3 
    N = 40
    A = floor(rand(N,N) + p)
    return A
def p4():
    p = 0.4 
    N = 40
    A = floor(rand(N,N) + p)
    return A
def p45():
    p = 0.45 
    N = 40
    A = floor(rand(N,N) + p)
    return A
def p5():
    p = 0.5
    N = 40
    A = floor(rand(N,N) + p)
    return A
def p6():
    p = 0.6 
    N = 40
    A = floor(rand(N,N) + p)
    return A

#The following code is for the map:
#assert set([0,1]) == set(map(int,A.flatten()))
#print("Here we have a %dx%d matrix, with fill fraction %f"%(N,N,p))
#printbinarymatrix(A.T)
#print("If we start on the top, how far toward the bottom can we move on blanks?")
#for i in range(N):
#    d = calc_percolation_depth(A,i)
#    print("From column %2d, we go %2d steps down"%(i,d))
#print("Max depth: ", calc_percolation_depth(A))
#print("Now, double-check with your own eyes.  Are all of these correct?")


M3 = zeros(1000)
for i in range(1000):
    print('i = %d' %i)
    M3[i] = calc_percolation_depth(p3())
M3.sort()

M4 = zeros(1000)
for i in range(1000):
    print('i = %d' %i)
    M4[i] = calc_percolation_depth(p4())
M4.sort()

M45 = zeros(1000)
for i in range(1000):
    print('i = %d' %i)
    M45[i] = calc_percolation_depth(p45())
M45.sort()

M5 = zeros(1000)
for i in range(1000):
    print('i = %d' %i)
    M5[i] = calc_percolation_depth(p5())
M5.sort()

M6 = zeros(1000)
for i in range(1000):
    print('i = %d' %i)
    M6[i] = calc_percolation_depth(p6())
M6.sort()

g3 = zeros(41)
x = linspace(0,40,41)
j,k = 0,0
while k < 41:
    print('x = %d' %k)
    for i in range(1000):
        if k == M3[i]:
            j += 1
    g3[k] = j/1000
    k += 1

g4 = zeros(41)
x = linspace(0,40,41)
j,k = 0,0
while k < 41:
    print('x = %d' %k)
    for i in range(1000):
        if k == M4[i]:
            j += 1
    g4[k] = j/1000
    k += 1
    
g45 = zeros(41)
x = linspace(0,40,41)
j,k = 0,0
while k < 41:
    print('x = %d' %k)
    for i in range(1000):
        if k == M45[i]:
            j += 1
    g45[k] = j/1000
    k += 1
    
g5 = zeros(41)
x = linspace(0,40,41)
j,k = 0,0
while k < 41:
    print('x = %d' %k)
    for i in range(1000):
        if k == M5[i]:
            j += 1
    g5[k] = j/1000
    k += 1
    
g6 = zeros(41)
x = linspace(0,40,41)
j,k = 0,0
while k < 41:
    print('x = %d' %k)
    for i in range(1000):
        if k == M6[i]:
            j += 1
    g6[k] = j/1000
    k += 1
    
figure(2,figsize = (12,9))
plot(g3, 'o-')
plot(g4, 'o-')
plot(g45, 'o-')
plot(g5, 'o-')
plot(g6, 'o-')
xlabel('Percolation Depth x',fontsize = 20)
ylabel('Fraction of Matrices with Percolation Depth <= x',fontsize = 20)
legend(['p=0.3','p=0.4','p=0.45','p=0.5','p=0.6'], loc=0, framealpha=1)