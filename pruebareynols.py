# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 16:32:31 2016

@author: ANDRES PRIETO YANES
"""

import matplotlib.pyplot as plt
from numpy import genfromtxt
from matplotlib.legend_handler import HandlerLine2D

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

# print datos
fig, ax = plt.subplots()

acero_galv, = ax.plot(re_1,f_1,'o' , label='Acero galvanizado')
cobre, = ax.plot(re_2 , f_2 , 'v' , label = 'Cobre')
pvc_1, = ax.plot(re_3 , f_3, 'x' , label = 'PVC (Estrecho)')
pvc_2, = ax.plot(re_4 , f_4 , 'o', label = 'PVC (Ancho)')



plt.legend(handler_map={acero_galv: HandlerLine2D(numpoints=2)})
plt.legend(handler_map={cobre: HandlerLine2D(numpoints=2)})
plt.legend(handler_map={pvc_1: HandlerLine2D(numpoints=2)})
plt.legend(handler_map={pvc_2: HandlerLine2D(numpoints=2)})

plt.xlim(4600 , 40000)
plt.ylim(10**-2 , 10**1)

#plt.title('Factor de friccion obtenido frente al numero de Reynolds')
plt.grid(False)
plt.ylabel('Factor de friccion')
plt.xlabel('Reynols')

ax.set_yscale('log')
ax.set_xscale('log')
plt.show()

# limite 4900 reynols
# limite 0.2 fricccion


# pyplot.plot(y, color='red', lw=1.2)

# pyplot.yscale('log')
# pyplot.xscale('log')
# pyplot.show()
