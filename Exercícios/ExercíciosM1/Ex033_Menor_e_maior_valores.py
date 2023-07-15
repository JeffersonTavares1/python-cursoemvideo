"""Faça um programa que leia três números
e mostra qual é o maior a qual é o menor."""


n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
n3 = int(input("Terceiro valor: "))

menor = n1 #verificabdo quem e o menor:
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1 #verificando quem e o menor:
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print("\nO menor valor digitado foi {}".format(menor))
print("O mailhor valor digitado foi {}".format(maior))
