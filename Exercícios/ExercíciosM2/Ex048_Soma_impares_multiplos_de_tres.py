"""Exercício Python 048: Faça um programa que 
calcule a soma entre todos os números que são 
múltiplos de três e que se encontram no intervalo de
 1 até 500."""


soma = 0
cont = 0
for c in range(1, 501, 2):
     if c % 3 == 0: #pegando os numeros múltiplos de 3
         cont = cont + 1 #simplifica: cont += 1
         soma += c
 
print("A soma de todos os {} valores e {}".format(cont, soma))
