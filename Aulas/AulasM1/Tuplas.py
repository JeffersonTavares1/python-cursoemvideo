"""
Variável simples:                    | MEMÓRIA:
一一一一一一一一一一一一一一一一一一一一一一一一一一一
lanche = ""      →                        [    ]
lenche = "Hamburguer"      →       [ Hamburguer ]
lanche = "Suco"              →       [ Suco ]
一一一一一一一一一一一一一一一一一一一一一一一一一一一


Variável composta:  tupla    | MEMÓRIA:
一一一一一一一一一一一一一一一一一一一一一一一一一一一
lanche = [ Hanburguer, Suco, Piza, Pudin ]  c[ Hamburguer ]
                        0              1        2         3
for c in lanche:
    print(c) #Hamburguer
一一一一一一一一一一一一一一一一一一一
"""
#Tuplas São imutaveis ()

lanche = ("Hamburguer", "Suco", "Pizza", "Pudim", "Batata Frita")
print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[1: 3]) #desconsidera o indese 3
print(lanche[2:])
print(lanche[:2])

print()

for comida in lanche:
    print(comida)

print()

for c in range(0, len(lanche)): 
    print(lanche[c], c)

print()

for c, comida in enumerate(lanche):  #enumerate() > retorna o indese eo conteudo no for
    print(comida, c)

print()

print(sorted(lanche)) #> mostra o conteúdo em ordem alfabética.


print()

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a #juntar tuplas
print(c)

print(c.count(5)) #saber a contidade de 5 se nao tiver da 0

print(c.index(8)) #em que posição está o 8
print(c.index(5, 1)) #em que posição está o 5 apartir do indse 1

print()

pessoa = ("Jeffe", 23, "M", 75.97)
print(pessoa)

del(pessoa) #apagar tudo, variável, tuplas...
#print(pessoa) #da erro 

max() #maior valor
min() #min() menor valor

