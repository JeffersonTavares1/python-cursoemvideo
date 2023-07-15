"""Exercício Python #061​ - Progressão Aritmética
 v2.0, Exercício Python 061: Refaça o DESAFIO 051, 
 lendo o primeiro termo e a razão de uma PA, 
 mostrando os 10 primeiros termos da progressão 
 usando a estrutura while."""


print("=" * 17)
print("GERADOR DE PA")
print("=" * 17)

primeiro = int(input("Primeiro termo: "))
razão = int(input("Razão: "))

termo = primeiro
cont = 1

while cont <= 10:
    print("{} → ".format(termo), end="")
    termo += razão
    cont += 1
print("FIM")
