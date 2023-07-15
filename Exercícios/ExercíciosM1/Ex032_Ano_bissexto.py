"""Faça um programa que leia um ano
qualquer a mostra se ate é BISSEXTO."""

from datetime import date #<

ano = int(input("Que ano quer analisar? \nColoque 0 para analisar o Ano atual: "))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("\nO ano {} é BISSEXTO".format(ano))
else:
    print("\nO ano {} não é BISSEXTO".format(ano))




