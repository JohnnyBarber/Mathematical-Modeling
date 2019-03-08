# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 03:21:52 2018

@author: Jiaqi Li
"""

import numpy
from scipy import *
from matplotlib.pyplot import *

data = loadtxt('1d_data.txt')

tF = data[:,6]
n = len(tF)

estF = [-54]*n

Md = data[:,2]

figure(1,figsize=(12,8))
plot(Md,tF)
plot(Md,estF)
ylim(-130,10)
legend(['Observed','Estimated Average'],loc=2,framealpha=1,fontsize=15)
xlabel('Sols',fontsize=20)
ylabel('Temperature',fontsize=20)
title('Temperature Change on Mars in One Martian Day',fontsize=20)