#Exercício Python 009: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

n = int(input('Informe um valor: '))

print('\n' + ('_' * 10))
print('{:2}  × {:2}  = {:2}'.format(n, 1, n * 1))
print('{:2}  × {:2}  = {:2}'.format(n, 2, n * 2))
print('{:2}  × {:2}  = {:2}'.format(n, 3, n * 3))
print('{:2}  × {:2}  = {:2}'.format(n, 4, n * 4))
print('{:2}  × {:2}  = {:2}'.format(n, 5, n * 5))
print('{:2}  × {:2}  = {:2}'.format(n, 6, n * 6))
print('{:2}  × {:2}  = {:2}'.format(n, 7, n * 7))
print('{:2}  × {:2}  = {:2}'.format(n, 8, n * 8))
print('{:2}  × {:2}  = {:2}'.format(n, 9, n * 9))
print('{:2}  × {:2}  = {:2}'.format(n, 10, n * 10))
print('_' * 10)
