# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 17:18:19 2018

@author: Jiaqi Li
"""

import random
from matplotlib.pyplot import *

def montecarlo(experiment, trials):
    positive = 0
    for _ in range(trials):
        positive += 1 if experiment() else 0
    return positive

def successive_heads(trials,heads_in_a_row):
    count = 0
    for _ in range(trials):
        if random.random() < 0.5:
            count += 1
            if count == heads_in_a_row:
                return True
        else:
            count = 0
    return False

def distribution(n):
    x = 0
    Y = [0]*101
    while x < n+1:
        Y[x] = montecarlo(lambda: successive_heads(100,x), 100000)
        x += 1
    return Y

X = [0]*101
for i in range(102):
    X[i-1] = i
    
figure(1)
plot(X,distribution(100))
xlabel('succesive heads in a row',fontsize = 10)
ylabel('successful trials with x succesive heads in a row',fontsize = 10)
