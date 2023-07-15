#Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit

C = float(input("Informe a temperatura em °C: "))

F = ((9 * C) / 5) + 32 #Equaçao de conversao de cesio para farenaite

print("A temperatura de {:.1f}°C corresponde a {:.1f}.°F!".format(C, F))
