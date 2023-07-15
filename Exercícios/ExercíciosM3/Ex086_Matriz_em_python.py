"""Exercício Python 086: Crie um programa que declare 
uma matriz de dimensão 3x3 e preencha com valores 
lidos pelo teclado. No final, mostre a matriz na tela, 
com a formatação correta."""


dado = [[], [], []]

lin = 3
col = 3

for coluna in range(col):
    
    for linha in range(lin):
        valor = int(input(f"Digite um valor pra posição [{coluna},  {linha}]: "))
        dado[coluna].append(valor)     

print("一" * 23)

for coluna in range(col):
    for linha in range(lin):
        print(f"[{dado[coluna][linha]:^5}]", end="   ")
    print()


