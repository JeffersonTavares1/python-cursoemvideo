"""Cria um programa que laia o nome de uma cidade
e diga se ela comasa ou não com o nome "SANTO"."""

cidade = str(input("Em que cidade você nasceu? ")).strip().lower()

print("{}".format(cidade[:5] == "santo"))
(cidade.split()[0] == "santo"))

