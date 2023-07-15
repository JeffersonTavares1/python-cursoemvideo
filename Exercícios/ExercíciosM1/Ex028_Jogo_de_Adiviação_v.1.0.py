"""Escrava um programa que faça o computador "pensar"
cm um número inteiro entre 0 a 5 a pasa para
o usuário tentar descobrir qual foi o número escolhido 
pelocomputador. O programa deverá ascrèver na tela sa o
Usuário venceu ou perdeu."""


from random import randint
from time import sleep #<faz esperar>

print("\033[33m" + ("-=" * 23) + "\033[m")
print("\033[34mVou pensar no número entre 0 e 5. Tente adivinhar...\033[m")
print("\033[33m" + ("-=" * 23) + "\033[m")

computador = randint(0, 5)
jogador = int(input("Em que número eu pensei? "))

print("\033[37mPROCESSADOR...\033[m")
sleep(2)

print("\033[32mPARABENS!, Você Venceu!\033[m" if computador == jogador else "\033[31mERROU!, Você Perdeu!, Escolhi o {}\033[m".format(computador))
