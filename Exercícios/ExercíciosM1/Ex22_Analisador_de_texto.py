"""Crie um que leia o nome completo de uma pessoa a mostra:
O nome com todas as latras maiúsculas
▶ O nome com todas minúsculas.
▶Quantas letras ao todo (sem considerar espafos).
▶Quantas letras temo primeiro noma."""

nome = str(input("Nome completo? ")).strip()

print("\nMaiúsculas: {} \nMinúsculas: {}".format(nome.upper(), nome.lower()))
print("Autodo seu nome tem {} letras".format(len(nome) - nome.count(" ")))
print("Seu primeiro nome tem {} letras".format(len(nome.split()[0])))
