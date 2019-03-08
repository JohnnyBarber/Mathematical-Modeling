# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 02:32:23 2018

@author: Jiaqi Li
"""

from scipy import array, linspace
from scipy import integrate
from matplotlib.pyplot import *

#60 %

wid1 = linspace(0, 15, 256)
s1 = 100.7
int1 = 436.2
TBL1 = [(s1*i + int1)/100 for i in wid1]

#65%

wid2 = linspace(0, 15, 256)
s2 = 106
int2 = 390
TBL2 = [(s2*i + int2)/100 for i in wid2]

x_0 = 12
y_60 = (s1*x_0+int1)/100
y_65 = (s2*x_0+int2)/100
#The predicted body length of Titanoboa in meter

figure(1)
plot(wid1, TBL1, 'b')
plot(wid2, TBL2, 'r')
plot(x_0,y_60,'o',x_0,y_65,'o')
legend(['60%', '65%'], loc=0, framealpha=0.)
xlabel('Verterba Width (cm)')
ylabel('Total Body Length (TBL) (meter)')

print('\nlength due to 60% and 65% extreme values')
print(y_60,y_65)
