"""Exercício Python 077: Crie um programa que tenha 
uma tupla com várias palavras (não usar acentos). 
Depois disso, você deve mostrar, para cada palavra, 
quais são as suas vogais."""

#aeiou
item = ("Lapis", "Boracha", "50 folhas ofício", 
"Caderno", "Caneta")

print("\nAnalisando vogais em Tupla:")
print("一" * 20, end="")
for pos, palavra in enumerate(item):
    print("\nNa palavra: < {} > temos: ".format(palavra.upper()), end=" ")
    
    for letra in item[pos].strip().upper():
        if letra in "AEIOU":
            print(f"{letra}", end=" ")
print("\n" + "一" * 20)
