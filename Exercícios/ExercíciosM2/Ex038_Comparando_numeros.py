"""Exercício Python 038: Escreva um programa que leia 
dois números inteiros e compare-os. mostrando na
 tela uma mensagem:
- O primeiro valor é maior
-O segundo valor é maior
-Não existe valor maior, os dois são iguais"""

n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))

if n1 > n2:
    print("O PRIMEIRO valor e maior")
elif n1 < n2:
    print("O SEGUNDO valor e maior")
else:
    print("Não existe valor MAIOR os dois são iguais!")
