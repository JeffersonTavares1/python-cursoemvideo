#Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario = float(input("Qual e o salario do Fucionario? R$ "))

aumento = salario + (salario * 15 / 100)

print("\nUm fucionario que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}".format(salario, aumento))
