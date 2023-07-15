"""Escrava um programa que leia a velocidade e um carro.
Se ala ultrapassar 80Km/h, mostra umamensagem dizendo
que ele foi multado. A multa vai custar R$7,00 por cada Km
acima do limita."""


velocidade = int(input("Informa a velocidade do carro? "))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print("\nPor ultrapassar {}Km acima do limita de 80Km da pista \nVocê foi multado em R${:.2f}".format(velocidade - 80, multa))
else:
    print("Velocidade dentro do permitido, Boa Viagem!")
!")

