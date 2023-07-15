
'''
int = 7, -4, 0, 9875
floaat = 4.5, 0.076, -15.223, 7.0
bool = True, False
str = "Olá", "7.5", " "
'''

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))   

soma = n1 + n2

print('\nA soma entre {} e {} vale: {}'.format(n1, n2, soma))
#----------------------

n = input('\n\nDigite um algo: ')

print(type(n)) #saber o tipo do conteúdo dentro da variavel
print(bool(n)) #Tem um valor dentro?

print(n.isnumeric()) #contem um número na variavel n?
print(n.isalpha()) #contem letra na variavel n?
print(n.isalnum) #contem letra e número na variavel n?

print(n.isupper()) #Botar as letras em MAIUSCULAS
print(n.islower()) #Bota as letras em minúsculas

print(n.isspace()) #contem so espaço na variavel n?

print(n.istitle()) #Esta capitalizado?
