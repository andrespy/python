# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 16:32:31 2016

@author: ANDRES PRIETO YANES
"""
import numpy as np
from matplotlib import pyplot as plt

from numpy import genfromtxt

datos = genfromtxt(
            '/Users/ANDRES/Dropbox/uni/ambientales/amb2.csv',
            delimiter=';')

gast_95 = datos[0]
prec_95 = datos[1]
gast_85 = datos[2]
prec_85 = datos[3]


plt.scatter(gast_85, prec_85, label = 'loquesea', s=80, facecolors='none', edgecolors='r')
plt.scatter(gast_95, prec_95, label = 'loquesa', s=80, facecolors='none', edgecolors='b')

plt.show()

