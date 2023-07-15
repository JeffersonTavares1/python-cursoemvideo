"""Um professor quer sortear um dos seus
quatro alunos para apagar o quadro. Faça
um programa que ajudecle. lendo o nome deles e escrevendo o noma do ascolhido."""

from random import choices #<usar para fazer uma escolha aleatoria em uma lista>

nome1 = str(input("Primeiro aluno: "))
nome2 = str(input("Segundo aluno: "))
nome3 = str(input("Terceiro aluno: "))
nome4 = str(input("Quarto aluno: "))

lista = [nome1, nome2, nome3, nome4]
escolhido = choices(lista)

print("O aluno escolhido foi {}".format(escolhido[0]))

