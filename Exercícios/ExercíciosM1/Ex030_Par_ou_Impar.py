"""Crie um programa que leia um número inteiro a mostra na
tela se ele é PAR ou IMPAR. """


num = int(input("Me diga um número qualquer: "))

resultado = num % 2

if resultado == 0:
    print("O número {} e PAR".format(num))
else:
    print("O número {} e ÍMPAR".format(num))








