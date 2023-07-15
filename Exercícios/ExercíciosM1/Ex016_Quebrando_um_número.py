"""Crie um programa que leia um número Real qualquer pelo
teclado a mostra na tela a sua porção Inteira.
Ex:
Digite um número: 6.127 O número 6.127 tam a parta Inteira 6. """

from math import trunc
 
num = float(input("Digete um numero: "))

print("O numero {} tem a parte inteira {}".format(num, trunc(num)))
