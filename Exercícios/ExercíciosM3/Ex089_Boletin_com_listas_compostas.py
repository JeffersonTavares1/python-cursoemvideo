"""Exercício Python 089: Crie um programa que leia 
nome e duas notas de vários alunos e guarde tudo 
em uma lista composta. No final, mostre um boletim 
contendo a média de cada um e permita que o usuário 
possa mostrar as notas de cada aluno individualmente."""


ficha = list()

while True:
    nome = str(input("Nome: ")).strip()
    nota1 = float(input("Nota1 : "))
    nota2 = float(input("Nota2 : "))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input("Quer continuar? [S/N]: ")).strip()
    
    if resp in "Nn":
        break
print("一=" * 13)


print(f"{'No.':<8}{'NOME':<10}{'MÉDIA'}:<8")
print("一" * 18)
for pos, intem in enumerate(ficha):
    print(f"{pos:<8}{intem[0]:<10}{intem[2]:>8.1f}")

while True:
    print("一" * 18)
    opc = int(input("Mostrar nota de qual aluno? (999 sair): "))
    if opc == 999:
        break
    if opc <= len(ficha) - 1:
        print(f"Notas de {ficha[opc] [0]} são {ficha[opc] [1]}")
print("<<< Fim! >>>")




       break
    else:
        print(f"Notas de {dados_guardados[op][0]} são {dados_guardados[op][1:]}")
    
print("Voute Sempre")

