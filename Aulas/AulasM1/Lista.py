
#Lista = [ ], Listas podem ser multaves
#Lista = list()
"""
Variável simples:                    | MEMÓRIA:
一一一一一一一一一一一一一一一一一一一一一一一一一一一
lanche = ""      →                        [    ]
lenche = "Hamburguer"      →       [ Hamburguer ]
lanche = "Suco"              →       [ Suco ]
一一一一一一一一一一一一一一一一一一一一一一一一一一一


Variável composta:  Lista    | MEMÓRIA:
一一一一一一一一一一一一一一一一一一一一一一一一一一一
lanche = [ Hanburguer, Suco, Piza, Pudin ]  c[ Hamburguer ]
                        0              1        2         3
for c in lanche:
    print(c) #Hamburguer
一一一一一一一一一一一一一一一一一一一





lanche = [ Hanburguer, Suco, Piza, Pudin ]
                            0              1        2         3
                            
                            
                            
MODIFICAÇÕES:
    一一一一一一一一
lanche[3] = "Picole"
>>> [ Hanburguer, Suco, Piza, Picole ]
                   0              1        2         3

lanche.append("Koki") #> adicionar um novo elemento no final da lista
>>> [ Hanburguer, Suco, Piza, Picole, Koki ]
                   0              1        2         3         4

lanche.insert(0, "Cachorro quente") #> adicionar um novo elemento na posição 0 da lista
>>> [ Cachorro quente, Hanburguer, Suco, Piza, Picole, Koki ]
                   0                            1               2         3         4        5




APAGAR:
    一一一一一
del lanche[3] #> apagar o conteúdo do indse 3
>>> [ Cachorro quente, Hanburguer, Suco, Picole, Koki ]
                   0                            1               2         3          4      

lanche.pop(3) #> apagar o conteúdo do indse 3, pop() remove o último conteúdo indse final
>>> [ Cachorro quente, Hanburguer, Suco, Picole, Koki ]
                   0                            1               2         3          4      

lanche.remove("Koki") #> apagar aprimeira ocorrencia pelo conteúdo não pelo indse
>>> [ Cachorro quente, Hanburguer, Suco, Picole ]
                   0                            1               2         3   

lanche.clear()  #para apagar tudo


CRIAÇÃO:
    一一一一一一一
valores = list(range(4, 11)) #>
>>> [ 4, 5, 6, 7, 8, 9, 10 ]
          0 1  2  3  4  5   6




ORGANIZAÇÃO:
    一一一一一一一一
valores.sort() #> Ordenar tudo 1234...
>>> [ 4, 5, 6, 7, 8, 9, 10 ]
          0 1  2  3  4  5   6

valores.sort(reverse=True) #> Ordenar tudo em ordem inversa 4321...
>>> [ 10, 9, 8, 7, 6, 5, 4 ]
           0   1  2  3  4  5 6



VERIFICAR:
    一一一一一一一一
len(valores) #> mostra quantidade de itens na lista
>>> 7

Valor.index(10) #> mostra a posição do item (passado). na lista

"""

#>Pratica aula 1:


num = [2, 5, 9, 1]
#            0 1   2  3

print(num)
# [2, 5, 9, 1]

num[2] = 3
print(num)
# [2, 5, 3, 1]

num.append(7)
print(num)
#[2, 5, 3, 1, 7]

num.sort()
print(num)
#[1, 2, 3, 5, 7]

num.sort(reverse=True)
print(num)
#[7, 5, 3, 2, 1]

num.insert(2, 0)
print(num)
# [7, 5, 0, 3, 2, 1]

print(len(num))
#>>> 6

num.pop()  #remove o último
print(num)
#[7, 5, 0, 3, 2]

num.pop(2)  #remove o último
print(num)
#[7, 5, 3, 2]

num = [7, 5, 2, 3, 2, 1]
print(num)
#[7, 5, 2, 3, 2, 1]

num.remove(2)
print(num)
#[7, 5, 3, 2, 1]


valores = []

valores.append(5)
valores.append(9)
valores.append(4)

print(valores)
#[5, 9, 4]

print()
for posição, valor in enumerate(valores):
    print(f"{posição = }   ==   {valor = }...", end=" ")
    print()
"""
posição = 0   ==   valor = 5...
posição = 1   ==   valor = 9...
posição = 2   ==   valor = 4...
"""
print()

a = [2, 3, 4, 7]
b = a  # as 2 vai apontar pro mesmo endereço na memória.

print(f"Lista A: {id(a)}")
print(f"Lista B: {id(b)}")
#Lista A: 529147256768
#Lista B: 529147256768

print(f"Lista A: {a}")
print(f"Lista B: {b}")
#Lista A: [2, 3, 4, 7]
#Lista B: [2, 3, 4, 7]


b[2] = 8
print(f"Lista A: {a}")
print(f"Lista B: {b}")

#Lista A: [2, 3, 8, 7]
#Lista B: [2, 3, 8, 7]

print()

a = [2, 3, 4, 7]
b = a[:]  # as 2 vai apontar pro endereço memória diferente

print(f"Lista A: {id(a)}")
print(f"Lista B: {id(b)}")
#Lista A: 501014549248
#Lista B: 501014614656

print(f"Lista A: {a}")
print(f"Lista B: {b}")
#Lista A: [2, 3, 4, 7]
#Lista B: [2, 3, 4, 7]

b[2] = 8
print(f"Lista A: {a}")
print(f"Lista B: {b}")

#Lista A: [2, 3, 4, 7]
#Lista B: [2, 3, 8, 7]










