"""O mesmo professor do desafio anterior
quer sortear a ordem de apresentação de
trabalhos dos alunos. Faça um programa que 
leia o nome dos quatro alunos a mostra a
ordem sorteada."""

from random import shuffle #<usar para embaralhar a ondem de itens em uma lista. nao precisa atribuir a uma variável pra funcionar>

nome1 = str(input("Primeiro aluno: "))
nome2 = str(input("Segundo aluno: "))
nome3 = str(input("Terceiro aluno: "))
nome4 = str(input("Quarto aluno: "))

lista = [nome1, nome2, nome3, nome4]
shuffle(lista)

print("\nA ondem de Apresentação será: \n {}".format(lista))

