#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 18:45:59 2021
This is the code for PBC condition for the peptide COM
@author: sl302
"""
import sys
import numpy as np
from matplotlib import pyplot as plt

#File 1 to define the xvg file 1:4
file1=sys.argv[1]
file2=sys.argv[2]

a1,b1,c1,d1 = np.loadtxt(file1,comments=["@", "#"], unpack=True)

#Fprint(len(d1))
#x=np.zeros(len(d1))
j=-10
file=open(file2, 'w+')
for i in d1:
    j=j+10
    if i < 4:
        file.write( str(j) + " " + str(i+7.8) + "\n")
    else:
        file.write(  str(j) + " " + str(i)+ "\n")

        
file.close()
       
