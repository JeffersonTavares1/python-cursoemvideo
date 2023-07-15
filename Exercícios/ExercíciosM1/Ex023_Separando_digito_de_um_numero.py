""" Faça um programa que leia um número de 0
a 9999 e mostra na tela cada um dos digitos separados.

Digite um número: 1834
unidada: 4
dezena: 3
centena: 8
milhar: 1"""

num = int(input("Digite um número: "))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print("\nAnalisando o número {}".format(num))
print("Unidada: {} \nDezena: {} \nCentena: {} \nMilhar: {}".format(u, d, c, m))
