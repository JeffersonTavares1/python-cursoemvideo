#Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.


real = float(input("Quanto dinheiro voce tem na carteira? R$ "))

dolar = real / 5.22
#real = dolar / 0,19

print("Com {:.2f} voce pode comprar US${:.2f}".format(real, dolar))



#USD-BRL,USD-BRLT,CAD-BRL,EUR-BRL,GBP-BRL,ARS-BRL,BTC-BRL,LTC-BRL,JPY-BRL,CHF-BRL,AUD-BRL,CNY-BRL,ILS-BRL,ETH-BRL,XRP-BRL
