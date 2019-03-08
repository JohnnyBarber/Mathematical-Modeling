# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 13:25:05 2018

@author: Jiaqi Li
"""

from scipy import *
import numpy

A = matrix([[1, 1/3,0,0,0],[0,0,1/3,0,0],[0,2/3,0,1/3,0],[0,0,2/3,0,0],[0,0,0,2/3,1]])
P = A**10000

print(P)
