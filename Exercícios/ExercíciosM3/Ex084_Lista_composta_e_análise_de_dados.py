"""Exercício Python 084: Faça um programa 
que leia nome e peso de várias pessoas, guardando 
tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""


dados_guardados = []
dados_temporarios = []
maior = menor = 0

while True:
    nome = input("Qual seu Nome: ").strip().capitalize()
    peso = float(input(f"{nome} Quanta você está pesando: "))
    print("一" * 16)
    
    dados_temporarios.append(nome)
    dados_temporarios.append(peso)
    
    if len(dados_guardados) == 0:
        maior = menor = dados_temporarios[1]
    else:
        if dados_temporarios[1] > maior:
            maior = dados_temporarios[1]
        if dados_temporarios[1] < menor:
            menor = dados_temporarios[1]
    
    dados_guardados.append(dados_temporarios[:])
    dados_temporarios.clear()
    
    resp = input("Quer continuar [S/N]: ").strip().upper()
    print("一" * 16)
    if resp in "N":
        break

print(f"\nNo Total {len(dados_guardados)} pessoa cadastradas.")
print(f"\nO maior peso foi de {maior} kg. Pesso de", end=" ")
for p in dados_guardados:
    if p[1] == maior:
        print(f"[{p[0]}]")

print(f"\nO menor peso foi de {menor} kg. Peso de", end=" ")
for p in dados_guardados:
    if p[1] == menor:
        print(f"[{p[0]}]")
