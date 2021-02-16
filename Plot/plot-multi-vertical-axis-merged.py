#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 12:40:57 2021

@author: sl302
"""


import numpy as np
from matplotlib import pyplot as plt
a1,b1,c1,d1 = np.loadtxt("com-pep1-1.xvg",comments=["@", "#"], unpack=True)
e1,f1,g1,h1 = np.loadtxt("com-pep1-dopc-p-up-1.xvg",comments=["@", "#"], unpack=True)
i1,j1,k1,l1 = np.loadtxt("com-pep1-dopc-p-dw-1.xvg",comments=["@", "#"], unpack=True)

a2,b2,c2,d2 = np.loadtxt("com-pep1-2.xvg",comments=["@", "#"], unpack=True)
e2,f2,g2,h2 = np.loadtxt("com-pep1-dopc-p-up-2.xvg",comments=["@", "#"], unpack=True)
i2,j2,k2,l2 = np.loadtxt("com-pep1-dopc-p-dw-2.xvg",comments=["@", "#"], unpack=True)

a3,b3,c3,d3 = np.loadtxt("com-pep1-3.xvg",comments=["@", "#"], unpack=True)
e3,f3,g3,h3 = np.loadtxt("com-pep1-dopc-p-up-3.xvg",comments=["@", "#"], unpack=True)
i3,j3,k3,l3 = np.loadtxt("com-pep1-dopc-p-dw-3.xvg",comments=["@", "#"], unpack=True)

#To plot all the three plots in vertical orientation
#To make one row of two plots each
fig, axs = plt.subplots(1,3, sharey=True)
fig.suptitle("Peptide 1")
fig=plt.figure()
#+fig=plt.subplots_adjust(wspace=0)
#gs=fig.add_gridspec(1,3, wspace=0)
#axs= gs.subplots(sharex=True, sharey=True)

axs[0].plot(a1/1000,d1, label="Peptide 1 COM")
axs[0].plot(e1/1000,h1, label="DOPC-P")
axs[0].plot(i1/1000,l1, label="DOPC-P" )

axs[1].plot(a2/1000,d2)
axs[1].plot(e2/1000,h2)
axs[1].plot(i2/1000,l2)

axs[2].plot(a3/1000,d3)
axs[2].plot(e3/1000,h3)
axs[2].plot(i3/1000,l3)



#for ax in axs:
#    ax.label_outer()

#axs[2].plot(i,l)
# ...
#plt.plot(a,d)
