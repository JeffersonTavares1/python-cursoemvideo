"""Exercício Python 081: Crie um programa que vai ler
 vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""

Lista = []

while True:
    num = int(input("\nDigite um valor: "))
    Lista.append(num)
    print("Valor adicionado a Lista...")
    
    resp = str(input("Quer continuar [S/N]: ")).strip().upper()
    if resp == "N":
        break
    
print("\nVocê digitou {len(Lista)} números...")
Lista.sort(reverse=True)
print(f"{Lista = } em ordem decrescente.")
print("O valor 5 está na lista" if 5 in Lista else "O valor 5 não está na lista")
