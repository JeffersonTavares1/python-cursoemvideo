"""Exercício Python 070: Crie um programa que leia o
 nome e o preço de vários produtos. O programa 
 deverá perguntar se o usuário vai continuar ou não. 
 No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato."""


import os

cont = 1
Total = maior1000 = menor = 0
baratoNome = ""

while True:
    print("一" * 20)
    print("LOJA DA SUPER MARCASSE LE ABAUT")
    print("一" * 20)
    
    nome = str(input("NOME do Produto?   ")).strip().capitalize()
    preco = float(input("VALOR da Compra?  R$"))
    print("一" * 20)
    print(f"{cont} Produtos adicionado no Carinho")
    
    op = "Entra"
    while op not in "SN":
        print("一" * 20)
        op = str(input("Continuar? [S/N]:  ")).strip().upper()[0]
    
    Total += preco #A) qual é o total gasto na compra.
    
    if preco > 1000: #B) quantos produtos custam mais de R$1000.
        maior1000 += 1
        
    if cont == 1 or preco < menor: #C) qual é o nome do produto mais barato.
        menor = preco
        baratoNome = nome
    
    if op == "N":
        break
    cont += 1
    os.system("clear")
    
print("\nTotal a pagar pelos {} Produtos: R${}".format(cont, Total))
print("{} Produto custando mais de R$1000".format(maior1000))
print("Nome do Produto mais barato: {} que custa {}".format(menor, baratoNome))



ome do Produto mais barato: {}".format(baratoNome))





