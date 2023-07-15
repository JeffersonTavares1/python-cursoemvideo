"""Exercicio Python 036: Escreva um programa para
 aprovar o empréstimo bancário para a compra de uma 
 casa. Pergunte o valor da casa, o salário do comprador 
 e em quantos anos ele vai pagar. Aprestação mensal
  não pode exceder 30% do salário ou então o 
  empréstimo será negado."""

valorC = float(input("Valor da casa? R$"))
salário = float(input("Salario do comprador? R$"))
ano = int(input("Quantos anos de financiamento? "))

prestação = valorC / (ano * 12)
minimo = salário * 30 / 100

print("\nPara pagar uma casa de R${:.2f} em {} anos".format(valorC, ano), end="")
print(" a prestação será de R${:.2f}".format(prestação))

if prestação <= minimo:
    print("Empréstimo pode ser concedido!")
else:
    print("Empréstimo negado!!")
