# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 15:30:27 2018

@author: Jiaqi Li
"""
from scipy import floor, cumsum, array, linspace, cos, pi, rand, loadtxt
from scipy.stats import poisson
from scipy.optimize import fminbound
from matplotlib.pyplot import *
import time

def norm(x,e):
    return sum(abs(x)**e)**(1./e)

def rndBinomial(p, n, replicas=1):
    if replicas == 1:
        return int(sum(floor(rand(n) + p)))
    trials = [ rndBinomial(p,n) for i in xrange(replicas)]
    return trials

def main():
    # load data
    particle = loadtxt('p3 data.txt',delimiter = ',')
    x, y = map(array, zip(*particle))
    N = sum(y)

    Y = y*1./N
    # distribution fitting
    def fit_error(L_guess):
        # calculate the distance between our guess and the data
        z = poisson.pmf(x, L_guess)
        return norm(Y-z, 1)/norm(Y,1) # can be any p-norm
    L_best = fminbound(fit_error, 1e-5, 6-1e-5)
    err_best = fit_error(L_best)
    print("Best fit: L = %f,  error = %f"%(L_best, fit_error(L_best)))

    # generate data for animation
    F = [ (p, fit_error(p)) for p in linspace(1e-4,6-1e-4, 137) ]
    u, v = map(array, zip(*F))

    # draw basic figure
    fig = figure()

    subplot(2,1,2)
    plot(u, v, 'b-')
    #plot( L_best, fit_error(L_best), 'ko')
    marker_fit_error = plot( u[2], v[2], 'ro').pop()
    ylim(0,1)
    xlabel('Poisson intensity $\lambda$')

    subplot(2,1,1)
    plot(x, y, 'ko')
    z = poisson.pmf(x, L_best)
    width = .3
    xw = x-width*.5
    bar_ob = bar(xw, z*N, width, color='r')
    ttl = 'N = %d observations, $\lambda_{best} = %.3f$, $Err_{best} = %1.2g$'
    title(ttl%(N, L_best, err_best))
    ylabel('Number of times observed')
    xlabel('Number of successes')
    xlim(-0.5,max(x)+.5)
    ylim(0,max(y)*1.2)

    show(block=False)

main()