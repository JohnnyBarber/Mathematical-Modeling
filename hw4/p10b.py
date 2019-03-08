# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 20:54:29 2018

@author: Jiaqi Li
"""

from scipy import *
import numpy
from matplotlib.pyplot import *

day = load('bolideDayData.npy')
day_1995 = day[0:19]

figure(1,figsize=(8,6))
bar(day_1995,0.5)
ylim(0,1)
xlabel('date (day from 2004)', fontsize = 20)
title('shot-plot of arrival time of meteors',fontsize = 20)