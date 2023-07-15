""".Exercício Python 043: Desenvolva uma lógica que
 leia o peso e a altura de uma pessoa, calcule seu 
 índice de Massa Corporal (IMC) e mostre seu 
 status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
-Entre 18,5 e 25: Peso Ideal
-25 até 30: Sobrepeso
-30 até 40: Obesidade
-Acima de 40: Obesidade Mórbida"""


peso = float(input("Qual seu peso? (Kg) "))
altura = float(input("Qual a sua altura? (m) "))

IMC = peso / (altura ** 2)

print("O OMC dessa pessoa e de {:.1f}".format(IMC))

if IMC < 18.5:
    print("Você esta ABAIXO do Peso normal!")
elif 18.5 <= IMC < 25:
    print("Parabéns você esta na faixa de peso normal!")
elif 25 <= IMC < 30:
    print("Você está em SOBREPESOE!")
elif 30 <= IMC < 40:
    print("Você está em OBESIDADE! ")
elif IMC >= 40:
    print("Você está em OBESIDADE MÓRBIDA!")
