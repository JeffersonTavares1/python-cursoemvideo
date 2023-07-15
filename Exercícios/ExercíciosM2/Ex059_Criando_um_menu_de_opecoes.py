"""Exercício Python 059: Crie um programa 
que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em 
cada caso."""

op = 4
while op != 5:
    
    print("=" * 20)
    print("\tCalculadora Simples")
    print("=" * 20)
    
    if op == 4:
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
        print("=" * 20)
        op = 0
    
    if op == 0:
        print("""[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa""")
    print("=" * 20)
    op = int(input("Sua Opção: "))
    
    if op == 1:
        print("=" * 20)
        print("R:   {} + {} = {}".format(n1, n2, n1 + n2))
        op = 0
        
    elif op == 2:
        print("=" * 20)
        print("R:   {} x {} = {}".format(n1, n2, n1 * n2))
        op = 0
        
    elif op == 3:
        print("=" * 20)
        if n1 == n2:
            print("{} e {} São números iguais!".format(n1, n2))
        elif n1 > n2:
            print("{} e Maior que {}".format(n1, n2))
        else:
            print("{} e Maior que {}".format(n2, n1))
        op = 0
    else:
        print("Opção inválida!")
