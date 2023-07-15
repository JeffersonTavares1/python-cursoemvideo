"""Exercício Python #065​ - Maior e Menor valores, 
Exercício Python 065: Crie um programa que leia vários 
números inteiros pelo teclado. No final da execução,
 mostre a média entre todos os valores e qual foi o 
 maior e o menor valores lidos. O programa deve 
 perguntar ao usuário se ele quer ou não continuar a
  digitar valores."""


continuar = "S"
meio = cont = soma = maior = menor = 0

while continuar == "S":
    valor = int(input("Digite um valor: "))
    continuar = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
    
    soma += valor
    cont += 1
    
    if cont == 1:
        maior = menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor

print("\nA média de todos os {} número informado foi {:.1f}".format(cont, soma / cont))
print("Analisando os números, O Maior foi {} e O Menor foi {}".format(maior, menor))
t("Analisando os números, O Maior foi {} e O Menor foi {}".format(maior, menor))


























