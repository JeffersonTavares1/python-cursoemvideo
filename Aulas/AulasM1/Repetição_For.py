

#FOR == Laço com variável de controle:

"""
laço Var no intervalo(1, 10)
    passo
pega


for Var in range(1, 10):
    passo
pega

---------------

"""


#Praticas:


for c in range(1, 6):
    print(c)
print("fim")



for c in range(6, 0, -1): #-1 para contar pra trás
    print(c)
print("fim2")



for c in range(0, 7, 2): #2 e pulando de 2 em 2
    print(c)
print("fim3")




n = int(input("Digite um número: "))
for c in range(0, n+1):
    print(c)
print("fim4")


i = int(input("Inicio: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
for c in range(i, f+1, p):
    print(c)
print("fim4")




for c in range(0, 3):
    n = int(input("Digite um valor: "))
print("fim")




s = 0
for c in range(0, 4):
    n = int(input("Digite um valor: "))
    s += n #s = s + n
print("O somatório de todos os valores foi {}".format(s))




va= "jefferson"


for ind, val in enumerate(va):
    print(ind, val)
#>>> 0, "j"



texto = "Python"
i = 0

tamanho_string = len(texto)

while i < tamanho_string:
    print(texto[i])
    i += 1
    
print()

for cont in range(0, len(texto)):
    print(texto[cont])

print()

novo_texto = ""
for letra in texto:
    novo_texto += f"*{letra}"
    print(letra)

print(novo_texto + "*")


#range(start, stop, step)


número = range(5, 10)  #>>> range(5, 10), vai de 5 a 9.
número = range(5, 10, 2)  #>>> range(5, 10, 2), vai de 5 a 9 pulando de 2 em 2.
número = range(10)  #>>> range(0, 10)
print()

print(número[5])  #>>> 5, pegando o indese do range de 0 a 10

for valor in número:
    print(valor)

print()

número = range(0, -10, -1)  #se bota o pulo negativo, a parada tem que ser negativa também

for valor in número:
    print(valor)





# Como o For fuciona;

"""
Iterável -> str, range, etc (__iter__)

Iterador -> quem sabe entregar um valor por vez

next -> me entregue o próximo valor

iter -> me entregue seu iterador

__ == nome: dander
"""



# for letra in texto

texto = 'Luiz'  # iterável



# iteratador = iter(texto)  # iterator

texto = "Luiz".__iter__()  #mesma coisa de iter("Luiz")
print(texto)


texto = iter("Luiz")  #retorna o intereitor: <str_iterator object at 0x784243b040>
print(texto.__next__())  #>>> L
print(next(texto))             #>>> u, bote usar o função next()
print(texto.__next__())  #>>> i
print(texto.__next__())  #>>> z
#print(texto.__next__())  #>>> erro pos ja pegou tudo.

print()


#for fuciona assim:

# for letra in texto:
texto = "Luiz"  # iterável
iterador = iter(texto)  #iterador

while True:  #for e assim
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break
    



for i in range(10):
  #0, 9
    if i == 2:

        print('i é 2, pulando...')

        continue



    if i == 8:

        print('i é 8, seu else não executará')

        break



    for j in range(1, 3):

        print(i, j)

else:

    print('For completo com sucesso!')



































esso!')










