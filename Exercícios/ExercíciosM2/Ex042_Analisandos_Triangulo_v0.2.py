"""Exercício Python 042: Refaça o DESAFIO 035 dos
 triângulos, acrescentando o recurso de mostrar
  que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISOSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes"""



print("\033[33m" + ("-=" * 23) + "\033[m")
print("\033[34mAnalisador de Triângulo.\033[m")
print("\033[33m" + ("-=" * 23) + "\033[m")


r1 = float(input("Primeiro seguimento? "))
r2 = float(input("Segundo seguimento? "))
r3 = float(input("Terceiro seguimento? "))

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print("\nOs seguimento acima PODEM FORMAR UM TRIÂNGULO", end=" ")
    if r1 == r2 and r2 == r3:
        print("EQUILÁTERO!")
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print("ESCALENO!")
    else:
        print("ISOSCELES!")
else:
    print("\nOs seguimento acima NÃO PODEM FORMAR UM TRIÂNGULO!")
