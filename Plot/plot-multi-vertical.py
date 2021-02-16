#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 12:20:41 2021
-To read a xvg file without comments in Numpy format.
-Subplot all the three columns as vertical orientation.
@author: sl302
"""
import numpy as np
from matplotlib import pyplot as plt
a,b,c,d = np.loadtxt("com-pep1-1.xvg",comments=["@", "#"], unpack=True)
e,f,g,h = np.loadtxt("com-pep1-dopc-p-up-1.xvg",comments=["@", "#"], unpack=True)
i,j,k,l = np.loadtxt("com-pep1-dopc-p-dw-1.xvg",comments=["@", "#"], unpack=True)

#To plot all the three plots in vertical orientation
fig, axs = plt.subplots(3)
fig.suptitle("Peptide 1")
axs[0].plot(a,d)
axs[1].plot(e,h)
axs[2].plot(i,l)
# ...
#plt.plot(a,d)


