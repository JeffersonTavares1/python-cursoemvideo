"""Exercício Python #049​ - Tabuada v.2.0, Exercício
 Python 049: Refaça o DESAFIO 009, mostrando a 
 tabuada de um número que o usuário escolher, só que 
 agora utilizando um laço for"""


ta = int(input("Número para ver sua tabuada: "))

print("-" * 10)
for c in range(1, 11):
    print("{:2} × {:2} = {}".format(c, ta, c * ta))
print("-" * 10)
