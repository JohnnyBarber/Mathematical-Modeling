# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 01:38:07 2018

@author: Jiaqi Li
"""
from scipy import floor, cumsum, array, linspace, cos, pi, rand, loadtxt
from scipy import *
from scipy.stats import poisson
from scipy.optimize import fminbound
from matplotlib.pyplot import *
import time
import numpy

#c------------------------------------------
day = load('bolideDayData.npy')
rank = linspace(1,280,280)
    
figure(1,figsize=(10,8))
scatter(day,rank)
xlabel('days', fontsize = 25)
ylabel('ranks', fontsize = 25)

#d------------------------------------------
rate1 = -280/day[0]
print(rate1)

#e------------------------------------------
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

x = linspace(0,11,12)

figure(2,figsize=(10,8))
bar(x,count[:,0])
ylabel('frequency (unit = 45 days)',fontsize = 25)
xlabel('number of meteors',fontsize = 25)  