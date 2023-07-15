"""Exercício Python 076: Crie um programa que tenha 
uma tupla única com nomes de produtos e seus 
respectivos preços, na sequência. No final, mostre 
uma listagem de preços, organizando os dados em 
forma tabular."""


item = ("Lapis", 1.75, "Boracha", 2.00, "50 folhas ofício", 
4.50, "Caderno", 15.99, "Caneta", 2.10)

print("一" * 20)
for pro in item:
    if type(pro) == str:
        print("{:-<20} R$".format(pro), end=" ")
    if type(pro) == float or type(pro) == int:
        print("{:>10.2f}".format(pro))
print("一" * 20)
