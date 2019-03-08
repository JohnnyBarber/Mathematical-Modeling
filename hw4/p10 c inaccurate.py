# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 14:31:28 2018

@author: Jiaqi Li
"""
#c------------------------------------------
from scipy import *
import numpy
from matplotlib.pyplot import *

t = loadtxt('p10 c data.txt')
rank = linspace(1,280,280)

i = 0
m = zeros((280,1))
j = 0
while i < 280:
    m[i] = m[i] + j
    j += t[279-i]
    i += 1
    
figure(1,figsize=(10,8))
scatter(m,rank)
xlabel('days', fontsize = 25)
ylabel('ranks', fontsize = 25)

#d------------------------------------------
rate1 = 280/m[279]
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
            j += t[279-k]
            k += 1
        else:
            j = 45*i +1
    i += 1
rate2[80] = rate2[80] - 1
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

