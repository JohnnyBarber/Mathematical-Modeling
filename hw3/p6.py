# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 19:45:45 2018

@author: Jiaqi Li
"""

from random import random
from math import pow, sqrt

trial=10000000
points_the_circle = 0
throws_in_square = 0
for i in range (1, trial):
    throws_in_square += 1
    x = random()
    y = random()
    distance = sqrt(pow(x, 2) + pow(y, 2))
    if distance <= 1.0:
        points_the_circle = points_the_circle + 1.0

# hits / throws = 1/4 Pi
pi = 4 * (points_the_circle / throws_in_square)

print("Estimate value for pi by using montecarlo simulation is",pi)

#b-------------------------------------------------------

def function1(x):
    y = x - x**3/3 + x**5/5 - x**7/7 + x**9/9 - x**11/11
    return y

def function2(x):
    y = x - x**3/3 + x**5/5 - x**7/7 + x**9/9
    return y

x = sqrt(3)/3

pi1 = 6*function1(x)
pi2 = 6*function2(x)
print("The estimated pi (3 digits of accuracy) by using Taylor series of arctan is",pi1)
print("The estimated pi (2 digits of accuracy) by using Taylor series of arctan is",pi2)



def function1(x):
    y = x - x**3/3 + x**5/5 - x**7/7 + x**9/9 - x**11/11
    return y
x = sqrt(3)/3
print("The estimated pi (3 digits of accuracy) by using Taylor series of arctan is",pi1)