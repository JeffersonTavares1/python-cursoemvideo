"""Desenvolva um programa que leia o comprimento
 de três retas e diga ao usuário se elas podem ou não
formar um triângulo."""


print("\033[33m" + ("-=" * 23) + "\033[m")
print("\033[34mAnalisador de Triângulo.\033[m")
print("\033[33m" + ("-=" * 23) + "\033[m")


r1 = float(input("Primeiro seguimento? "))
r2 = float(input("Segundo seguimento? "))
r3 = float(input("Terceiro seguimento? "))

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print("\nOs seguimento a cima PODEM FORMAR UM TRIÂNGULO!")
else:
    print("\nOs seguimento a cima NÃO PODEM FORMAR UM TRIÂNGULO!")
