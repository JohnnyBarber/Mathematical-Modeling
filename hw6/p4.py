# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 12:58:54 2018

@author: Jiaqi Li
"""

from scipy import sqrt
import scipy.integrate
from matplotlib.pyplot import *
from numpy import *
from numpy.linalg.linalg import norm


def stream_plot(F, domain, **kwargs):
    dx, dy = domain[0][2]*1j, domain[1][2]*1j
    Y, X = mgrid[domain[1][1]:domain[1][0]:dy, domain[0][0]:domain[0][1]:dx]
    U = 0*X
    V = 0*Y
    s = Y.shape
    for x in range(s[0]):
        for y in range(s[1]):
            vec = F(X[x,y], Y[x,y])
            U[x,y] = vec[0]
            V[x,y] = vec[1]
    #UV = vectorize(F, otypes=[numpy.ndarray, numpy.ndarray])(X, Y)
    return streamplot(X[0,:], Y[:,0], U, V, **kwargs)

def vector_field(X, t):
    # The differenti equations are
    #
    #    dtheta
    #    --     = s
    #    dt
    #
    #    ds
    #    -- = -sin(theta)
    #    dt
    s = X[0]
    theta = X[1]
    return array([s,  -sin(theta)])


def main():
    s = 0.1
    theta = pi/4

    F = lambda x,y : vector_field((x,y), 0)
    figure(1,figsize = (10,8))
    stream_plot(F, ((-10,10,100),(-12,18,150)))
    show()

main()