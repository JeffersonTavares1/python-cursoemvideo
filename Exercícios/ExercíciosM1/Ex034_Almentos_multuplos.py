"""Escrava um programa que pergunte o salário de
um Funcionário a calcule o valor do seuaumento. 
Para salários superiores a R$1.250,00, calcule um
 aumento de 10%. Para os inferiores ou iguais, 
 o aumento é de 15%."""


salário = float(input("Qual valor do seu salário? "))

if salário > 1.250:
    aumento = salário + (salário * 10 / 100)
else:
    aumento = salário + (salário * 15 / 100)

print("\nSeu salário que custava R${:.2f} com aumento fica por R${:.2f}".format(salário, aumento))
alário, aumento))
