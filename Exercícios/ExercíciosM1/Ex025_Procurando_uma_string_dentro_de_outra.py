"""Crie um programa que leia o nome de uma
pessoa e diga sa ala tem "SILVA" no nome"""

nome = str(input("Informa seu nome completo? ")).strip().lower()

print("Seu nome tem Silva? {}".format("silva" in nome))
