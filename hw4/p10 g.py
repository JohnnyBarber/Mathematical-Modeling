# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 17:49:14 2018

@author: Jiaqi Li
"""

from pylab import *
import csv
from scipy.stats import norm as gaussian
from scipy.optimize import fmin

day = load('bolideDayData.npy')

rate2 = zeros((81,1))
i = 1
k = 0
j = 0
while i <= 81:
    while j <= 45*i:
        rate2[i-1] += 1
        if k <= 279:
            j = -day[279-k]
            k += 1
        else:
            j = 45*i +1
    i += 1
sum(rate2)

count = zeros((12,1))
j = 0
while j < 12:
    i = 0
    while i < 81:
        if rate2[i] == j:
            count[j] += 1
        i += 1
    j += 1

def main():
    x = linspace(0,11,12)
    y = count[:,0]
    m = count.shape[0]

    z = []
    for i in range(m):
        z += [x[i]]*int(y[i])
    n = len(z)
    z = array(z)

    # slow, inaccurate method
    def fit_likelihood(a):
        return -sum(log(gaussian.pdf((z-a[0])/a[1])/a[1]))
    objective = fit_likelihood
    a = array([64.,6.])
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