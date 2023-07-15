"""Desenvolva um programa que pergunte a distância
de uma viagem em Km. Calcule o preço da
passagem.cobrando R$0.50 por Km para
viagens de até 200km a R$0.45 para viagens mais longas."""

distância = int(input("Qual a distância de sua viagem? "))


"""
if distância <= 200:
    valor = distância * 0.50
else:
    valor = distância * 0.45
"""
valor = (distância * 0.50) if distância <= 200 else (distância * 0.45) #Condiçao simplificado

print("\nVocê está presente a fazenda uma viagem de {}.0Km.".format(distância))
print("E o preço de sua passagem será de R${:.2f}".format(valor))
