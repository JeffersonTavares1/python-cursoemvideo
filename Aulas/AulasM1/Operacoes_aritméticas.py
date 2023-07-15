

'''
arredondado número real:
round(3.4) >>> 3
round(3.7) >>> 4

+ = Adição
- = Substituição
* = Multiplicação
/ = Divisão
** = Potência
// = Divisão Inteira
% = Resto da Divisão

== usado pra comparar se 2 coisas e igual

5 + 2 == 7
5 - 2 == 3
5 * 2 == 10
5 / 2 == 2.5
5 ** 2 == 25  (5 * 5) 2 representa a contidade de vezes 5 * 5 se fose 5**3 ia ser 5 * 5 *5 e asim vai...
5 // 2 == 2
5 % 2 == 1

ordem de precedência:
1  ()
2 **
3 * / // %
4 + -

ex:
5 + 3 * 2 == 11
3 * 5 + 4 ** 2 == 31
3 * (5 + 4) ** 2 == 243
'''
'''
Prática:

5 + 3 * 2 = 11

5**2 = 25   #5 ao quadro
pow(5, 2) 25 
5**3 = 123  #5 ao cubo
pow(5, 3) 123

19/2 = 9.5
19//2 = 9
19%2 = 1

81 ** (1 / 2) = 9.0 #Raiz quadrada de 81
127 ** (1 / 3)   #Raiz cubica
#_____

max() #maior valor
min() #min() menor valor



'''
#ex:
nome = input('Qual seu nome? ')

print('\nPrazer em te conhecer {:20}!'. format(nome)) #com 20 espaço
print('\nPrazer em te conhecer {:>20}!'. format(nome)) #direita
print('\nPrazer em te conhecer {:<20}!'. format(nome)) #esquerda
print('\nPrazer em te conhecer {:^20}!'. format(nome)) #sentro

print('\nPrazer em te conhecer {:=^20}!'. format(nome)) #usa = em vez do espaço
#--------------------‐-



n1 = int(input('\nUm valor: '))
n2 = int(input('Outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

#end=' ' e pra nao pular a linha de um prit pro outro

print('\nA soma e {}, Produto e {}, Divisão e {:.3f} '.format(s, m, d), end=' >>> ') #{0} {1} pode bota a ordem de exibição
print('Divisão Inteira e {}, Potência e {}'.format(di, e))







