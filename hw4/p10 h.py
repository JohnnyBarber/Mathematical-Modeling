# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 03:58:53 2018

@author: Jiaqi Li
"""

from scipy import floor, cumsum, array, linspace, cos, pi, rand, loadtxt
from scipy import *
from scipy.stats import poisson
from scipy.optimize import fminbound
from matplotlib.pyplot import *
import time
import numpy

day = load('bolideDayData.npy')

interval = zeros((279,1))
i = 0
while i < 279:
    interval[i] = (-day[279-i-1])- (-day[279-i])
    i += 1

figure(1,figsize = (8,6))
hist(interval)
xlabel('number of days',fontsize = 20)
ylabel('frequency (unit = interval)',fontsize = 20)

