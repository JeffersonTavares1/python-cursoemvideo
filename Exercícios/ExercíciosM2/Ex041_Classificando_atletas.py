"""Exercício Python 041: A Confederação Nacional de
 Natação precisa de um programa que leia o ano 
 de nascimento de um atleta e mostre sua categoria,
  de acordo com a idade:
- Ate 9 ano MIRIM
-Até 14 anos: INFANTIL
-Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
-Acima de 25 anos: MASTER """

from datetime import date

anoAtual = date.today().year
anoNascimento = int(input("Qual ano você nasceu? "))

idadeUsuário  = anoAtual - anoNascimento

if idadeUsuário <= 9:
    print("\nVocê tem {} anos, sua categoria e MIRIM".format(idadeUsuário))
elif idadeUsuário <= 14:
    print("\nVocê tem {} anos, sua categoria e INFANTIL".format(idadeUsuário))
elif idadeUsuário <= 19:
    print("\nVocê tem {} anos, sua categoria e JÚNIOR".format(idadeUsuário))
elif idadeUsuário <= 25:
    print("\nVocê tem {} anos, sua categoria e SÊNIOR".format(idadeUsuário))
elif idadeUsuário > 25:
    print("\nVocê tem {} anos, sua categoria e MASTER".format(idadeUsuário))
\nVocê tem {} anos, sua categoria e MASTER".format(idadeUsuário))
