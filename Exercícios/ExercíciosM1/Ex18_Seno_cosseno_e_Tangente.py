"""Faça um programa que leia um ângulo 
qualquer a mostra na tela o valor do seno,
cossano a tangente desse ângulo."""

from math import sin, radians, cos, tan

angulo = float(input("Digite o ângulo que você deseja: "))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print("\nO ângulo {} tem o Seno de {:.2f}".format(angulo, seno))
print("O ângulo {} tem o Cosseno de {:.2f}".format(angulo, cosseno))
print("O ângulo {} tem a Tangente de {:.2f}".format(angulo, tangente))



