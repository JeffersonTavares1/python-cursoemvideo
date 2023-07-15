"""Exercício Python 074: Crie um programa que vai gerar 
cinco números aleatórios e colocar em uma tupla.
 Depois disso, mostre a listagem de números gerados 
 e também indique o menor e o maior valor que estão
  na tupla."""


from random import randint

num = (randint(0, 10), randint(0, 10), randint(0, 10), 
              randint(0, 10), randint(0, 10))
#maior = menor = 0

print("\nLista de números aleatórios:")
print("一" * 20)

for c in num:
    print(c)

"""
#minha solicitação:
for c in range(0, len(num)):
    print(num[c], end=" ")
    
    if c == 0:
        menor = maior = num[c]
    else:
        if num[c] > maior:
            maior = num[c]
        if num[c] < menor:
            menor = num[c]
"""
print("" + "一" * 20)

#print("Maior valor na tupla: {} \nMenor valor na tupla: {}".format(maior, menor))
print("Maior valor na tupla: {} \nMenor valor na tupla: {}".format(max(num), min(num)))
