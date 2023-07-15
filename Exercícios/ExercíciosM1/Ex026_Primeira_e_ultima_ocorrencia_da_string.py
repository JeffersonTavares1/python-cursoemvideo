"""Faça um programa que leia uma frase pelo
teclado a mostra:  Quantas vezes aparece a latra "A".
Em que posição ela aparece a primeira vez
Em que posição ela aparece a última vaz"""

frase = str(input("Digite uma frase? ")).strip().upper()

print("Na frase {} tem no total de {} letras A".format(frase, frase.count("A")))
print("A primeira letra A esta na posição {}".format(frase.find("A") + 1))
print("A última letra A esta na posição {}".format(frase.rfind("A") + 1))
))




