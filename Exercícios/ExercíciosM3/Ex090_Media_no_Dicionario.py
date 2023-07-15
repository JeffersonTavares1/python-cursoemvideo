"""Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela."""


ficha = dict()

ficha["Nome"] = str(input("Nome: ")).strip().capitalize()
ficha["Media"] = float(input(f"Média de {ficha['Nome']}: "))
ficha["Situação"] = "Aprovado" if ficha["Media"] > 7 else "Recuperação"

print("一" * 15)
for k, v in ficha.items():
    print(f"  -{k} e igual a {v}")

cuperação")

