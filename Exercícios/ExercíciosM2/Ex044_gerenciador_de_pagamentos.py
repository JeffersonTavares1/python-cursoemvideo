"""Exercício Python 044: Elabore um programa que 
calcule o valor a ser pago por um produto, considerando 
o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
-3x ou mais no cartão: 20% de juros"""


print("{:=^46}".format(" Loja Python "))

preco = float(input("Preço das Compras? R$"))

print("""FORMAS DE PAGAMENTOS
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] em até 2x no cartão
[ 4 ] 3x ou mais no cartão""")
op = int(input("Sua opção? "))

precoFinal = preco
if op == 1:
    precoFinal = preco - (preco * (10 / 100))
elif op == 2:
    precoFinal = preco - (preco * (5 / 100))
elif op == 3:
    parcela = precoFinal / 2
    print("Sua compra será parcelada em 2x de R${:.2f}".format(parcela))
elif op == 4:
    precoFinal = preco + (preco * (20 / 100))
else:
    print("Opção inválida de pagamento!")

print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(preco, precoFinal))
