""""Exercício Python 037: Escreva um programa em
 Python que leia um número inteiro qualquer e 
 peça para o usuário escolher qual será a base 
 de conversão: 1 para binário, 2 para octal e 3 para
hexadecimal."""

num = int(input("Digite um número inteiro: "))
print("""Escolha uma das bases para conversão
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL""")

op = int(input("Sua opção: "))

if op == 1:
    print("{} Convertido pra BINÁRIO e igual a {}".format(num, bin(num)[2:]))
elif op == 2:
    print("{} Convertido pra OCTAL e igual a {}".format(num, oct(num)[2:]))
elif op == 3:
    print("{} Convertido pra HEXADECIMAL e igual a {}".format(num, hex(num)[2:]))
else:
    print("Opção inválida!")





