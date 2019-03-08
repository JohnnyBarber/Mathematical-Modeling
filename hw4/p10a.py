# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 20:51:44 2018

@author: Jiaqi Li
"""

#!/usr/bin/env python3

import json
from urllib.request import urlopen
import time
import numpy
import os
from scipy import log, linalg, exp, linspace
from scipy.optimize import fminbound
from scipy.linalg import norm
from matplotlib.pyplot import *

diff = lambda x : [float(x[i]-x[i-1]) for i in range(1,len(x))]

firstday = '1995-01-01'
lastday = '2005-01-01'
def bindata(y, n):
    tmin, tmax = min(y), max(y)
    print("Rough parameter estimate $\lambda=%f$"%((len(y)-1)/(tmax-tmin)))
    dt = (tmax-tmin)/float(n)
    print("# bin size = %f days"%dt)
    def g(t):
        return int( (t-tmin)/dt )
    h = [ g(i) for i in y]
    x,y = list(zip(*[(i,h.count(i)) for i in range(n)]))
    for i in range(max(y)+1):
        print(i, y.count(i))
    return dt,x,y

def retrievedata():
    # We can easily program functions to access and
    # retrieve data from the internet these days.
    # This function retrieves data on bolide impacts
    # from JPL.
    #
    # docs at http://ssd-api.jpl.nasa.gov/doc/fireball.html
    #
    baseurl="http://ssd-api.jpl.nasa.gov/fireball.api"
    tags={
        'date-min': firstday,
        'date-max': lastday,
    }
    parameters = '&'.join(['%s=%s'%(i,tags[i]) for i in tags])
    url = baseurl+'?'+parameters
    return json.loads(urlopen(url).read())

def dataclean(result):
    rawdates = [i[0] for i in result['data']]
    f = lambda s : time.mktime(time.strptime(s, '%Y-%m-%d %H:%M:%S'))
    secdata = numpy.array([f(i[0]) for i in result['data']]) # seconds since epoch of each hit
    secdata.sort()
    daydata = (secdata - secdata[-1])/float(60*60*24)
    return rawdates, daydata

def main():
    daydatafile= 'bolideDayData.npy'
    datedatafile = 'bolideDateData.csv'
    if os.path.exists(daydatafile) and os.path.exists(datedatafile):
        return

    rawdates, daydata = dataclean(retrievedata())

    numpy.save(daydatafile,daydata)

    header = "# year, month, day, hour, minute, second\n"
    body = '\n'.join(rawdates).replace(' ',',')
    body = body.replace('-',',').replace(':',',')
    f = open(datedatafile, 'w')
    print(header + body, file=f)
    f.close()

main()