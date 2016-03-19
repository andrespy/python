# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 16:32:31 2016

@author: ANDRES PRIETO YANES
"""
import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt

datos = genfromtxt(
            '/Users/ANDRES/Documents/2-q2/FLUIDOS/practica2/Workbook2.csv',
            delimiter=';')



f_1 = datos[0]
re_1 = datos[1]
f_2 = datos[2]
re_2 = datos[3]
f_3 = datos[4]
re_3 = datos[5]
f_4 = datos[6]
re_4 = datos[7]


fig, ax = plt.subplots()

acero_galv = ax.plot(re_1,f_1,'o')
cobre = ax.plot(re_2,f_2,'v')
pvc_1 = ax.plot(re_3,f_3, 'o')
pvc_2 = ax.plot(re_4,f_4, 'o')

ax.set_yscale('log')
ax.set_xscale('log')
plt.show()




# pyplot.plot(y, color='red', lw=1.2)

# pyplot.yscale('log')
# pyplot.xscale('log')
# pyplot.show()
