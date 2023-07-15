#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))

print('\nO dobro de {} vale: {} \nO triplo de {} vale: {}'.format(n, n * 2, n, n * 3))
print('\nA raiz quadrada de {} e igual a {:.2f}'.format(n, n ** (1 / 2)))
