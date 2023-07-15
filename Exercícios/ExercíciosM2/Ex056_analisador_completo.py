"""Exercício Python #056​ - Analisador completo, 
Exercício Python 056: Desenvolva um programa 
que leia o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: a média de idade do 
grupo, qual é o nome do homem mais velho e quantas 
mulheres têm menos de 20 anos."""


media = maior = cont = 0
for c in range(1, 5):
    print("----- {}ª PESSOA -----".format(c))
    nome = str(input("Nome: ")).strip().lower()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo: [M/F]: ")).strip().lower()
    
    media += idade
    
    if sexo == "m" and idade > maior:
        maior = idade
        velho = nome
    
    if sexo == "f" and idade < 20:
        cont =+ 1
    
print("\nA média de idade do grupo e de {} anos".format(media / c))
print("O Homem mais velho tem {} anos e se chama {}.".format(maior, velho))
print("Ao todo são {} mulheres com menos de 20 anos".format(cont))






Somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = 0
totmulher20 = 0

for p in range(1, 5):
    print('---- {} PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    
    somaidade += idade
    
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
        
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
        
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
        médiaidade = somaidade / 4
        
print('A média de idade do grupo é de {} anos'.format(médiaidade))
print('0 homem mais velho tem {} anos e se chama {}.'. format (maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))





