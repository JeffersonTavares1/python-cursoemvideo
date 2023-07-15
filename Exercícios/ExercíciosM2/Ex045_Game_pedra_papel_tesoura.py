"""Exercício 45: Crie um programa que faça o computador
jogar jokenpô com você."""


from random import randint
from time import sleep

itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)
print("""Sua opção:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")
jogador = int(input("Qual e a sua jogada? "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!")
print("-=" * 11)
print("Computador jogou {}".format(itens[computador]))
print("Jogador jogou {}".format(itens[jogador]))
print("-=" * 11)

if computador == 0: #computador 
    if jogador == 0:
        print("EMPTE")
    elif jogador == 1:
        print("JOGADOR VENCE")
    elif jogador == 2:
        print("COMPUTADOR VENCE")
    else:
        print("Jogada inválida!")
        
elif computador == 1:
    if jogador == 0:
        print("COMPUTADOR VENCE")
    elif jogador == 1:
        print("EMPTE")
    elif jogador == 2:
        print("JOGADOR VENCE")
    else:
        print("Jogada inválida!")
    
elif computador == 2:
    if jogador == 0:
        print("JOGADOR VENCE")
    elif jogador == 1:
        print("COMPRANDO VENCE")
    elif jogador == 2:
        print("EMPTE")
    else:
        print("Jogada inválida!")
