#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 12:37:23 2021

@author: sl302
This is to plot the horizontal multiple plots

"""

import numpy as np
from matplotlib import pyplot as plt
a,b,c,d = np.loadtxt("com-pep1-1.xvg",comments=["@", "#"], unpack=True)
e,f,g,h = np.loadtxt("com-pep1-dopc-p-up-1.xvg",comments=["@", "#"], unpack=True)
i,j,k,l = np.loadtxt("com-pep1-dopc-p-dw-1.xvg",comments=["@", "#"], unpack=True)

#To plot all the three plots in vertical orientation
#To make one row of two plots each
fig, axs = plt.subplots(1,2)
fig.suptitle("Peptide 1")
axs[0].plot(a,d)
axs[1].plot(e,h)
#axs[2].plot(i,l)
# ...
#plt.plot(a,d)

