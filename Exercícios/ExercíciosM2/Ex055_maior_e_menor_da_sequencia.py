"""Exercício Python 055: Faça um programa que leia
 o peso de cinco pessoas. No final, mostre qual foi o
  maior e o menor peso lidos."""


maior = 0.0
menor = 1000
for c in range(1, 6):
    peso = float(input("Peso da {}° pessoa? ".format(c)))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print("\nMaior peso informado: {} \nMenor peso informado: {}".format(maior, menor))


ormat(maior, menor))
