"""Exercício Python 068: Faça um programa que jogue 
par ou ímpar com o computador. O jogo só será
 interrompido quando o jogador perder, mostrando 
 o total de vitórias consecutivas que ele conquistou
  no final do jogo. """


from random import randint

print("=" * 20)
print("Vamos jogar PAR ou IMPAR")

vitórias = soma = 0
while True:
    computador = randint(1, 10)
    print("=" * 20)
    jogador = int(input("Digite um valor: "))
    
    es = " "
    while es not in "PI":
        es = str(input("Par ou Ímpar? [P/I]: ")).strip().upper()[0]
    
    soma = computador + jogador
    
    print("=" * 20)
    print("Você jogador {} e o computador {} total de {} deu".format(jogador, computador, soma), end=" ")
    print("Par" if soma % 2 == 0 else "Ímpar")
    print("=" * 20)
    
    if es == "P":
        if soma % 2 == 0:
            print("VOCÊ VENCEU!")
            vitórias += 1
        else:
            print("VOCÊ PERDEU!")
            break
    
    elif es == "I":
        if soma % 2 == 1:
            print("VOCÊ VENCEU!")
            vitórias += 1
    else:
            print("VOCÊ PERDEU!")
            break
        
    print("Vamos Jogar Novamente...")

print("Game over! você venceu {} vezes".format(vitórias))
print("=" * 20)
