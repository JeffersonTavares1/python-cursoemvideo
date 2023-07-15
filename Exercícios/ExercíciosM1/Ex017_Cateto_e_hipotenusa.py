"""Faça um programa que leia o comprimento do catato 
oposto a do cateto adjacente de triângulo um retângulo,
 calcule e mostra o comprimento da hipotenusa. """

from math import hypot

co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))

#hi = (co ** 2 + ca ** 2) ** (1/2) formar matematica de resolver
hi = hypot(co, ca)

print("A hipotenusa vai medir {:.2f}".format(hi))
