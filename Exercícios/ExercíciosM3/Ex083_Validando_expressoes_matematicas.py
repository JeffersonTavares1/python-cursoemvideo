"""Exercício Python 083: Crie um programa onde o
 usuário digite uma expressão qualquer que use 
 parênteses. Seu aplicativo deverá analisar se a 
 expressão passada está com os parênteses abertos e
  fechados na ordem correta."""


expr = str(input("Digite uma expressão: "))

pilha = []

for sim in expr:
    if sim == "(":
        pilha.append("(")
    elif sim == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break

if len(pilha) == 0:
    print("Sua expressão esta valida.")

else:
    print("Sua expressão está errada.")
