# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 16:32:31 2016

@author: ANDRES PRIETO YANES
"""
import numpy as np
# FIXME: pyplot import is better done like this:
# from matplotlib import pyplot as plt
# even though it works as fine as the other, it's easier to read.
import matplotlib.pyplot as plt
# FIXME: when importing numpy as np, use np namespace to call its functions,
# classes, etc. => np.genfromtxt
from numpy import genfromtxt

# FIXME:
# import os
# base_path = os.path(...relative/absolute path to your base folder...)
# csv_file = os.path.join(base_path, 'Workbook2.csv')
# datos = np.genfromtxt(csv_file, delimiter=';')
datos = genfromtxt(
            '/Users/ANDRES/Documents/2-q2/FLUIDOS/practica2/Workbook2.csv',
            delimiter=';')

# FIXME: data unpacking is cool!
# f_1, re_1, f_2, re_2, f_3, re_3, f_4, re_4 = datos  # datos[:8]

f_1 = datos[0]
re_1 = datos[1]
f_2 = datos[2]
re_2 = datos[3]
f_3 = datos[4]
re_3 = datos[5]
f_4 = datos[6]
re_4 = datos[7]


fig, ax = plt.subplots()

# FIXME: leave one space after every comma
acero_galv = ax.plot(re_1,f_1,'o')
cobre = ax.plot(re_2,f_2,'v')
pvc_1 = ax.plot(re_3,f_3, 'o')
pvc_2 = ax.plot(re_4,f_4, 'o')

# ADVANCED FIXME: even if unpacking is cool, avoid it when possible
# styles = ['o', 'v', 'o', 'o']
# for f, r, style in zip(datos[::2], datos[1::2], styles):
#     ax.plot(re, f, style)

ax.set_yscale('log')
ax.set_xscale('log')
plt.show()

# FIXME: use English for coding ;)

# pyplot.plot(y, color='red', lw=1.2)

# pyplot.yscale('log')
# pyplot.xscale('log')
# pyplot.show()
