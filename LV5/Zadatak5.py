# -*- coding: utf-8 -*-
"""
Created on Sun Dec 02 12:08:00 2018

@author: Grbic
"""

import scipy as sp
from sklearn import cluster, datasets
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
imageNew = mpimg.imread('example.png')

    
re_img1 = imageNew.imread('example.png')
b, g, r = imageNew.split(imageNew)

ttl = re_img1.size / 3 


B = float(np.sum(b)) / ttl 
G = float(np.sum(g)) / ttl
R = float(np.sum(r)) / ttl
B_mean1 = list()
G_mean1 = list()
R_mean1 = list()
B_mean1.append(B)
G_mean1.append(G)
R_mean1.append(R)

plt.figure(1)
plt.imshow(imageNew,  cmap='gray')
plt.show()

plt.figure(2)
plt.imshow(re_img1,  cmap='gray')
plt.show()

