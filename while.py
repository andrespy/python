# -*- coding: utf-8 -*-
# FIXME: in pythono 2.7 previous line is used to include non-ascii characters

print "While controlado con Conteo"
print "==========================="

print "Un ejemplo es un sumador numérico hasta 10, como se muestra a continuación:"

suma = 0
numero = 1
while numero <= 10:
    suma = numero + suma  # FIXME: suma += numero
    numero = numero + 1  # FIXME: numero += 1
print "La suma es "
