#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 13:00:50 2021
-Scatter plot and histogram in x and y axis also.
@author: sl302
"""

import numpy as np
from matplotlib import pyplot as plt
a1,b1,c1,d1 = np.loadtxt("com-pep1-1.xvg",comments=["@", "#"], unpack=True)
e1,f1,g1,h1 = np.loadtxt("com-pep1-dopc-p-up-1.xvg",comments=["@", "#"], unpack=True)
i1,j1,k1,l1 = np.loadtxt("com-pep1-dopc-p-dw-1.xvg",comments=["@", "#"], unpack=True)


#To plot all the three plots in vertical orientation
#To make one row of two plots each
#fig, axs = plt.subplots(1,3)
#fig.suptitle("Peptide 1")
mean = [0, 0]
cov = [[1, 1], [1, 2]]
x, y = np.random.multivariate_normal(mean, cov, 3000).T

# Set up the axes with gridspec
fig = plt.figure(figsize=(6, 6))
grid = plt.GridSpec(4, 4, hspace=0.2, wspace=0.2)
main_ax = fig.add_subplot(grid[:-1, 1:])
y_hist = fig.add_subplot(grid[:-1, 0], xticklabels=[], sharey=main_ax)
x_hist = fig.add_subplot(grid[-1, 1:], yticklabels=[], sharex=main_ax)

# scatter points on the main axes
main_ax.plot(x, y, 'ok', markersize=3, alpha=0.2)

# histogram on the attached axes
x_hist.hist(x, 40, histtype='stepfilled',
            orientation='vertical', color='gray')
x_hist.invert_yaxis()

y_hist.hist(y, 40, histtype='stepfilled',
            orientation='horizontal', color='gray')
y_hist.invert_xaxis()
