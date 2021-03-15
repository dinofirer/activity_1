# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 10:35:07 2021

@author: mn17jyf
"""
import numpy as np
import matplotlib as plt
#import scipy as sp

for i in range (1, 10, 1):
    func = np.cos(i)
    plt.plot(i,func)
