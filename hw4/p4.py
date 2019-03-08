# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 16:08:27 2018

@author: Jiaqi Li
"""
#!/usr/bin/python

from pylab import *
import csv
from scipy.stats import norm as gaussian
from scipy.optimize import fmin


def main():
    height = loadtxt('p4 data.txt', delimiter=',')
    x = height[:,0]
    y = height[:,1]
    m = height.shape[0]

    z = []
    for i in range(m):
        z += [x[i]]*int(y[i])
    n = len(z)
    z = array(z)

    # slow, inaccurate method
    def fit_likelihood(a):
        return -sum(log(gaussian.pdf((z-a[0])/a[1])/a[1]))
    objective = fit_likelihood
    a = [64.,6.]
    result = fmin(objective, a)
    mu, sigma = result[0], result[1]
    print( "Numerical Parameter fits: ", (mu, sigma))
    print( "\tAverage Log-Likelihood: ", fit_likelihood(result)/n)

    # fast, exact method
    mu = sum(z)/float(n)
    sigma = sqrt(sum((z-mu)**2)/n)
    print( "Exact Parameter fits: ", (mu,sigma))
    print( "\tAverage Log-Likelihood: ", fit_likelihood((mu,sigma))/n)
    print( "\tn = : ", fit_likelihood((mu,sigma))/n)


    u = linspace(min(z)*.95,max(z)*1.05, 256)
    figure(1, figsize=(8,16))
    subplot(3,1,1)

    plot(u, n*gaussian.pdf((u-mu)/sigma)/sigma, 'b-')
    width = .3
    bar_ob = bar(x-width*.5, y, width, color='k')
    xlim(min(u), max(u))
    ylabel('Count', fontsize=18)
    title('Best Fit Gaussian: $\mu = %f$, $\sigma = %f$'%(mu,sigma), fontsize=18)

    subplot(3,1,2)
    q = linspace(0,1,n)
    plot(z,q,'ko', u, gaussian.cdf((u-mu)/sigma),'b-')
    xlabel('Height (inches)', fontsize=18)
    ylabel('Cumulative Probability', fontsize=18)
    xlim(min(u), max(u))

    subplot(3,1,3)
    plot(gaussian.cdf((z-mu)/sigma), q, 'o', q, q, 'k-')
    xlabel('Expected probability', fontsize=18)
    ylabel('Observed probability', fontsize=18)

    savefig('height_gaussian.png', bbox_inches='tight')
    show()

main()

k = [1]
k*2
