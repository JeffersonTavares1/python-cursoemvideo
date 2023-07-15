"""Exercício Python #058​ - Jogo da Adivinhação v2.0, 
Exercício Python 058: Melhore o jogo do DESAFIO 
028 onde o computador vai "pensar" em um número 
entre 0 e 10. Só que agora o jogador vai tentar 
adivinhar até acertar, mostrando no final quantos 
palpites foram necessários para vencer."""


from random import randint

print("=" * 21)
print("DE 0 A 10 TENTE ADIVINHAR")
print("=" * 21)

computador = randint(0, 10)
jogador = int(input("Qual o seu palpite? "))
cont = 1

while jogador != computador:
    
    if jogador < computador:
        print("Mais... Tente mais uma vez!")
    else:
        print("Menos... Tente mais uma vez!")
        
    jogador = int(input("Qual o seu palpite? "))
    cont += 1

print("\nVocê acertou! com {} tentativas".format(cont))
