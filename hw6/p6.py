# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 13:59:03 2018

@author: Jiaqi Li
"""

from scipy import *
import numpy
from pylab import *
import scipy

x = linspace(0,7e6,7e6+1)
sol = 1500*scipy.special.erf(x/(2*sqrt(2800*200000*365*60*60)))
figure(1,figsize = (10,8))
plot(sol)
xlabel('Depth x of the Earth',fontsize = 25)
ylabel('Temperature at Depth x',fontsize = 25)
title('Temperature Changes Due to Depth of the Earth',fontsize = 25)
