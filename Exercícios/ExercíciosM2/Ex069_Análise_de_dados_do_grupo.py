"""Exercício Python #069​ - Análise de dados do grupo,
 Exercício Python 069: Crie um programa que leia a 
 idade e o sexo de várias pessoas. A cada pessoa 
 cadastrada, o programa deverá perguntar se o usuário
  quer ou não continuar. No final, mostre:
      
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. """


maior18 = numHomens = numMulher = 0

while True:
    print("-" * 20)
    print("CADASTRE UMA PESSOA")
    print("-" * 20)
    
    idade = int(input("Quantos anos voce tem? "))
    sexo = str(input("Qual seu Sexo? [M/F]: ")).strip().upper()[0]
    
    if idade >= 18:
        maior18 += 1
        
    if sexo == "M":
        numHomens += 1
        
    if sexo == "F" and idade < 20:
        numMulher += 1
        
    print("-" * 20)
    es = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
    
    if es == "N":
        break
    
print("-" * 20)
print("\nForam encontrados {} pessoas maior de 18 anos".format(maior18))
print("E o total de Homens cadastrados foi de {}".format(numHomens))
print("Mulheres com menos de 20 anos foram {}".format(numMulher))
print("-" * 20)
