#Exercício Python 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota1 = float(input('Primeira nota do aluno: '))
nota2 = float(input('Segunda nota do aluno: '))

média = (nota1 + nota2) / 2

print('\n A media entre {:.1f} e {:.1f} e igual a {:.1f}'.format(nota1, nota2, média))
