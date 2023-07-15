"""Exercício Python 039: Faça um programa que
 leia o ano de nascimento de um jovem e informe, 
 de acordo com a sua idade, se ele ainda vai se
  alistar ao serviço militar, se é a hora exata de
  se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que 
falta ou que passou do prazo."""


from datetime import date


anoAtual = date.today().year
anoNascimento = int(input("Em que ano você nasceu? "))

idade = anoAtual - anoNascimento

if idade < 18:
    print("Você está com {} anos, falta {} Anos para seu alistamento!".format(idade, 18 - idade))
    print("Seu alistamento será em {}.".format(anoAtual + (18 - idade)))
elif idade == 18:
    print("Você está com {} anos, seu alistamento pode ser feito!".format(idade))
elif idade > 18:
    print("Você está com {} anos, ja passou {} Anos para seu alistamento!".format(idade, idade - 18))
    print("Seu alistamento foi em  {}.".format(anoAtual + (18 - idade)))
