"""Exercício Python 075: Desenvolva um programa que leia
quatro valores pelo teclado e guarde-os em uma tupla. No
final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares."""


num = (int(input("1ª Valor: ")), int(input("2ª Valor: ")), 
              int(input("3ª Valor: ")), int(input("4ª Valor: ")))

print("一" * 20)
print("O valor 9 apareceu {} vezes".format(num.count(9)))
print("O 1ª valor 3 está na posição {}".format(num.index(3) +1) if 3 in num else "O valor 3 não foi digitado.")
print("一" * 20)
print("Os valor par são:")
for v in num:
    if v % 2 == 0:
        print(v)
print("一" * 20)
