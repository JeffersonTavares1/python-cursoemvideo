""" Exercício Python 066: Crie um programa que leia 
 números inteiros pelo teclado. O programa só 
 vai parar quando o usuário digitar o valor 999, 
 que é a condição de parada. No final, mostre 
 quantos números foram digitados e qual foi a 
 soma entre elas (desconsiderando o flag)."""


cont = soma = 0
while True:
    v = int(input("Digite um valor ou [999] para somar: "))
    if v == 999:
        break
    cont += 1
    soma += v

print(f"\nA soma dos {cont} valores digitados foi {soma}")
