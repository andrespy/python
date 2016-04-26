#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt
from matplotlib import cm

# pick out a subset of them


datos_0 = ("F1", "F2", "F3", "B1", "B2", "B3","B4", "B5", "B6", "B7", "B8", "B9", "B10")

datos_1 = genfromtxt(
    '/Users/ANDRES/Dropbox/uni/ambientales/amb2.csv',
    delimiter=';')
print datos_0
print datos_1
fig = plt.figure()
fig.suptitle('Cantidad vs precio', fontsize=18, fontweight='bold')
ax = fig.add_subplot(111)
#ax.set_title('Cantidad vs precio')

ax.set_xlabel('')
ax.set_ylabel(' Precio / Cantidad ( EUR / Kg )')
h = plt.bar(xrange(len(datos_0)), datos_1, label=datos_0,color=cm.jet(0.65*datos_1/float( len(datos_1))))
plt.subplots_adjust(bottom=0.3)
xticks_pos = [0.5 , 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5 ,9.5, 10.5, 11.5, 12.5, 13.5]
#0.65*patch.get_width() + patch.get_xy()[0] for patch in h
plt.xticks(xticks_pos, datos_0,  ha='right', rotation=45)
plt.show()