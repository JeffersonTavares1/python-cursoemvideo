"""Faça um programa que leia 5 valoras numéricos e
guardeos em uma lista. No final, mostra qual foi o
 maior e o menor valor digitado a as suas respectivas
posições na lista."""


num = list()
mai = men = 0



for vezes in range(0, 5):
    num.append(int(input(f"Digite o {vezes} valor: ")))
    
    if vezes == 0:
        mai = men = num[0]
    else:
        if num[vezes] > mai:
            mai = num[vezes]
        if num[vezes] < men:
            men = num[vezes]

print(f"\nVocê digitou {num}")

print(f"O Maior valor foi {mai} que esta na posição ", end=" ")
for pos, va in enumerate(num):
    if va == mai:
        print(f"{pos}... ", end="")

print(f"\nO Menor valor foi {men} que esta na posição ", end="")
for pos, va in enumerate(num):
    if va == men:
        print(f"{pos}... ", end="")
"")
")








