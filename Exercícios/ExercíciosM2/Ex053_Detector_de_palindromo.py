"""Exercício Python 053: Crie um programa que leia
 uma frase qualquer e diga se ela é um palíndromo,
  desconsiderando os espaços."""


frase = str(input("Digite uma frase: ")).strip().upper().replace(" ", "")

nome = ""
for c in range(len(frase) -1, -1, -1):
    nome += frase[c]

print("\nO inverso de [{}] e [{}]".format(frase, nome))
print("A frase e um PALÍNDROMO!" if frase == nome else "A frase não e um PALÍNDROMO!")
